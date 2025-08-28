import streamlit as st

def home_page():
    st.markdown("""
    <div class="hero">
        <h1>Tripzy, Travel with Ease!</h1>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="small")
    with col2:
        if st.button("Sign In →", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()
    with col3:
        if st.button("Sign Up →", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()

    st.markdown("""
        <div style="
            padding:2.5rem; 
            background: linear-gradient(135deg, rgba(0,0,0,0.4), rgba(20,20,20,0.6)); 
            border-radius:15px; 
            margin-top:2rem; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            text-align: left;
        ">
            <p style="color:#f1f1f1; font-size:1.2rem; line-height:1.7; text-align:justify;">
                Planning a trip to Kolkata can be overwhelming – finding the best places to visit, 
                selecting restaurants, managing time, and ensuring everything fits your preferences. 
                <strong style="color:#ffea9b;">Tripzy</strong> simplifies it all by creating a personalized 
                travel itinerary tailored to your journey.
            </p>
            <h3 style="color:#ffea9b; margin-top:1.5rem;">What We Offer</h3>
            <ul style="color:#eee; font-size:1.05rem; line-height:1.8; padding-left:1.2rem;">
                <li><strong>Smart Recommendations</strong> – Handpicked hotels, restaurants, and attractions based on your budget.</li>
                <li><strong>Day-Wise Itinerary</strong> – A clear, organized plan of activities, meals, and sightseeing for each day.</li>
                <li><strong>Interactive Map Integration</strong> – Quick access to Google Maps for routes.</li>
                <li><strong>Customizable & Hassle-Free</strong> – Adjust your itinerary to match your pace and preferences.</li>
            </ul>
            <h3 style="color:#ffea9b; margin-top:1.5rem;">Why Choose Tripzy?</h3>
            <p style="color:#ddd; font-size:1.1rem; line-height:1.6; text-align:justify;">
                With real-time data, AI-driven suggestions, and a seamless user interface, 
                Tripzy helps you travel smarter – whether it's a weekend getaway or a week-long vacation.
            </p>
        </div>
    """, unsafe_allow_html=True)


    
