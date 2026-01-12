# Text Analyzer - Tips & Code Sketches

## Step 1: Text Area Input

**Key Concept**: `text_area()` provides a multi-line text input field.

```python
text = st.text_area(
    "Enter your text here:",
    height=200,                          # Height in pixels
    placeholder="Type or paste text..."  # Hint text
)

if text:
    # Process text
else:
    st.info("👆 Enter some text to analyze")
```

**Tip**: Always check if text exists before processing to avoid errors.

---

## Step 2: Basic String Statistics

**Key Concept**: Python string methods make text analysis easy.

```python
# Total characters including spaces
char_count = len(text)

# Characters without spaces or newlines
char_no_spaces = len(text.replace(" ", "").replace("\n", ""))

# Word count
word_count = len(text.split())
```

**Tip**: `split()` divides text by whitespace and returns a list of words.

---

## Step 3: Advanced Text Analysis

**Key Concept**: Use list comprehensions for efficient filtering and counting.

```python
# Count sentences (simple method)
sentence_count = text.count('.') + text.count('!') + text.count('?')

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

# Count consonants
consonants = sum(1 for char in text if char.isalpha() and char not in vowels)
```

**Tip**: `sum()` with a generator expression is memory-efficient for counting.

---

## Step 4: Metric Display

**Key Concept**: `st.metric()` creates professional-looking statistics cards.

```python
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Characters", char_count)
    st.caption(f"Without spaces: {char_no_spaces}")

with col2:
    st.metric("Words", word_count)
```

**Tip**: Use `st.caption()` under metrics for additional context or details.

---

## Step 5: Character Frequency with Counter

**Key Concept**: `Counter` from collections module counts item occurrences.

```python
from collections import Counter

# Filter to letters only and convert to lowercase
letters_only = [char.lower() for char in text if char.isalpha()]

# Count frequency
freq = Counter(letters_only)

# Get most common
most_common = freq.most_common(10)  # Top 10

for char, count in most_common:
    st.write(f"- **{char}**: {count}")
```

**Tip**: List comprehensions can filter and transform data in one line.

---

## Step 6: Data Visualization

**Key Concept**: Convert data to DataFrame for easy charting.

```python
import pandas as pd

# Create DataFrame from frequency data
df = pd.DataFrame(most_common, columns=['Character', 'Frequency'])

# Display as bar chart
st.bar_chart(df.set_index('Character'))
```

**Tip**: `set_index()` makes the character column the x-axis labels.

---

## Step 7: Calculated Statistics

**Key Concept**: Derive meaningful insights from basic statistics.

```python
with st.expander("📊 Detailed Statistics"):
    # Average word length
    avg_word_len = char_no_spaces / max(word_count, 1)
    st.write(f"Average word length: {avg_word_len:.2f} characters")

    # Average sentence length
    avg_sentence_len = word_count / max(sentence_count, 1)
    st.write(f"Average sentence length: {avg_sentence_len:.2f} words")

    # More stats
    st.write(f"Uppercase: {sum(1 for c in text if c.isupper())}")
    st.write(f"Lowercase: {sum(1 for c in text if c.islower())}")
    st.write(f"Digits: {sum(1 for c in text if c.isdigit())}")
```

**Tip**: Use `max(count, 1)` to avoid division by zero errors.

---

## Best Practices

1. **Input Validation**: Always check if text exists before processing
2. **Efficient Counting**: Use generator expressions with `sum()` for counting
3. **Data Structures**: Use Counter for frequency analysis
4. **Visual Organization**: Group related metrics in columns
5. **User Guidance**: Provide clear instructions and placeholder text
6. **Edge Cases**: Handle division by zero and empty inputs
7. **Formatting**: Use f-strings and format specifiers for clean output
