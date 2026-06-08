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

def calculate_average_word_length(text):
    if not text.strip():
        return 0

    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = re.split(r'\n\s*\n', text.strip())
    paragraphs = [p for p in paragraphs if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    if not text.strip():
        return 1

    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)

