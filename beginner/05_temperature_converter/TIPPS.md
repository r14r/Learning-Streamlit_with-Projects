# Temperature Converter - Tips & Code Sketches

## Step 1: Basic Temperature Input

**Key Concept**: Number inputs can be configured with default values and formatting.

```python
temperature = st.number_input(
    "Enter temperature:",
    value=0.0,      # Default value
    format="%.2f"   # 2 decimal places
)
```

**Tip**: The `format` parameter uses printf-style formatting.

---

## Step 2: Unit Selection

**Key Concept**: Provide clear options for temperature units.

```python
from_unit = st.selectbox(
    "From:",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

to_unit = st.selectbox(
    "To:",
    ["Celsius", "Fahrenheit", "Kelvin"]
)
```

**Tip**: Keep unit names consistent and user-friendly.

---

## Step 3: Column Layout

**Key Concept**: Organize related inputs in columns.

```python
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("Temperature:", value=0.0)
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])

with col2:
    # Add spacing to align with left column
    st.write("")
    st.write("")
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
```

**Tip**: Use empty `st.write()` calls to add vertical spacing.

---

## Step 4: Conversion Functions

**Key Concept**: Create separate functions for each conversion type.

```python
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin"""
    return c + 273.15

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    """Convert Fahrenheit to Kelvin"""
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius"""
    return k - 273.15

def kelvin_to_fahrenheit(k):
    """Convert Kelvin to Fahrenheit"""
    return (k - 273.15) * 9/5 + 32
```

**Tip**: Use descriptive function names and add docstrings.

---

## Step 5: Conversion Logic

**Key Concept**: Handle all possible conversion combinations.

```python
if st.button("Convert", type="primary"):
    result = None

    # Check if same unit
    if from_unit == to_unit:
        result = temperature
        st.info(f"Same unit selected: {temperature:.2f}°")
    else:
        # Celsius conversions
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(temperature)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = celsius_to_kelvin(temperature)

        # Fahrenheit conversions
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = fahrenheit_to_celsius(temperature)
        # ... (add all other combinations)

    if result is not None:
        # Handle degree symbol (Kelvin doesn't use it)
        unit_symbol = "°" if to_unit != "Kelvin" else ""
        st.success(f"{temperature:.2f}°{from_unit[0]} = {result:.2f}{unit_symbol}{to_unit[0]}")
```

**Tip**: Use the first letter of unit names for compact display (C, F, K).

---

## Step 6: Formulas and References

**Key Concept**: Provide educational information to users.

```python
# Show formula used
formula = "°F = (°C × 9/5) + 32"
st.info(f"**Formula**: {formula}")

# Reference table in expander
with st.expander("📖 Reference Table"):
    st.write("**Common Temperatures:**")
    st.write("- Water freezes: 0°C = 32°F = 273.15K")
    st.write("- Water boils: 100°C = 212°F = 373.15K")
    st.write("- Room temperature: 20°C = 68°F = 293.15K")
    st.write("- Body temperature: 37°C = 98.6°F = 310.15K")
```

**Tip**: Reference tables help users verify results and learn.

---

## Temperature Conversion Formulas

```python
# Celsius to others
F = (C × 9/5) + 32
K = C + 273.15

# Fahrenheit to others
C = (F - 32) × 5/9
K = (F - 32) × 5/9 + 273.15

# Kelvin to others
C = K - 273.15
F = (K - 273.15) × 9/5 + 32
```

---

## Best Practices

1. **Function Organization**: One function per conversion type
2. **Edge Cases**: Handle same-unit selection gracefully
3. **Symbol Handling**: Remember Kelvin doesn't use degree symbol
4. **Formula Display**: Show the formula used for transparency
5. **Number Formatting**: Consistent decimal places for all outputs
6. **Reference Data**: Provide common conversions for verification
7. **Clear Labels**: Use full unit names in UI, abbreviations in formulas
