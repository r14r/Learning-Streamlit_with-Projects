"""
Step 4: Adding 5-Day Forecast Structure

In this step, we'll:
- Create a list to store forecast data
- Generate forecast data for 5 days
- Display forecast data in a simple list

Key Concepts:
- Lists and dictionaries for data storage
- for loops for generating multiple data points
- random.choice() for selecting random values
"""

import streamlit as st
import random

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="wide")

st.title("🌤️ Weather Dashboard")

cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
city = st.selectbox("Select City", cities)

# Generate demo weather data
random.seed(hash(city))
temp = random.randint(10, 30)
humidity = random.randint(40, 80)
wind = random.randint(5, 25)

# Current weather metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperature", f"{temp}°C")
with col2:
    st.metric("💧 Humidity", f"{humidity}%")
with col3:
    st.metric("💨 Wind Speed", f"{wind} km/h")

st.divider()

# Generate 5-day forecast
st.subheader("📅 5-Day Forecast")

forecast_data = []
for i in range(5):
    forecast_data.append({
        'Day': f"Day {i+1}",
        'Temp': f"{temp + random.randint(-5, 5)}°C",
        'Condition': random.choice(["Sunny", "Cloudy", "Rainy"])
    })

# Display forecast as a list for now
for data in forecast_data:
    st.write(f"**{data['Day']}**: {data['Temp']} - {data['Condition']}")

st.divider()
st.caption("Built with Streamlit 🎈")
