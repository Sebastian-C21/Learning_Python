user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    #print(letter)
    if(letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U"):
        continue
    else:
        print(letter)

