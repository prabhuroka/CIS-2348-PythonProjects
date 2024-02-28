# Prabhu Roka
# 1986444
def palindrome(x):
    # Remove spaces and convert to lowercase
    cleaned_word = ''.join(x.split()).lower()

    # Check if the cleaned word is equal to its reverse
    return cleaned_word == cleaned_word[::-1]


if __name__ == '__main__':
    word = input()

    if palindrome(word):
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')
