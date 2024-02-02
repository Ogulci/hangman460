import random

word_list=['Banana', 'Pineapple', 'Blueberry','Strawberry','Mango']

print(word_list)

word= random.choice(word_list)
print(word)

while True:
    guess= input("Please enter a single letter:   ")

    if len(guess)==1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Oops! That is not a valid input.") 