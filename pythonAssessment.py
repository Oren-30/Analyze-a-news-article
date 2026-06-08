import re

def count_specific_word(text, word):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    count = 0

    for w in words:
        if w == word.lower():
            count += 1

    return count


def identify_most_common_word(text):
    if not text.strip():
        return None

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    most_common = None
    max_count = 0

    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            most_common = word

    return most_common


def calculate_average_word_length(text):
    if not text.strip():
        return 0

    words = re.findall(r'\b[a-zA-Z]+\b', text)

    total = 0
    count = 0

    for w in words:
        total += len(w)
        count += 1

    return total / count if count > 0 else 0


def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = text.split("\n\n")

    count = 0
    for p in paragraphs:
        if p.strip():
            count += 1

    return count


def count_sentences(text):
    if not text.strip():
        return 1

    count = 0

    for char in text:
        if char in ".?!":
            count += 1

    return count