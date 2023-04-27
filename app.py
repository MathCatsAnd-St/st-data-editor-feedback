'''Data Editor Feedback'''

import streamlit as st
from helper import page_tracker, init_page

st.set_page_config(layout='wide', page_icon=":cake:")

PAGE = 'home'
page_tracker(PAGE)
init_page(PAGE)

df = st.session_state['df_'+PAGE]

cols = st.columns(4)

with cols[0]:
    st.subheader('Input df')
    st.write(df)
    st.code('''
pd.DataFrame(
    np.random.randint(0,100,size=(5, 4)), 
    columns=list('ABCD')
)
    ''')
with cols[1]:
    st.subheader('Data Editor')
    df_out = st.experimental_data_editor(df,num_rows='dynamic', key='df_edit_'+PAGE)
    df_out2 = st.experimental_data_editor(df,key='df_edit_static_'+PAGE)
with cols[2]:
    st.subheader('Raw output')
    st.write(df_out)

with cols[3]:
    st.subheader('Data Re-Editor')
    st.experimental_data_editor(df_out,num_rows='dynamic', key='df_reedit_'+PAGE)

st.write('---')
st.write("Note the editor with dynamic rows does not show index, while the static one does. Various inconsistencies around index (page2, page3).")
st.write('Empty rows are not added until some edit happens somewhere. Feels like an unintentional lag/delay.')
st.write('Arrow keys don\'t work to highlight additional rows, but does work for individual cells. (`Shift`+up/down)')
st.write('State and widget output are completely different. As noted on #6540, editing state is not supported. (extra different from other widgets)')
st.write('Possible fluke: Had trouble pasting data copied from Excel or another dataframe in Edge. But after testing in '\
         'Firefox (worked) and then Chrome (prompted for permission, then worked), it started working in Edge without additional prompt. Not sure '\
         'if there was some permission carry-over from Chrome to Edge somehow. Relaunched the app on a different port and '\
         'Edge prompted for permission and worked.')