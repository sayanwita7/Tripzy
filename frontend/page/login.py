import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def login_page():
    st.markdown("""
    <style>
        /* Background with darker overlay */
        [data-testid="stAppViewContainer"] {
            background-image:
                linear-gradient(to top, rgba(0,0,0,0.75)50%, rgba(0,0,0,0.75)50%),
                url("https://res.cloudinary.com/dz3lffkkf/image/upload/v1756386179/d7f7eb13-33ce-423c-95fa-d43b64fa1513_rw_1920_xza0wj.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2>Login</h2>", unsafe_allow_html=True)
        uname = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login", use_container_width=True):
            if not uname or not password:
                st.error("Please enter both username and password")
            else:
                try:
                    uri=os.getenv("LOGIN_URL")
                    response = requests.post(
                        uri,
                        json={"username": uname, "password": password}
                    )
                    data = response.json()
                    if response.status_code == 200 and "userId" in data:
                        st.session_state.logged_in = True
                        st.session_state.username = uname
                        st.session_state.page = "landing"
                        st.rerun()
                    elif "error" in data:
                        st.error(data["error"])
                    else:
                        st.error("Login failed. Please try again.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to server: {e}")
        if st.button("Back to Home", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
