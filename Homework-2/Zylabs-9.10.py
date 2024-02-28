# Prabhu Roka
# 1986444
import csv


def word_freq(file_name):
    frequencies = {}

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                cleaned_word = word.strip()
                frequencies[cleaned_word] = frequencies.get(cleaned_word, 0) + 1
    return frequencies


if __name__ == '__main__':
    file_name = input()
    word_freq = word_freq(file_name)
    for word, count in word_freq.items():
        print(f'{word} {count}')
