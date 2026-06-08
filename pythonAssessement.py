import re

def count_specific_word(text, word):
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(word.lower())
