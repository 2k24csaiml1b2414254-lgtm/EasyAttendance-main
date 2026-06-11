import streamlit as st


def header_home():
    logo_url = "https://static.vecteezy.com/system/resources/previews/020/088/534/original/teacher-and-students-are-studying-in-the-classroom-cartoon-vector.jpg"



    st.markdown(f"""
        <div style = "display:flex; flex-direction:column; align-items:center; justify-content:center ; margin-bottom : 30px;">
            <img src = '{logo_url}' style = 'height:100px';></img>
            <h1 style = 'text-align:center; color: #E0E3FF'>EASY <br>  ATTENDANCE</h1>
        </div>
    """ , unsafe_allow_html = True)




def header_dashboard():
    logo_url = "https://static.vecteezy.com/system/resources/previews/020/088/534/original/teacher-and-students-are-studying-in-the-classroom-cartoon-vector.jpg"



    st.markdown(f"""
        <div style = "display:flex; align-items:center; justify-content:center ; gap :10px">
            <img src = '{logo_url}' style = 'height:85px';></img>
            <h2 style = 'text-align:center; color: #5865F2'>EASY <br>  ATTENDANCE</h1>
        </div>
    """ , unsafe_allow_html = True)