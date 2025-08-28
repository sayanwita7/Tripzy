import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(to top, rgba(0,0,0,0.5)50%,rgba(0,0,0,0.5)50%), 
        url("https://res.cloudinary.com/dz3lffkkf/image/upload/v1756371014/Landing_page_img_ynxer9.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .navbar {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        padding: 1rem 2rem;
        background-color: rgba(255, 255, 255, 0.2);
    }

    .navbar img {
        height: 40px;
    }


    /* Hero */
    .hero {
        text-align: center;
        padding: 20px 0;
        color: white;
    }
    .hero h1 span {
        color: #4285F4;
    }

    /* Buttons */
    .button {
        background-color: white;
        color: black;
        padding: 0.8rem 1.5rem;
        font-size: 1rem;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
        border: none;
    }
    .button:hover {
        background-color: grey;
    }
    /* Image gallery */
    .gallery {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 1rem;
        padding: 2rem;
        background-color: rgba(255,255,255,0.1);
    }
    .gallery img {
        width: 300px;
        height: 200px;
        object-fit: cover;
        border-radius: 12px;
    }
    /* Login/Register Box */
    .login-box {
        max-width: 400px;
        margin: 2rem auto;
        padding: 2rem;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
                
    /* Glassmorphism Itinerary Card */
        .stItinerary {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            border: 1px solid rgba(255,255,255,0.2);
            font-size: 1rem;
            line-height: 1.5;
            color: #fff;
        }
        /* Subheader Styling */
        .stSubheader {
            font-size: 1.3rem;
            font-weight: 700;
            color: #ffcb05; /* bright accent */
            margin-bottom: 0.75rem;
        }    
        .stItinerary ul {
            margin: 0.3rem 0;
            padding-left: 1.2rem;
        }
        .stItinerary li {
            margin: 0.2rem 0;
        }
                /* Full-width table */
        .itinerary-table {
            width: 100%;
            border-collapse: collapse;
            color: #fff;
        }

        .itinerary-table th, .itinerary-table td {
            border: 1px solid rgba(255,255,255,0.2);
            padding: 10px;
            text-align: center;
        }

        .itinerary-table th {
            background: rgba(255, 203, 5, 0.2);
            color: #ffcb05;
            font-weight: bold;
        }
                
        /* Table Container */
        .itinerary-table {
            width: 100%;
            margin-top: 20px;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.2);
        }

        /* Table row styling */
        .itinerary-row {
            display: flex;
            border-bottom: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.05);
            transition: 0.3s;
        }
        .itinerary-row:hover {
            background: rgba(255, 203, 5, 0.1);
        }

        /* Table cell styling */
        .itinerary-cell {
            flex: 1;
            padding: 12px;
            text-align: center;
            font-size: 0.95rem;
            color: #fff;
        }

        /* Header row */
        .itinerary-header {
            display: flex;
            background: rgba(255, 203, 5, 0.2);
            font-weight: bold;
            color: #ffcb05;
        }
    </style>
    """, unsafe_allow_html=True)
