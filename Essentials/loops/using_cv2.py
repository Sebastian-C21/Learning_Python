word_w_v = ""

word =  input("Tap any word: ")
word =  word.upper()

for letter in word:
    if(letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U"):
        continue
    else:
        word_w_v += letter
print(word_w_v)

