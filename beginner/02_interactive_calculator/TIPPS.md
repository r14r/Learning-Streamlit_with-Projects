# Interactive Calculator - Tips & Code Sketches

## Step 1: Basic Setup

**Key Concept**: Set up the calculator with appropriate theme and layout.

```python
import streamlit as st

st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Interactive Calculator")
st.write("Perform basic arithmetic operations with ease!")
```

---

## Step 2: Number Inputs

**Key Concept**: `number_input()` creates a numeric input field with validation.

```python
num1 = st.number_input(
    "Enter first number",
    value=0.0,        # Default value
    format="%.2f"     # Display with 2 decimal places
)
```

**Tip**: The `format` parameter controls how the number is displayed (e.g., `%.2f` for 2 decimals).

---

## Step 3: Columns for Layout

**Key Concept**: Use columns to arrange widgets side by side.

```python
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First number", value=0.0)

with col2:
    num2 = st.number_input("Second number", value=0.0)
```

**Tip**: The `with` statement makes it clear which widgets belong to which column.

---

## Step 4: Operation Selection

**Key Concept**: `selectbox()` creates a dropdown menu for user selection.

```python
operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)
```

**Tip**: Make option labels user-friendly by including symbols.

---

## Step 5: Button and Calculation Logic

**Key Concept**: Buttons trigger actions when clicked; use if/elif for different operations.

```python
if st.button("Calculate", type="primary"):
    result = None

    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        result = num1 / num2

    if result is not None:
        st.success(f"Result: {result:.2f}")
```

**Tip**: `type="primary"` makes the button stand out with accent color.

---

## Step 6: Error Handling

**Key Concept**: Always check for errors before performing operations.

```python
if operation == "Division (÷)":
    if num2 == 0:
        st.error("⚠️ Cannot divide by zero!")
    else:
        result = num1 / num2
```

**Tip**: Use `st.error()` for error messages - it displays in red to grab attention.

---

## Step 7: Expandable Details

**Key Concept**: Expanders hide content by default, keeping the UI clean.

```python
with st.expander("ℹ️ Calculation Details"):
    st.write(f"- First Number: {num1}")
    st.write(f"- Second Number: {num2}")
    st.write(f"- Operation: {operation}")
    st.write(f"- Result: {result:.2f}")
```

**Tip**: Use expanders for optional or detailed information that might clutter the main view.

---

## Best Practices

1. **Input Validation**: Always validate user inputs before calculations
2. **Clear Feedback**: Use success/error messages to confirm actions
3. **Layout Organization**: Use columns for better visual hierarchy
4. **Error Handling**: Check for edge cases (like division by zero)
5. **User Experience**: Make button labels clear and use appropriate colors
6. **Number Formatting**: Format numbers consistently (e.g., 2 decimal places)
