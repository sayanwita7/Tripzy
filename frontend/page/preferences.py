import streamlit as st
import os
import requests
from components import sidebar
from dotenv import load_dotenv
load_dotenv()

def preferences_page():
    sidebar.sidebar_nav()
    st.markdown("""
    <style>
        /* Background with darker overlay */
        [data-testid="stAppViewContainer"] {
            background-image:
                linear-gradient(to top, rgba(0,0,0,0.75)50%, rgba(0,0,0,0.75)50%),
                url("https://res.cloudinary.com/dz3lffkkf/image/upload/v1756371915/kolkata-3331553_1280_nz2mff.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>✈️ Travel Preferences</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        trip_length = st.number_input("Trip Length in Days ⏰", min_value=1, step=1)
    with col2:
        options = { 
            "Low (~ INR 500)": "Low", 
            "Mid (~ INR 1500)": "Mid", 
            "High(~ INR 5000)": "High"}
        budgetChoice = st.selectbox("Comfortable Daily Budget 💳", list(options.keys()))
        budget=options[budgetChoice]
    col3, col4 = st.columns(2)
    with col3:
        options = { 
            "🧍 Solo - Discovering on Your Own": "Solo", 
            "💑 Partner - Exploring with a Loved One": "Partner", 
            "👨‍👩‍👧 Family - Traveling with Family": "Family", 
            "👯 Friends - Exploring with Friends": "Friends" }
        choice = st.radio("Traveling With 🚗", list(options.keys())) 
        travel_with = options[choice]
    with col4:
        arrival = [ "Dumdum Airport", "Howrah Railway Station","Sealdah Railway Station","Esplanade Bus Stand"]
        arrival_at = st.radio( "Arrival Point 📍", arrival)
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        if st.button("🚀 Plan", use_container_width=True):
            try:
                uri=os.getenv("FETCH_URL")
                with st.spinner("⏳ Generating your personalized itinerary... Please wait (~1 min)"):
                    response = requests.post(
                        uri, 
                        json={
                            "duration": trip_length,
                            "budget": budget,
                            "grouptype": travel_with,
                            "arrival": arrival_at,
                            "username": st.session_state.username
                        }
                    )
                data = response.json()
                if data:
                    st.session_state["itinerary_data"] = data
                    st.session_state.page = "itinerary"
                    st.rerun()
                else:  
                    st.error("Prediction failed. Try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"Server error: {e}")

        if st.button("⬅ Back", use_container_width=True):
            st.session_state.page = "landing"
            st.rerun()
