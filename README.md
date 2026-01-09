# Learning Streamlit with Projects

A comprehensive collection of 30 Streamlit applications organized by difficulty level, designed to help you learn Streamlit through practical, hands-on projects. Each app comes with detailed requirements documentation (specifications) describing functionality, inputs, outputs, and tests.

## 📚 Project Structure

This repository contains 30 Streamlit applications divided into three difficulty levels:
- **Beginner** (10 apps): Fundamental Streamlit concepts and widgets
- **Advanced** (10 apps): Intermediate Streamlit features and data visualization
- **Expert** (10 apps): Advanced Streamlit patterns, caching, and deployment

Each app is contained in its own directory with:
- `app.py` - The Streamlit application
- `specifications.md` - Requirements document with functionality, I/O specs, and test cases

## 🎯 Beginner Level

Perfect for those starting their Streamlit journey. Learn basic widgets, layouts, and interactivity.

| # | Project | Description |
|---|---------|-------------|
| 01 | [Hello Streamlit](beginner/01_hello_streamlit/) | Basic text display and markdown |
| 02 | [Interactive Calculator](beginner/02_interactive_calculator/) | Input widgets and arithmetic operations |
| 03 | [Text Analyzer](beginner/03_text_analyzer/) | Text input and string analysis |
| 04 | [Data Display](beginner/04_data_display/) | DataFrames and tables |
| 05 | [Temperature Converter](beginner/05_temperature_converter/) | Number input and unit conversion |
| 06 | [Image Gallery](beginner/06_image_gallery/) | File uploader and image display |
| 07 | [Color Picker Tool](beginner/07_color_picker_tool/) | Color widgets and hex/RGB conversion |
| 08 | [Simple Survey Form](beginner/08_simple_survey_form/) | Multiple input types and form submission |
| 09 | [Number Guessing Game](beginner/09_number_guessing_game/) | Session state and game logic |
| 10 | [BMI Calculator](beginner/10_bmi_calculator/) | Sliders and health calculations |

## 🚀 Advanced Level

Build on fundamentals with charts, data visualization, and external data sources.

| # | Project | Description |
|---|---------|-------------|
| 01 | [Data Visualizer](advanced/01_data_visualizer/) | Interactive charts with plotly |
| 02 | [CSV Analyzer](advanced/02_csv_analyzer/) | Upload and analyze CSV files |
| 03 | [API Dashboard](advanced/03_api_dashboard/) | Fetch and display REST API data |
| 04 | [Stock Price Tracker](advanced/04_stock_price_tracker/) | Real-time stock data visualization |
| 05 | [Weather Dashboard](advanced/05_weather_dashboard/) | Weather API integration |
| 06 | [TODO List Manager](advanced/06_todo_list_manager/) | Persistent task management with session state |
| 07 | [Data Filter Explorer](advanced/07_data_filter_explorer/) | Advanced filtering and search |
| 08 | [Multi-Page App](advanced/08_multi_page_app/) | Navigation and page structure |
| 09 | [Form Validator](advanced/09_form_validator/) | Complex form validation |
| 10 | [Quiz Application](advanced/10_quiz_application/) | Interactive quiz with scoring |

## 💎 Expert Level

Master advanced Streamlit concepts including caching, optimization, and production patterns.

| # | Project | Description |
|---|---------|-------------|
| 01 | [ML Model Dashboard](expert/01_ml_model_dashboard/) | Machine learning model deployment |
| 02 | [Real-Time Data Stream](expert/02_realtime_data_stream/) | Live data updates with auto-refresh |
| 03 | [Advanced Caching](expert/03_advanced_caching/) | Optimal caching strategies |
| 04 | [Custom Components](expert/04_custom_components/) | Create custom Streamlit components |
| 05 | [Database Integration](expert/05_database_integration/) | SQL database CRUD operations |
| 06 | [Authentication System](expert/06_authentication_system/) | User login and session management |
| 07 | [Data Pipeline Monitor](expert/07_data_pipeline_monitor/) | ETL pipeline visualization |
| 08 | [A/B Testing Dashboard](expert/08_ab_testing_dashboard/) | Statistical analysis and visualization |
| 09 | [Performance Optimizer](expert/09_performance_optimizer/) | App optimization techniques |
| 10 | [Production Deployment](expert/10_production_deployment/) | Deploy to cloud platforms |

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/r14r/Learning_Streamlit_with-Projects.git
cd Learning_Streamlit_with-Projects
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Streamlit:
```bash
pip install streamlit
```

4. Install additional dependencies for specific projects:
```bash
# For data visualization (Advanced/Expert)
pip install plotly pandas numpy

# For machine learning projects (Expert)
pip install scikit-learn

# For API projects
pip install requests

# Or install all at once
pip install streamlit plotly pandas numpy scikit-learn requests
```

### Running an App

Navigate to any project directory and run the Streamlit app:

```bash
cd beginner/01_hello_streamlit
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## 📖 Learning Path

### Recommended Order:

1. **Start with Beginner**: Complete all 10 beginner apps to build a solid foundation
2. **Move to Advanced**: Learn data visualization and external integrations
3. **Challenge with Expert**: Master production-ready Streamlit applications

### How to Use Each Project:

1. **Read the specifications.md** - Understand what the app should do
2. **Study the app.py** - Analyze the implementation
3. **Run the app** - See it in action with `streamlit run app.py`
4. **Modify it** - Experiment with changes
5. **Try the tests** - Verify functionality

## 🎓 What You'll Learn

### Beginner Level
- Basic Streamlit widgets (text_input, button, slider, etc.)
- Layout components (columns, sidebar, containers)
- Session state basics
- File uploaders
- Basic interactivity
- Markdown and text formatting

### Advanced Level
- Data visualization with charts
- Working with DataFrames
- API integration
- File processing (CSV, JSON)
- Advanced session state
- Multi-page applications
- Form handling and validation

### Expert Level
- Caching strategies (@st.cache_data, @st.cache_resource)
- Custom component development
- Database integration
- Authentication and security
- Real-time data updates
- Performance optimization
- Production deployment
- Testing Streamlit apps

## 📝 Documentation Format

Each `specifications.md` includes:

- **Expected Functionality**: What the app does
- **Input**: User interactions and data inputs
- **Expected Output**: What users see and get
- **Tests**: Sample test cases with expected results
- **Dependencies**: Required Python packages
- **Usage**: How to run the app

## 🌟 Streamlit Features Covered

- **Widgets**: text_input, number_input, slider, selectbox, multiselect, checkbox, radio, button, file_uploader, color_picker, date_input, time_input
- **Layouts**: columns, sidebar, expander, tabs, container
- **Display**: text, markdown, code, dataframe, table, metric, json
- **Charts**: line_chart, area_chart, bar_chart, pyplot, plotly_chart, altair_chart
- **Media**: image, audio, video
- **State**: session_state for maintaining state across reruns
- **Caching**: @st.cache_data and @st.cache_resource
- **Navigation**: Multi-page apps
- **Forms**: st.form and form_submit_button

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new projects
- Improve existing code
- Add more test cases
- Enhance documentation

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

Created as a comprehensive learning resource for Streamlit developers at all levels. Inspired by the structure of Learning_Python_with-Projects.

---

**Happy Streamlit Learning! 🎈**