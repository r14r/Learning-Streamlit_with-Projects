# Specifications: Text Analyzer

## Expected Functionality

Analyze text input and provide statistics:
- Count total characters
- Count words
- Count sentences
- Count vowels and consonants
- Show character frequency

## Input

- Multi-line text input from user

## Expected Output

- Character count (with and without spaces)
- Word count
- Sentence count
- Vowel and consonant count
- Most frequent characters

## Tests

### Test 1: Simple Text
- **Input**: "Hello World"
- **Expected Output**: 11 chars (10 without spaces), 2 words, 1 sentence, 3 vowels, 7 consonants

### Test 2: Multi-sentence Text
- **Input**: "Hello. How are you? I am fine."
- **Expected Output**: Multiple sentences detected

## Dependencies

```txt
streamlit>=1.28.0
```

## Usage

```bash
streamlit run app.py
```
