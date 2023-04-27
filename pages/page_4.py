'''Page 4: Editing widget key value in session state'''

import streamlit as st
import pandas as pd
import numpy as np
from helper import page_tracker, init_page

PAGE = 'p4'
change = page_tracker(PAGE)
init_page(PAGE)

st.write(st.session_state)
st.session_state[PAGE+'_test']={}

df = st.session_state['df_'+PAGE]

st.experimental_data_editor(df, key=PAGE+'_test')
st.button('Test', key=PAGE+'_button')

st.write(st.session_state)

