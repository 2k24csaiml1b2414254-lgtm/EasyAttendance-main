import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code):
    std_id = st.session_state.student_data['std_id']



    res = supabase.table('subjects').select('sub_id , name').eq('subject_code' , subject_code).execute()
    if not res.data:
        st.error('Subject Code NOT found!')
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()
        return 
    
    subject = res.data[0]
    check = supabase.table('subject_students').select('*').eq('sub_id' , subject['sub_id']).eq('std_id' , std_id).execute()
    if check.data:
        st.info('You are already enrolled! ')
        if st.button('Got it!'):
            st.query_params.clear()
            st.rerun()
        return
    
    st.markdown(f'Would you like to enroll in **{subject['name']}**?')


    col1 , col2 = st.columns(2)

    with col1:
        if st.button('No Thanks!'):
            st.query_params.clear()
            st.rerun()
    with col2:
        if st.button('Yes Enroll Now !' , type = 'primary' , width = 'stretch'):
            enroll_student_to_subject(std_id , subject['sub_id'])
            st.success('Joined Succesfully!')
            st.query_params.clear()
            time.sleep(2)
            st.rerun()
