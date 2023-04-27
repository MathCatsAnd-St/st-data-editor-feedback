'''Page 3: Different df constructions show index or not'''

import streamlit as st
import pandas as pd
import numpy as np
from helper import page_tracker, init_page

PAGE = 'p3'
page_tracker(PAGE)
init_page(PAGE)

cols = st.columns([2,1])

with cols[0]:
    subcols = st.columns(2)
    with subcols[0]:
        df = pd.DataFrame({'A':[1,2,3],'B':[1,2,3]})
        st.experimental_data_editor(df, num_rows='dynamic', key=PAGE+'_1')
    with subcols[1]:
        st.code('''
        df = pd.DataFrame(
                {'A':[1,2,3],'B':[1,2,3]}
             )
        ''')
    
    subcols = st.columns(2)
    with subcols[0]:
        A = pd.Series([1,2,3])
        B = pd.Series([1,2,3])
        df = pd.DataFrame()
        df['A'] = A
        df['B'] = B
        st.experimental_data_editor(df,num_rows='dynamic', key=PAGE+'_2')
    with subcols[1]:
        st.code('''
            A = pd.Series([1,2,3])
            B = pd.Series([1,2,3])
            df = pd.DataFrame()
            df['A'] = A
            df['B'] = B
        ''')

    subcols = st.columns(2)
    with subcols[0]:
        df = pd.DataFrame({'A':[1,2,3],'B':[1,2,3]})
        df['i'] = [0,1,2]
        df.set_index('i', inplace=True)
        st.experimental_data_editor(df,num_rows='dynamic', key=PAGE+'_3')
        st.write('Columns:')
        st.write(df.columns)
    with subcols[1]:
        st.code('''
        df = pd.DataFrame({'A':[1,2,3],'B':[1,2,3]})
        df['i'] = [0,1,2]
        df.set_index('i', inplace=True)
        ''')
        
    subcols = st.columns(2)
    with subcols[0]:
        df = pd.DataFrame({'A':[1,2,3],'B':[1,2,3]})
        df.index = list(df.index)
        st.experimental_data_editor(df,num_rows='dynamic', key=PAGE+'_4')
        st.write(df.columns)
    with subcols[1]:
        st.code('''
        df = pd.DataFrame({'A':[1,2,3],'B':[1,2,3]})
        df.index = list(df.index)
        ''')