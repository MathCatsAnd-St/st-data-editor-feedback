'''Helper script'''

import streamlit as st
import pandas as pd
import numpy as np

def page_tracker(page):
    '''Track when pages are switched or rerun
    
    Arguments
        page:str -- Page name
    
    Returns
        bool -- True if page has been switched; False if page has
        been rerun
    '''
    if 'page' not in st.session_state:
        st.session_state.page = page
        return True
    if st.session_state.page == page:
        return False
    st.session_state.page = page
    return True

def init_page(page:str):
    '''Generate dataframe to initialize session state values for a page
    '''
    if 'df_'+page not in st.session_state:
        st.session_state['df_'+page] = pd.DataFrame(np.random.randint(0,100,size=(5, 4)), columns=list('ABCD'))
        st.session_state['df_'+page+'_valid'] = st.session_state['df_'+page].copy()

def keeper(key):
    st.session_state[key] = st.session_state['_'+key]