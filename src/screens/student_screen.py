import streamlit as st

import streamlit as st

from src.ui.base_layout import style_bg_dashboard , style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def student_screen():

    style_bg_dashboard()
    style_base_layout()
    c1,c2= st.columns(2 , vertical_alignment = 'center' , gap='large')


    with c1:
        header_dashboard()


    with c2:
        if st.button("Go back to home ->" , type = 'secondary' , key='lbb'):
            st.session_state['student_login_type'] = None
            st.rerun()
    st.markdown(
    "<h2 style='text-align:center;'>Login using FaceID</h2>",
    unsafe_allow_html=True
    )


    st.camera_input("Position your face in the center")

    footer_dashboard()
