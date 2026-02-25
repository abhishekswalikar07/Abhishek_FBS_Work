import streamlit as st
import joblib
import numpy as np

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Weather Prediction App",
    page_icon="🌦",
    layout="wide"
)

# ---------------------------------
# Custom UI
# ---------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #007acc;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #005f99;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------
# Load Model (and scaler if used)
# ---------------------------------
model = joblib.load("weather_model.pkl")

# If you used StandardScaler during training, uncomment:
scaler = joblib.load("scaler.pkl")

# ---------------------------------
# Encoding Dictionaries
# ---------------------------------
Cloud_Cover = {'partly cloudy':0, 'clear':1, 'overcast':2, 'cloudy':3}
Season = {'Winter':0, 'Spring':1, 'Summer':2, 'Autumn':3}
Location_dict = {'inland':0, 'mountain':1, 'coastal':2}

# ---------------------------------
# Title
# ---------------------------------
st.title("🌦 Weather Classification Predictor")
st.markdown("Predict Weather Type using Atmospheric Conditions")

st.markdown("---")

# ---------------------------------
# Sidebar Inputs
# ---------------------------------
st.sidebar.header("📌 Enter Weather Details")

cloud = st.sidebar.selectbox("Cloud Cover",
                             ["Select"] + list(Cloud_Cover.keys()))

season_type = st.sidebar.selectbox("Season",
                                   ["Select"] + list(Season.keys()))

location = st.sidebar.selectbox("Location",
                                 ["Select"] + list(Location_dict.keys()))

temperature = st.sidebar.number_input("Temperature (°C)", value=25.0)
wind_speed = st.sidebar.number_input("Wind Speed", value=10.0)
precipitation = st.sidebar.number_input("Precipitation %", value=20.0)
uv_index = st.sidebar.number_input("UV Index", value=5)
visibility_km = st.sidebar.number_input("Visibility (KM)", value=10.0)

st.markdown("---")

# ---------------------------------
# Prediction
# ---------------------------------
if st.button("🔍 Predict Weather"):

    if cloud == "Select" or season_type == "Select" or location == "Select":
        st.warning("⚠ Please select all dropdown values.")
    else:
        with st.spinner("Analyzing..."):

            # Convert string to encoded numbers
            cloud_encoded = Cloud_Cover[cloud]
            season_encoded = Season[season_type]
            location_encoded = Location_dict[location]

            # Arrange in SAME order as training
            user_data = np.array([[temperature,
                                   wind_speed,
                                   precipitation,
                                   cloud_encoded,
                                   uv_index,
                                   season_encoded,
                                   visibility_km,
                                   location_encoded]])

            # If you used scaling:
            user_data_scaled = scaler.transform(user_data)

            prediction = model.predict(user_data_scaled)
            # probability = model.predict_proba(user_data_scaled)

            # confidence = round(np.max(probability) * 100, 2)

            st.markdown("## 📢 Prediction Result")

            if prediction[0] == 0:
                st.success("🌧 Weather is Rainy... Use umbrella!!!")
            elif prediction[0] == 1:
                st.info("☁ Cloudy weather... Rain may come!!!")
            elif prediction[0] == 2:
                st.success("☀ Sunny weather... Sun is here !!!")
            else:
                st.warning("❄ It's snow time.. Snowfall is near!!!")

            # st.write(f"### Model Confidence: {confidence}%")