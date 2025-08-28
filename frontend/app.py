import streamlit as st
import requests
import os
from dotenv import load_dotenv
from page import home, landing, login, preferences, register, profile, itinerary
from styles import load_styles

load_dotenv()
load_styles()
st.set_page_config(page_title="Tripzy", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown("""
        <div class="navbar">
            <img src="https://res.cloudinary.com/dz3lffkkf/image/upload/v1756384962/output-onlinepngtools_p7jlth.png" 
                alt="Logo 2" style="height:40px;">
            <img src="https://res.cloudinary.com/dz3lffkkf/image/upload/v1756372700/Logo_final_kalcpz.webp" 
                alt="Logo 1" style="height:40px; margin-right: 15px;">
        </div>
    """, unsafe_allow_html=True)

if st.session_state.page == "home":
    home.home_page()
elif st.session_state.page == "login":
    login.login_page()
elif st.session_state.page == "register":
    register.registration_page()
elif st.session_state.page == "landing":
    landing.landing_page()
elif st.session_state.page == "preferences":
    preferences.preferences_page()
elif st.session_state.page == "itinerary":
    itinerary.itinerary_page()
elif st.session_state.page == "profile":
    profile.profile_page()
