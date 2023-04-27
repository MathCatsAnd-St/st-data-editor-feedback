'''Page 2: Certain manipulations cause index to show and be editable'''

import streamlit as st
import pandas as pd
import numpy as np
from helper import page_tracker, init_page

PAGE = 'p2'
page_tracker(PAGE)
init_page(PAGE)

df = st.session_state['df_'+PAGE]
cols=st.columns(5)
with cols[0]:
    st.subheader('Input df')
    df1 = st.experimental_data_editor(df, key='edit_'+PAGE)
    df2 = st.experimental_data_editor(df, num_rows='dynamic', key='edit_dynamic_'+PAGE)

df = df.copy()
with cols[1]:
    st.subheader('Copied df')
    df1 = st.experimental_data_editor(df, key='copy_edit_'+PAGE)
    df2 = st.experimental_data_editor(df, num_rows='dynamic', key='copy_edit_dynamic_'+PAGE)
    st.write('Columns')
    subcols = st.columns(2)
    subcols[0].write(df2.columns)
    subcols[1].write(pd.DataFrame(df2.index))

df.reset_index(inplace=True)
with cols[2]:
    st.subheader('Reset Index')
    df1 = st.experimental_data_editor(df, key='reset_edit_'+PAGE)
    df2 = st.experimental_data_editor(df, num_rows='dynamic', key='reset_edit_dynamic_'+PAGE)
    st.write('Columns')
    subcols = st.columns(2)
    subcols[0].write(df2.columns)
    subcols[1].write(pd.DataFrame(df2.index))

df = df[df['A']>=0]
with cols[3]:
    st.subheader('Masked')
    df1 = st.experimental_data_editor(df, key='sub_'+PAGE)
    df2 = st.experimental_data_editor(df, num_rows='dynamic', key='sub_dynamic'+PAGE)
    st.write('Columns')
    subcols = st.columns(2)
    subcols[0].write(df2.columns)
    subcols[1].write(pd.DataFrame(df2.index))

df = df.copy()
with cols[4]:
    st.subheader('Copied again')
    df1 = st.experimental_data_editor(df, key='copy_reset_edit_'+PAGE)
    df2 = st.experimental_data_editor(df, num_rows='dynamic', key='copy_reset_edit_dynamic_'+PAGE)
