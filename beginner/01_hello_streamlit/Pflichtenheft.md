# Pflichtenheft: Hello Streamlit

## Expected Functionality

A basic Streamlit application that demonstrates fundamental text display features including:
- Display a welcome message
- Show formatted markdown text
- Display code snippets
- Use different text formatting options (title, header, subheader)
- Show an informational message

## Input

No user input required. This is a static display app.

## Expected Output

The app should display:
1. A title: "Hello Streamlit!"
2. A welcome message with formatted text
3. A code snippet showing a simple Python function
4. Various text formatting examples
5. An info box with getting started information

## Tests

### Test 1: App Loads Successfully
- **Action**: Run `streamlit run app.py`
- **Expected**: App opens in browser without errors
- **Result**: Page displays with title "Hello Streamlit!"

### Test 2: Text Formatting
- **Action**: View the page
- **Expected**: Different heading levels are visible
- **Result**: Title, headers, and subheaders are properly displayed with different sizes

### Test 3: Code Display
- **Action**: View the code snippet section
- **Expected**: Python code is displayed with syntax highlighting
- **Result**: Code block shows with proper formatting

## Dependencies

```txt
streamlit>=1.28.0
```

## Usage

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`
