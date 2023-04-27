'''Page 5: more complex validation example'''

import streamlit as st
import pandas as pd
import numpy as np
from helper import page_tracker, keeper

PAGE = 'p5'
change = page_tracker(PAGE)

if 'memory_'+PAGE not in st.session_state:
    st.session_state['memory_'+PAGE] = False
st.session_state['_memory_'+PAGE] = st.session_state['memory_'+PAGE]
st.checkbox('Memory', key='_memory_'+PAGE, on_change=keeper, args=['memory_'+PAGE])

if change and st.session_state['memory_'+PAGE]:
    st.session_state['df_'+PAGE] = st.session_state['df_'+PAGE+'_valid']

def validation_ex_init():
    st.session_state['df_'+PAGE] = pd.DataFrame({
        'A':[False, True, True, True],
        'B':[0.0,1.0,1.0,2.0],
        'C':[False, False, True, True],
        'D':[0.0,0.0,2.0,np.inf]
    })
    st.session_state['df_'+PAGE+'_valid'] = st.session_state['df_'+PAGE].copy()

if 'df_'+PAGE not in st.session_state:
    validation_ex_init()

df = st.session_state['df_'+PAGE]

st.button('Restart', on_click=validation_ex_init)

def validate(row):
    if not row['A'] and row['C']:
        return False
    if not row['A'] and not (np.isnan(row['B']) or row['B'] == 0):
        return False
    if row['A'] and (row['B'] <= 0 or np.isnan(row['B'])):
        return False
    if row['C'] and (np.isnan(row['D']) or row['D'] <= row['B']):
        return False
    if not row['C'] and not (np.isnan(row['D']) or row['D'] == 0):
        return False
    return True

def highlight_invalid(row):
    if not validate(row):
        return ['background-color: red']*len(row)
    return['']*len(row)

cols = st.columns(4)

with cols[0]:
    st.subheader('Input df')
    st.write(df)
with cols[1]:
    st.subheader('Data Editor')
    df_out = st.experimental_data_editor(df,num_rows='dynamic', key='df_edit_'+PAGE)
with cols[2]:
    st.subheader('Raw output')
    st.write(df_out.style.apply(highlight_invalid, axis=1))

with cols[3]:
    df_valid = df_out[df_out.apply(validate, axis=1)]
    st.session_state['df_'+PAGE+'_valid'] = df_valid
    st.subheader('Validated Data Editor')
    result = st.experimental_data_editor(df_valid,num_rows='dynamic', key='df_reedit_'+PAGE)