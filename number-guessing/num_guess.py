import random

def guessNum(num):
    #Here we need to guess the random number
    random_number=random.randint(1,num)#return a random int N such that a<=N<=b. Alias for randrange(a,b+1)
    guess=0
    c=1
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {num} "))
        if guess <random_number:
            print("Sorry, wrong guess. Try again. Hint:Too Low")
            c+=1
        elif guess>random_number:
            print("Sorry, wrong guess. Try again. Hint: Too High")
            c+=1
    print(f"Congratulations. You have guessed the number at {c}th time.")

def computer_guess(num):
    #Here computer will guess the number selected by us
    low=1
    high=num
    feedback=""
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low #could also be high b/c low==high
        feedback=input(f"Is {guess} too high(H), too low(L) or correct(C)? ")
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
    print(f"The Computer guessed your number({guess}) correctly.")

guessNum(100)
print("Now, you select a sectret number and let the computer guess it.")
computer_guess(100)
