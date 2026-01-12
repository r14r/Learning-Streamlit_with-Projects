# Specifications: Interactive Calculator

## Expected Functionality

A simple calculator app that performs basic arithmetic operations:
- Addition, subtraction, multiplication, and division
- User inputs two numbers
- User selects an operation
- App displays the result

## Input

- **Number 1**: Float number (via number_input)
- **Number 2**: Float number (via number_input)
- **Operation**: Select from addition (+), subtraction (-), multiplication (×), division (÷)

## Expected Output

- Display the calculation formula
- Show the result of the operation
- Handle division by zero with an error message

## Tests

### Test 1: Addition
- **Input**: Number 1 = 10, Number 2 = 5, Operation = Addition
- **Expected Output**: "10.0 + 5.0 = 15.0"

### Test 2: Division
- **Input**: Number 1 = 20, Number 2 = 4, Operation = Division
- **Expected Output**: "20.0 ÷ 4.0 = 5.0"

### Test 3: Division by Zero
- **Input**: Number 1 = 10, Number 2 = 0, Operation = Division
- **Expected Output**: Error message "Cannot divide by zero!"

## Dependencies

```txt
streamlit>=1.28.0
```

## Usage

```bash
streamlit run app.py
```
