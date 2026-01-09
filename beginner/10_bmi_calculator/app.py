"""
BMI Calculator - Beginner Project 10

Calculate Body Mass Index and provide health assessment.
"""

import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)

st.title("⚕️ BMI Calculator")
st.write("Calculate your Body Mass Index and understand your health status")

# Unit selection
unit_system = st.radio("Select unit system:", ["Metric (kg, cm)", "Imperial (lbs, inches)"], horizontal=True)

# Input fields based on unit system
col1, col2 = st.columns(2)

if unit_system == "Metric (kg, cm)":
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    with col2:
        height = st.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
    
    # Convert height to meters for calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)
else:
    with col1:
        weight = st.number_input("Weight (lbs)", min_value=1.0, max_value=700.0, value=154.0, step=0.1)
    with col2:
        height = st.number_input("Height (inches)", min_value=20.0, max_value=120.0, value=67.0, step=0.1)
    
    # Convert to metric for BMI calculation
    weight_kg = weight * 0.453592
    height_m = height * 0.0254
    bmi = weight_kg / (height_m ** 2)

# Calculate button
if st.button("Calculate BMI", type="primary"):
    st.divider()
    
    # Determine category
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
        emoji = "🔵"
        advice = "Consider consulting a healthcare provider for guidance on healthy weight gain."
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "green"
        emoji = "🟢"
        advice = "Great! Maintain your healthy lifestyle with balanced diet and regular exercise."
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "orange"
        emoji = "🟠"
        advice = "Consider a balanced diet and regular physical activity to reach a healthier weight."
    else:
        category = "Obese"
        color = "red"
        emoji = "🔴"
        advice = "Consult with a healthcare provider for personalized guidance on weight management."
    
    # Display result
    st.markdown(f"### Your BMI: {bmi:.1f}")
    st.markdown(f"### Category: {emoji} {category}")
    
    # BMI scale visualization
    st.subheader("📊 BMI Scale")
    
    # Create a visual scale
    scale_html = f"""
    <div style="background: linear-gradient(to right, #3498db 0%, #2ecc71 25%, #f39c12 50%, #e74c3c 75%, #c0392b 100%); 
                height: 30px; border-radius: 5px; position: relative; margin: 20px 0;">
        <div style="position: absolute; left: {min(max((bmi/40)*100, 0), 100)}%; 
                    top: -5px; transform: translateX(-50%);">
            <div style="background: white; border: 2px solid black; border-radius: 50%; 
                        width: 20px; height: 20px;"></div>
            <div style="text-align: center; margin-top: 5px; font-weight: bold;">↑</div>
        </div>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 12px;">
        <span>Underweight<br>(&lt;18.5)</span>
        <span>Normal<br>(18.5-24.9)</span>
        <span>Overweight<br>(25-29.9)</span>
        <span>Obese<br>(≥30)</span>
    </div>
    """
    st.markdown(scale_html, unsafe_allow_html=True)
    
    # Health advice
    st.info(f"💡 **Health Advice**: {advice}")
    
    # Additional metrics
    with st.expander("📋 Detailed Information"):
        st.write(f"**BMI Value**: {bmi:.2f}")
        st.write(f"**Category**: {category}")
        
        if unit_system == "Metric (kg, cm)":
            st.write(f"**Your Weight**: {weight} kg")
            st.write(f"**Your Height**: {height} cm")
            
            # Healthy weight range
            min_healthy = 18.5 * (height_m ** 2)
            max_healthy = 24.9 * (height_m ** 2)
            st.write(f"**Healthy Weight Range**: {min_healthy:.1f} - {max_healthy:.1f} kg")
        else:
            st.write(f"**Your Weight**: {weight} lbs")
            st.write(f"**Your Height**: {height} inches")
            
            # Healthy weight range
            min_healthy = 18.5 * (height_m ** 2) / 0.453592
            max_healthy = 24.9 * (height_m ** 2) / 0.453592
            st.write(f"**Healthy Weight Range**: {min_healthy:.1f} - {max_healthy:.1f} lbs")

# Information about BMI
with st.expander("ℹ️ About BMI"):
    st.markdown("""
    **Body Mass Index (BMI)** is a measure of body fat based on height and weight.
    
    **BMI Categories:**
    - **Underweight**: BMI < 18.5
    - **Normal weight**: BMI 18.5 - 24.9
    - **Overweight**: BMI 25 - 29.9
    - **Obese**: BMI ≥ 30
    
    **Note**: BMI is a screening tool and doesn't directly measure body fat percentage. 
    Factors like muscle mass, bone density, and overall body composition are not taken into account.
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
