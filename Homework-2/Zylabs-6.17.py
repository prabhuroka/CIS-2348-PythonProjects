# Prabhu Roka
# 1986444
new_word = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}
passwd = input()
strong_password = ''.join(new_word.get(char, char) for char in passwd)
strong_password += 'q*s'
print(strong_password)
