import streamlit as st
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from components import sidebar

def landing_page():
    sidebar.sidebar_nav()
    st.markdown("""
    <div class="hero">
        <h1>Tripzy, Travel with Ease</h1>
        <p>Plan your perfect Kolkata trip effortlessly! Choose your travel duration, budget, group type and arrival point, and let us craft a personalized itinerary that makes exploring the city smooth and enjoyable.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Plan a Trip", use_container_width=True):
        st.session_state.page = "preferences"
        st.rerun()
    st.markdown("""
    <div class="gallery">
        <img src="https://res.cloudinary.com/dz3lffkkf/image/upload/v1756380612/photo-1626198226928-617fc6c6203e_flwtrc.avif" alt="Tram">
        <img src="https://res.cloudinary.com/dz3lffkkf/image/upload/v1756380612/photo-1600080077823-a44592513861_flrsgb.avif" alt="Victoria Memorial">
        <img src="https://res.cloudinary.com/dz3lffkkf/image/upload/v1756380611/photo-1571679654681-ba01b9e1e117_udqkiw.avif" alt="Howrah Bridge">
    </div>
    """, unsafe_allow_html=True)

