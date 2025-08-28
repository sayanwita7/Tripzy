import streamlit as st
import pandas as pd
import requests
from components import sidebar
import os
from dotenv import load_dotenv
load_dotenv()

def profile_page():
    sidebar.sidebar_nav()
    history_response = {
        "itineraries": st.session_state.get("itineraries", []),
        "user_info": st.session_state.get("user_info", {})
    }
    st.markdown("""
    <style>
        /* Background with darker overlay */
        [data-testid="stAppViewContainer"] {
            background-image:
                linear-gradient(to top, rgba(0,0,0,0.75)50%, rgba(0,0,0,0.75)50%),
                url("https://res.cloudinary.com/dz3lffkkf/image/upload/v1756371262/Itineray_page_img.jpeg_yaszbd.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <div class="stItinerary">
            <h2 class="stSubheader">👤 {history_response['user_info'].get('name', '')} ({history_response['user_info'].get('username', '')})</h2>
            <p>📧 Email: {history_response['user_info'].get('email', '')}</p>
            <p>📞 Phone: {history_response['user_info'].get('phone', '')}</p>
        </div>
        """, unsafe_allow_html=True)
    itinerary_list = history_response["itineraries"]
    if itinerary_list:
        df = pd.DataFrame(itinerary_list)
        df_display = df.drop(columns=["itinerary_id"]).copy()
        header_cols = st.columns(len(df_display.columns) + 1)
        for i, col_name in enumerate(df_display.columns):
            header_cols[i].markdown(f"<div class='itinerary-cell'><b>{col_name}</b></div>", unsafe_allow_html=True)
        header_cols[-1].markdown(f"<div class='itinerary-cell'><b>Action</b></div>", unsafe_allow_html=True)
        for idx, row in df.iterrows():
            cols = st.columns(len(df_display.columns) + 1)
            for i, col_name in enumerate(df_display.columns):
                cols[i].markdown(f"<div class='itinerary-cell'>{row[col_name]}</div>", unsafe_allow_html=True)
            if cols[-1].button("View", key=f"view_{row['itinerary_id']}"):
                FETCH_IT_URL=os.getenv("FETCH_IT_URL")
                url = f"{FETCH_IT_URL}/{row['itinerary_id']}"
                response = requests.get(url)
                if response.status_code == 200:
                    st.session_state["itinerary_data"] = response.json()
                    st.session_state.page = "itinerary"
                    st.rerun()
                else:
                    st.error("Failed to fetch itinerary details")
    else:
        st.markdown("""
        <div>
            <p>No available history!</p>
        </div>
        """, unsafe_allow_html=True)