print("Please think of a number between 0 and 100!")
guess = 100
while True:
    print("Is your secret number " + str(guess))
    print("""Enter 'h' to indicate the guess is too high. 
Enter 'l' to indicate the guess is too low. 
Enter 'c' to indicate I guessed correctly.\n""")
    inp = input()
    if inp == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    elif inp == "h":
        guess -= guess//2
    elif inp == "l":
        guess += guess//2
    else:
        print("Sorry, I did not understand your input.")




