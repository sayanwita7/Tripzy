import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def sidebar_nav():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-image:
                linear-gradient(to bottom, rgba(0,0,0,0.2)0%, rgba(0,0,0,0.75)100%),
                url("https://res.cloudinary.com/dz3lffkkf/image/upload/v1756372285/pexels-photo-14449828_lzoqnr.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    LOGOUT_URL = os.getenv("LOGOUT_URL")
    PROFILE_URL=os.getenv("PROFILE_URL")
    username = st.session_state.get("username", "Guest")
    st.sidebar.markdown(
        """
        <div style="display: flex; align-items: center;">
            <img src="https://res.cloudinary.com/dz3lffkkf/image/upload/v1756384962/output-onlinepngtools_p7jlth.png" 
                style="width: 40px; height: auto; margin-right: 10px;">
            <img src="https://res.cloudinary.com/dz3lffkkf/image/upload/v1756372700/Logo_final_kalcpz.webp" 
                style="height: 40px; width: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown(f"👋 Welcome, {username} !")
    if st.session_state.get("page", "profile") != "profile":
        if st.sidebar.button("👤 Profile", key="profile_btn"):
            try:
                res=requests.post(PROFILE_URL, json={"username": username})
                data = res.json()
                if data:
                    st.session_state["itineraries"] = data["itineraries"]
                    st.session_state["user_info"] = data["user_info"]
                    st.session_state.page = "profile"
                    st.rerun()
                else:  
                    st.error("Profile fetch failed. Try again.")  
            except Exception as e:
                st.sidebar.error(f"Profile fetching error: {e}")
            
    if st.session_state.get("page", "landing") != "landing":
        if st.sidebar.button("🏠 Back to Landing Page", key="landing_btn"):
            st.session_state.page = "landing"
            st.rerun()
    if st.sidebar.button("🚪 Logout", key="logout_btn"):
        try:
            res = requests.get(LOGOUT_URL, timeout=5)
            if res.status_code == 200:
                st.sidebar.success("Logged out successfully!")
            else:
                st.sidebar.warning("Logout request failed.")
        except Exception as e:
            st.sidebar.error(f"Logout error: {e}")
        st.session_state.clear()
        st.session_state.page = "home"
        st.rerun()
