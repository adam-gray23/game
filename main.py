import time
import os
import random
from holder import HANGMANPICS

def game(length, word_guess, wrong_guess, word):
    guesses = 6
    win = False
    
    while guesses > 0:

        #check to see if all letters have been guessed
        if "_" not in word_guess:
            win = True
            break
        
        print(HANGMANPICS[6-guesses] + "\n")
        
        guess = str(input("Make a guess: "))
        guess_len = len(guess)
        if guess_len > 1:
            print("You can only guess one letter at a time")
            continue
        if guess in word:
            if guess in word_guess:
                print("You already guessed that")
                continue
            print("Correct")
            
            #add the letters to word_guess in order they appear, but not change the existing letters
            for i in range(length):
                if guess == word[i]:
                    word_guess[i] = guess
            #print word_guess as a string
            print(" ".join(word_guess))
        else:
            if guess in wrong_guess:
                print("You already guessed that")
                continue
            guesses -= 1
            wrong_guess.append(guess)
            print("Incorrect")
            print("You have " + str(guesses) + " guesses left")
            #print the current guess
            print(" ".join(word_guess))
    
    game_over(win, word)

def game_over(win, word):
    print("Game Over")
    if win == False:
        print("The word was " + word)
        
    else:
        print("You win!")


def set_up(word):
    length = len(word)
    word_guess = []
    wrong_guess = []
    for i in range(length):
        word_guess.append("_")
    for i in range(length):
        print("_", end=" ")
        
    print("\n")
    
    game(length, word_guess, wrong_guess, word)

def choose_word():
    #read file, store words in list, choose random word
    l = []
    with open("words.txt", "r") as f:
        for line in f:
            l.append(line.strip())
    
    word = random.choice(l)
    return word

def welcome():
    
    
    os.system('cls')
    print("Welcome to Hangman")
    print("Please wait while your word is chosen...")
    time.sleep(2)
    os.system('cls')
    
    word = choose_word()
    
    print("Your word has been chosen")
    print("You have 6 guesses")
    
    set_up(word)

def loop():
    while True:
        welcome()
        break

def main():
    loop()


if __name__ == '__main__':
    main()