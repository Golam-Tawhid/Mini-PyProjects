import random

def guessNum(num):
    random_number=random.randint(1,num)#return a random int N such that a<=N<=b. Alias for randrange(a,b+1)
    guess=0
    c=1
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {num}  "))
        if guess <random_number:
            print("Sorry, wrong guess. Try again. Hint:Too Low")
            c+=1
        elif guess>random_number:
            print("Sorry, wrong guess. Try again. Hint: Too High")
            c+=1
    print(f"Congratulations. You have guessed the number at {c}th time.")

guessNum(100)
