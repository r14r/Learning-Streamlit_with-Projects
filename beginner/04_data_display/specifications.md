# Specifications: Data Display

## Expected Functionality

Display data in various formats using Streamlit:
- Show sample data in a DataFrame
- Display data as a table
- Show metrics with delta values
- Display JSON data

## Input

No user input required. Uses sample data.

## Expected Output

- DataFrame with sample user data
- Styled table display
- Metric cards showing statistics
- JSON data display

## Tests

### Test 1: DataFrame Display
- **Action**: Run app
- **Expected Output**: DataFrame with 5 sample users displayed

### Test 2: Metrics Display
- **Action**: View metrics section
- **Expected Output**: Cards showing total users, average age, etc.

## Dependencies

```txt
streamlit>=1.28.0
pandas>=1.5.0
```

## Usage

```bash
streamlit run app.py
```
