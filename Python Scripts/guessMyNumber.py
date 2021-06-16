print("Please think of a number between 0 and 100!")
guess = 100
low = 1
high = guess
ans = (high + low)//2
while True:
    print("Is your secret number " + str(ans))
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if inp == "c":
        print("Game over. Your secret number was: " + str(ans))
        break
    elif inp == "h":
        high = ans
    elif inp == "l":
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    ans = (high + low)//2




