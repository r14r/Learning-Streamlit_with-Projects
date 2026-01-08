"""
Production Deployment - Expert Project 10

Guide for deploying Streamlit apps to production.
"""

import streamlit as st

st.set_page_config(page_title="Production Deployment", page_icon="🚀", layout="wide")

st.title("🚀 Production Deployment Guide")

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Checklist", "Platforms", "Best Practices"])

with tab1:
    st.header("Deployment Overview")
    st.markdown("""
    ### Deployment Options:
    
    1. **Streamlit Community Cloud** (Free)
       - Direct GitHub integration
       - Free for public repos
       - Automatic deployments
    
    2. **Heroku**
       - Full control
       - Custom domains
       - Add-ons available
    
    3. **AWS/Azure/GCP**
       - Enterprise-grade
       - Scalable
       - Advanced features
    
    4. **Docker**
       - Containerized
       - Portable
       - Consistent environments
    """)

with tab2:
    st.header("✅ Deployment Checklist")
    
    checklist = [
        "Add requirements.txt with all dependencies",
        "Create .streamlit/config.toml for settings",
        "Add .gitignore for sensitive files",
        "Test with production-like data",
        "Optimize caching strategy",
        "Add error handling",
        "Set up logging",
        "Configure secrets management",
        "Test responsiveness",
        "Add analytics/monitoring"
    ]
    
    for item in checklist:
        st.checkbox(item, key=item)

with tab3:
    st.header("🌐 Deployment Platforms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Streamlit Cloud")
        st.code("""
# 1. Push to GitHub
git push origin main

# 2. Visit share.streamlit.io
# 3. Connect your GitHub repo
# 4. Deploy!
        """)
    
    with col2:
        st.subheader("Docker")
        st.code("""
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
        """)

with tab4:
    st.header("🎯 Best Practices")
    
    st.markdown("""
    ### Performance:
    - Use `@st.cache_data` for expensive computations
    - Use `@st.cache_resource` for ML models/connections
    - Implement pagination for large datasets
    - Optimize image sizes
    
    ### Security:
    - Never commit secrets to GitHub
    - Use `st.secrets` for sensitive data
    - Validate user inputs
    - Implement authentication if needed
    
    ### Monitoring:
    - Add logging
    - Track errors
    - Monitor performance
    - Set up alerts
    
    ### User Experience:
    - Add loading spinners
    - Provide helpful error messages
    - Make it mobile-friendly
    - Add documentation
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
