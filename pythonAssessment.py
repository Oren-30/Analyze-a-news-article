def count_specific_word(text, word):
    words = text.lower().split()
    target = word.lower()

    count = 0
    for w in words:
        if w == target:
            count += 1
    return count


def identify_most_common_word(text):
    if not text.strip():
        return None

    words = text.lower().split()

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

    words = text.split()

    total = 0
    count = 0

    for w in words:
        total += len(w)
        count += 1

    if count == 0:
        return 0

    return total / count


def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = text.split("\n\n")

    count = 0
    i = 0

    while i < len(paragraphs):
        if paragraphs[i].strip():
            count += 1
        i += 1

    return count


def count_sentences(text):
    if not text.strip():
        return 1

    sentences = text.split(".")

    count = 0
    for s in sentences:
        if s.strip():
            count += 1

    return count