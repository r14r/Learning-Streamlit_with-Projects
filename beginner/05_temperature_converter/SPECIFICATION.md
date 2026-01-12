# Specifications: Temperature Converter

## Expected Functionality

Convert temperatures between Celsius, Fahrenheit, and Kelvin.

## Input

- Temperature value (number input)
- Source unit (Celsius, Fahrenheit, or Kelvin)
- Target unit (Celsius, Fahrenheit, or Kelvin)

## Expected Output

- Converted temperature value
- Conversion formula used

## Tests

### Test 1: Celsius to Fahrenheit
- **Input**: 0°C to Fahrenheit
- **Expected Output**: 32°F

### Test 2: Fahrenheit to Celsius
- **Input**: 212°F to Celsius
- **Expected Output**: 100°C

## Dependencies

```txt
streamlit>=1.28.0
```

## Usage

```bash
streamlit run app.py
```
