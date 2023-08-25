while True:
    
    guesses = 6
    word = "fart"
    win = False
    
    length = len(word)
    
    print("Welcome to Hangman")
    print("You have " + str(guesses) + " guesses")
    
    #word_guess is a list the length of the word, with each letter as an underscore
    
    word_guess = []
    wrong_guess = []
    
    for i in range(length):
        word_guess.append("_")
    
    for i in range(length):
        print("_", end=" ")
        

    print("\n")

    while guesses > 0:
        
        #check to see if all letters have been guessed
        if "_" not in word_guess:
            win = True
            break
        
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
    
    print("Game Over")
    if win == False:
        print("The word was " + word)
        
    else:
        print("You win!")
    break