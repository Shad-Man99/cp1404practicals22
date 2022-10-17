"""
Word Occurrences
Estimate: 45 minutes
Actual:   75 minutes
"""

words = input(str("Text: ")).split(' ')
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
words = list(word_to_count.keys())
words.sort()
longest_length = 0
for key in word_to_count.keys():
    if len(key) > longest_length:
        longest_length = len(key)
highest_count = 0
for word in words:
    print(f"{word:{longest_length}} : {word_to_count[word]}")
