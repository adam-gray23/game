while True:
    
    guesses = 6
    word = "fart"
    
    length = len(word)
    
    print("Welcome to Hangman")
    print("You have " + str(guesses) + " guesses")
    
    #word_guess is a list the length of the word, with each letter as an underscore
    
    word_guess = []
    
    for i in range(length):
        word_guess.append("_")
    
    for i in range(length):
        print("_", end=" ")
        

    print("\n")

    while guesses > 0:
        guess = str(input("Make a guess: "))
        if guess in word:
            print("Correct")
            
            #add the letters to word_guess in order they appear, but not change the existing letters
            for i in range(length):
                if guess == word[i]:
                    word_guess[i] = guess
            #print word_guess as a string
            print(" ".join(word_guess))
        else:
            guesses -= 1
            print("Incorrect")
            print("You have " + str(guesses) + " guesses left")
    
    print("Game Over")
    break