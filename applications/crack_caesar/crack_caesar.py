# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open("ciphertext.txt") as f:
    words = f.read()
dct = {}
frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W',
             'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
cipher = {}
total = 0
sentence = ''
for word in words.split():
    for letter in word:
        if letter.isupper() and letter.isalpha():
            total += 1
        if letter not in dct and letter.isupper() and letter.isalpha():
            dct[letter] = 1
        else:
            if letter.isalpha() and letter.isupper():
                dct[letter] += 1
for pair in dct.items():
    cipher[pair[0]] = pair[1] / total * 100

sorted_set = sorted(cipher.items(), key=lambda x: x[1], reverse=True)

cipher = dict(sorted_set)

counter = 0

for key in cipher:
    cipher[key] = frequency[counter]
    counter += 1


for word in words.split():
    new_word = ''
    for letter in word:
        if letter in cipher:
            new_word += cipher[letter]
        else:
            new_word += letter
    sentence += new_word + " "
print(sentence)
