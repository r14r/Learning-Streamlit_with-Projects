# Data Display - Tips & Code Sketches

## Step 1: Creating DataFrames

**Key Concept**: DataFrames are created from dictionaries where keys become column names.

```python
import pandas as pd

# Dictionary to DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'London']
}

df = pd.DataFrame(data)
st.write(df)  # Simple display
```

**Tip**: Each dictionary key becomes a column, and lists become the rows.

---

## Step 2: DataFrame Statistics

**Key Concept**: Extract useful statistics directly from DataFrame columns.

```python
# Count rows
total = len(df)

# Calculate column averages
avg_age = df['Age'].mean()

# Count unique values
unique_cities = df['City'].nunique()

# Display as metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Records", total)
with col2:
    st.metric("Average Age", f"{avg_age:.1f}")
with col3:
    st.metric("Unique Cities", unique_cities)
```

**Tip**: Use `.mean()`, `.sum()`, `.nunique()` for common statistics.

---

## Step 3: Display Methods Comparison

**Key Concept**: Choose the right display method for your use case.

```python
# Interactive table - scrollable, sortable, searchable
st.dataframe(df, use_container_width=True)

# Static table - simple HTML table
st.table(df.head(3))  # Show first 3 rows
```

**Tip**: Use `st.dataframe()` for large datasets, `st.table()` for small, formatted displays.

---

## Step 4: Column Filtering

**Key Concept**: `multiselect()` allows users to choose multiple items from a list.

```python
# Get all column names
columns = df.columns.tolist()

# Let user select columns
selected = st.multiselect(
    "Select columns to display:",
    columns,
    default=['Name', 'Age']  # Pre-selected columns
)

# Display only selected columns
if selected:
    st.dataframe(df[selected], use_container_width=True)
```

**Tip**: Always provide sensible defaults for better UX.

---

## Step 5: JSON Display with Toggle

**Key Concept**: Checkboxes return True/False for conditional display.

```python
if st.checkbox("Show data as JSON"):
    # Convert DataFrame to JSON format
    json_data = df.to_dict(orient='records')
    st.json(json_data)
```

**Tip**: `orient='records'` creates a list of dictionaries (one per row).

---

## Step 6: Statistics and Editing

**Key Concept**: `describe()` provides statistical summary; `data_editor()` allows editing.

```python
# Show statistics in expander
with st.expander("📊 Data Statistics"):
    st.write(df.describe())  # Statistical summary

# Editable table
st.subheader("✏️ Editable Data")
edited_df = st.data_editor(df, use_container_width=True)

# Detect changes
if not df.equals(edited_df):
    st.info("You've made changes!")
```

**Tip**: `describe()` works best with numeric columns.

---

## DataFrame Methods Reference

```python
# Common DataFrame operations
df.head(n)          # First n rows
df.tail(n)          # Last n rows
df.shape            # (rows, columns)
df.columns          # Column names
df.dtypes           # Data types
df['col'].mean()    # Average of column
df['col'].sum()     # Sum of column
df['col'].min()     # Minimum value
df['col'].max()     # Maximum value
df['col'].nunique() # Count unique values
df.describe()       # Statistical summary
df.to_dict()        # Convert to dictionary
```

---

## Best Practices

1. **Use Container Width**: `use_container_width=True` makes tables responsive
2. **Choose Correct Display**: Interactive for large data, static for small summaries
3. **Provide Defaults**: Always set sensible default selections
4. **Format Numbers**: Use f-strings for clean number formatting
5. **Organize Info**: Use expanders for detailed or optional information
6. **Column Names**: Use clear, descriptive column names in your data
7. **Data Validation**: Check if DataFrame is empty before operations