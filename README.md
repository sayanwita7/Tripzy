Tripzy - AI-Powered Itinerary Generator
Tripzy is a personalized trip planning tool built using Streamlit (Frontend) and Flask (Backend). It generates customized travel itineraries for touring around Kolkata based on preferences like trip duration, budget, travel group and arrival location.

Tech Stack:
1. Frontend: Streamlit
2. Backend: Flask
3. Database: MongoDB
4. Language: Python

Project Structure:

1. frontend : 
(a) app.py: Main Streamlit UI file ; (b) style.py : File containing all common styling ; (c) page : Pages ; (d) components : Common component across all pages; (e) requirements.txt : Frontend dependencies; (f) venv/ : Virtual environment (not pushed to GitHub); (g) .env : Frontend environment variables;

2. backend :
(a) app.py: Main backend server; (b) model : ML model; (c) requirements.txt : Backend dependencies; (d) .env : Backend environment variables

Project Setup Guide:

1. Clone the Repository : 
git clone https://github.com/sayanwita7/Tripzy
2. Navigate to the backend folder: 
cd backend
3. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux
4. Install dependencies:
pip install -r requirements.txt
5. Run the Flask server:
python app.py
6. In a separate terminal, navigate to the frontend folder:
cd frontend
7. Repeat steps 3 and 4 to create the virtual environment and install dependencies
8. Run the streamlit app:
streamlit run app.py

Environment variables for backend:
1. MONGO_DB_URL=your_mongodb_url

Environment variables for frontend: (sample)
1. REGISTER_URL = http://localhost:5000/user/register
2. LOGIN_URL = http://localhost:5000/user/login
3. LOGOUT_URL = http://localhost:5000/user/logout
4. PROFILE_URL = http://localhost:5000/user/history
5. FETCH_URL = http://localhost:5000/itinerary/predict
