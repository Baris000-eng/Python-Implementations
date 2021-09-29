import time
import random

print("Hangman game!")
print()
time.sleep(2)
print("Start to guess ! ")
time.sleep(1)
random_word_list= ["apple","banana","orange","chicken"]
selected_word= random.choice(random_word_list)
guesses = ''
charCount= 0
for i in selected_word:
  charCount=charCount+1
numberOfTries= charCount
while numberOfTries> 0:
    failed = 0
    for i in range(0,len(selected_word)):
        if selected_word[i] in guesses:
            print(selected_word[i]),
        else:
            print("_"),
            failed += 1
    if failed == 0:
        print()
        print("You won")
        break
    print()
    guess = input("Enter your guess char: ")
    guesses += guess
    if guess not in selected_word:
        numberOfTries -= 1
        print("Wrong")
    print("You have", + numberOfTries, 'more guesses')
    if numberOfTries == 0:
        print("You Lose")