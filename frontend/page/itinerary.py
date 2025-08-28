import streamlit as st
from components import sidebar
import time
import re

def show_loading_screen():
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
    with st.spinner("Loading your itinerary..."):
        time.sleep(1.5)

def itinerary_page():
    show_loading_screen()
    sidebar.sidebar_nav()
    st.markdown("""
    <style>
        /* Background with darker overlay */
        [data-testid="stAppViewContainer"] {
            background-image:
                linear-gradient(to top, rgba(0,0,0,0.75)50%, rgba(0,0,0,0.75)50%),
                url("https://res.cloudinary.com/dz3lffkkf/image/upload/v1756371533/photo-1536421469767-80559bb6f5e1_kxx1pt.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    """, unsafe_allow_html=True)
    data = st.session_state.get("itinerary_data", None)
    if not data:
        st.warning("⚠️ No itinerary found. Please go back and generate one.")
        st.stop()
    hotel_info_raw = data.get("Hotel", "No hotel info found")
    lines = hotel_info_raw.split("\n")
    hotel_line = lines[0].strip()
    maps_line = lines[1].replace("Maps:", "").strip() if len(lines) > 1 else None
    match = re.match(r"^(.*)\s\((.*)\)$", hotel_line)
    if match:
        hotel_name, details = match.groups()
    else:
        hotel_name, details = hotel_line, ""
    st.markdown(f"""
    <div class="stItinerary">
        <h3 style="margin:0; color:#4da6ff;">🏨 Hotel Recommendation: {hotel_name}</h3>
        <p style="margin:0.5rem 0; color:#eee;">💰 {details}</p>
        {"<p>📍 <a href='"+maps_line+"' target='_blank' style='color:#9cf;'>View on Google Maps</a></p>" if maps_line else ""}
    </div>
    """, unsafe_allow_html=True)
    itinerary = data.get("Itinerary", {})
    if not itinerary:
        st.json(itinerary)
        st.stop()
    if "current_day" not in st.session_state:
        st.session_state.current_day = 0
    days = itinerary.get("days", [])
    if not days:
        st.info("No detailed day-wise itinerary available.")
        st.stop()
    current_day = days[st.session_state.current_day]
    st.title("📅 Travel Itinerary")
    st.subheader(f"📍 Day {current_day.get('day_number')} – {current_day.get('area_focus', '')}")
    st.markdown("### 🍴 Meals")
    meal_order = ["Breakfast", "Lunch", "Snacks", "Dinner"]
    meals = current_day["meals"]
    ordered_meals = {m: meals[m] for m in meal_order if m in meals}
    meal_cols = st.columns(len(ordered_meals))
    for col, (meal_name, meal_info) in zip(meal_cols, ordered_meals.items()):
        with col:
            html = f"""
            <div class="stItinerary">
                <h4 style="margin:0; color:#4da6ff;">🍽️ {meal_name}</h4>
                <p style="margin:0.3rem 0; color:#eee;">
                    ⏱ {meal_info.get('allocated_minutes', 'N/A')} mins
                </p>
            """
            if meal_info.get("suggested_restaurants"):
                html += "<ul style='margin:0.3rem 0; padding-left:1.2rem;'>"
                for r in meal_info["suggested_restaurants"]:
                    distance = f" ({r['distance_km_from_hotel']} km)" if r.get("distance_km_from_hotel") else ""
                    html += f"<li style='margin:0.2rem 0;'>🍴 {r['name']}{distance}</li>"
                html += "</ul>"
            html += "</div>"
            st.markdown(html, unsafe_allow_html=True)
    if current_day.get("items"):
        st.markdown("### 🎯 Activities & Spots")
        for item in current_day["items"]:
            duration = item.get('duration_minutes')
            distance = item.get('distance_km_from_hotel')
            details = []
            if duration is not None:
                details.append(f"⏱ {duration} mins")
            if distance is not None:
                details.append(f"📏 {distance} km")
            details_line = " | ".join(details) if details else ""
            html = f"""
            <div class="stItinerary">
                <h4 style="margin:0; color:#4da6ff;">{item['name']} ({item['type']})</h4>
                {"<p style='margin:0.3rem 0;'>" + details_line + "</p>" if details_line else ""}
            """
            if item.get("description"):
                html += f"<p style='margin:0.3rem 0; color:#eee;'>{item['description']}</p>"
            if item.get("spot_type"):
                html += f"<p style='margin:0.3rem 0;'>🏷️  Spot Type: {item['spot_type']}</p>"
            if item.get("top_activities"):
                html += f"<p style='margin:0.3rem 0;'>✨ Activities: {item['top_activities']}</p>"
            if item.get("images"):
                html += "<div style='display:flex; gap:0.5rem; margin-top:0.5rem;'>"
                for img in item["images"][:5]: 
                    html += f"<img src='{img}' style='width:100%; border-radius:12px;' />"
                html += "</div>"
            html += "</div>"
            st.markdown(html, unsafe_allow_html=True)
    if current_day.get("maps_route_url"):
        maps_html = f"""
        <div class="stItinerary">
            <h4 style="margin:0; color:#4da6ff;">🗺️ Route Map</h4>
            <p style="margin:0.3rem 0;">
                <a href="{current_day['maps_route_url']}" target="_blank" style="color:#9cf; text-decoration:none;">
                    View Route on Google Maps
                </a>
            </p>
        </div>
        """
        st.markdown(maps_html, unsafe_allow_html=True)
    if current_day.get("transportation_tips"):
        st.info(current_day["transportation_tips"])
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.session_state.current_day > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current_day -= 1
                st.rerun()
    with col3:
        if st.session_state.current_day < len(days) - 1:
            if st.button("Next ➡️"):
                st.session_state.current_day += 1
                st.rerun()
    if st.button("Back to Home", use_container_width=True):
        st.session_state.page = "landing"
        st.rerun()
