import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_bg_home
from src.ui.base_layout import style_base_layout
from src.components.footer import footer_home

def home_screen():

    style_base_layout()

    header_home()

    style_bg_home()

    
    

    col1 , col2 = st.columns(2  , gap = "large")

    with col1:
        st.markdown("## FOR TEACHERS")
        st.image("https://img.freepik.com/premium-photo/teacher-with-pointer-teaching-isolated-transparent-background-education-classroom-design_1029469-238301.jpg?w=2000" , width = 92)
        if st.button('Teacher Portal' , type = "primary", icon = ":material/arrow_outward:"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    with col2:
        st.markdown("## FOR STUDENTS")
        st.image("https://static.vecteezy.com/system/resources/previews/042/350/900/non_2x/ai-generated-generated-image-teacher-in-front-of-chalkboard-free-photo.jpg" , width = 149 )
        if st.button ('Student Portal' , type = "primary" , icon = ":material/arrow_outward:"):
            st.session_state['login_type'] = 'student'
            st.rerun()
        
    footer_home()



