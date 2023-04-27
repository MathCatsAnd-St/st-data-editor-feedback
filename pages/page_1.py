'''Page 1: validation and statefulness in multipage app'''

import streamlit as st
import pandas as pd
import numpy as np
from helper import page_tracker, init_page, keeper

PAGE = 'p1'
change = page_tracker(PAGE)
init_page(PAGE)

if 'memory_'+PAGE not in st.session_state:
    st.session_state['memory_'+PAGE] = False
st.session_state['_memory_'+PAGE] = st.session_state['memory_'+PAGE]
st.checkbox('Memory', key='_memory_'+PAGE, on_change=keeper, args=['memory_'+PAGE])

if change and st.session_state['memory_'+PAGE]:
    st.session_state['df_'+PAGE] = st.session_state['df_'+PAGE+'_valid']

def validate(row):
    if row['A'] < 0 or row['A'] > 100 or np.isnan(row['A']):
        return False
    if row['B'] < 0 or row['B'] > 100 or np.isnan(row['B']):
        return False
    if row['C'] < 0 or row['C'] > 100 or np.isnan(row['C']):
        return False
    if row['D'] < 0 or row['D'] > 100 or np.isnan(row['D']):
        return False
    return True

def reset():
    del st.session_state['df_'+PAGE]

st.button('Regenerate', on_click=reset)

df = st.session_state['df_'+PAGE]

cols = st.columns(4)

with cols[0]:
    st.subheader('Input df')
    st.write(df)
with cols[1]:
    st.subheader('Data Editor')
    df_out = st.experimental_data_editor(df,num_rows='dynamic', key='df_edit_'+PAGE)
with cols[2]:
    st.subheader('Raw output')
    st.write(df_out)

with cols[3]:
    df_valid = df_out[df_out.apply(validate, axis=1)]
    st.session_state['df_'+PAGE+'_valid'] = df_valid
    st.subheader('Validated Data Editor')
    result = st.experimental_data_editor(df_valid,num_rows='dynamic', key='df_reedit_'+PAGE)

st.code('''
def validate(row):
    if row['A'] < 0 or row['A'] > 100 or np.isnan(row['A']):
        return False
    if row['B'] < 0 or row['B'] > 100 or np.isnan(row['B']):
        return False
    if row['C'] < 0 or row['C'] > 100 or np.isnan(row['C']):
        return False
    if row['D'] < 0 or row['D'] > 100 or np.isnan(row['D']):
        return False
    return True
''')