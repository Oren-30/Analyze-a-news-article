import re

def count_specific_word(text, word):
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(word.lower())

def identify_most_common_word(text):
    if not text.strip():
        return None

    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None

    from collections import Counter
    return Counter(words).most_common(1)[0][0]

