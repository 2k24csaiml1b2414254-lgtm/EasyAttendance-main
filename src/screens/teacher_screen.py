import streamlit as st

from src.ui.base_layout import style_bg_dashboard , style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.database.db import check_teacher_exists, create_teacher , teacher_login



def teacher_screen():
    style_bg_dashboard()
    style_base_layout()



    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type =="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()



def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    st.header(f"""Welcome, {teacher_data['name']}""")

     

def login_teacher(username , password):
    if not username or not password:
        return False
     
    teacher = teacher_login(username , password)


    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False



def teacher_screen_login():


    c1,c2= st.columns(2 , vertical_alignment = 'center' , gap='large')


    with c1:
        header_dashboard()


    with c2:
        if st.button("Go back to home ->" , type = 'secondary' , key='lbb'):
            st.session_state['teacher_login_type'] = None
            st.rerun()
    st.markdown(
    "<h2 style='text-align:center;'>Login using password</h2>",
    unsafe_allow_html=True
    )
    



    teacher_username = st.text_input("enter username" , placeholder = "name")

    teacher_pass = st.text_input("enter password" , type = "password" , placeholder = "enter password")



    st.divider()




    btnc1 , btnc2 = st.columns(2)


    with btnc1:
            if st.button('Login' , type = 'primary' , icon = ":material/login:" , width='stretch'):
                if login_teacher(teacher_username , teacher_pass):
                    st.toast("Welcome back!" , icon = "🎉")
                    import time
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username and password combo")
    with btnc2:
            if st.button('Register Now' , icon = ":material/account_box:" , width='stretch'):
                st.session_state.teacher_login_type = 'register'
                st.rerun()




    footer_dashboard()


def register_teacher(teacher_username , teacher_name , teacher_pass , teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
          return False , "All Fields are required!"
    if check_teacher_exists(teacher_username):
          return False , "Username already taken"
    if teacher_pass != teacher_pass_confirm:
          return False , "Password doesn't match"
    
    try:
        create_teacher(teacher_username , teacher_pass , teacher_name)
        return True , "Successfully Created! Login Now"
    except Exception as e:
         return False, f"{e}"
     




def teacher_screen_register():


    c1,c2= st.columns(2 , vertical_alignment = 'center' , gap='large')


    with c1:
        header_dashboard()


    with c2:
        if st.button("Go back to home ->" , type = 'secondary' , key='lbb'):
            st.session_state['login_type'] = None
            st.rerun()
    st.markdown(
    "<h2 style='text-align:center;'>Register now</h2>",
    unsafe_allow_html=True
    )
    



    teacher_username = st.text_input("enter username" , placeholder = "name")

    teacher_name = st.text_input("enter name" , placeholder = "name")

    teacher_pass = st.text_input("enter password" , type = "password" , placeholder = "enter password")


    teacher_pass_confirm = st.text_input("confirm your password" , type = "password" , placeholder = "enter password")


    st.divider()




    btnc1 , btnc2 = st.columns(2)


    with btnc1:
            if st.button('Login' , type = 'primary' , icon = ":material/login:" , width='stretch'):
                st.session_state.teacher_login_type = 'login'
    with btnc2:
            if st.button('Register Now' , icon = ":material/account_box:" , width='stretch'):
                success , message = register_teacher(teacher_username , teacher_name , teacher_pass , teacher_pass_confirm)
                if success:
                    st.success(message)
                    import time
                    time.sleep(2)
                    st.session_state.teacher_login_type = "login"
                    st.rerun()
                else:
                     st.error(message)
                      




    footer_dashboard()









