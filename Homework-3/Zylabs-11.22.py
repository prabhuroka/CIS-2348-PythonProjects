# Prabhu Roka
# 1986444
words = input().split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

for word in words:
    print(word, word_freq[word])
