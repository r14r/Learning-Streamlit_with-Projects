"""
Weather Dashboard - Advanced Project 05

Display weather information (demo data).
"""

import streamlit as st
import random

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="wide")

st.title("🌤️ Weather Dashboard")

cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
city = st.selectbox("Select City", cities)

# Demo weather data
random.seed(hash(city))
temp = random.randint(10, 30)
humidity = random.randint(40, 80)
wind = random.randint(5, 25)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperature", f"{temp}°C")
with col2:
    st.metric("💧 Humidity", f"{humidity}%")
with col3:
    st.metric("💨 Wind Speed", f"{wind} km/h")

st.subheader("📅 5-Day Forecast")

forecast_data = []
for i in range(5):
    forecast_data.append({
        'Day': f"Day {i+1}",
        'Temp': f"{temp + random.randint(-5, 5)}°C",
        'Condition': random.choice(["Sunny", "Cloudy", "Rainy"])
    })

cols = st.columns(5)
for i, data in enumerate(forecast_data):
    with cols[i]:
        st.write(f"**{data['Day']}**")
        st.write(data['Temp'])
        st.write(data['Condition'])

st.divider()
st.caption("Built with Streamlit 🎈")
