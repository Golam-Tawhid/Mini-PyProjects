import random

def play():
    user=input("What's your choice? 'r' for rock, 'p' for paper and 's' for scissors.\n")
    computer=random.choice(['r','p','s'])#it will choose a random element from the given list

    if user==computer:
        return "It's a Tie"

#r>s, s>p, p>r
    if is_win(user,computer):
        return'You won!'
    
    return "You Lost!"


def is_win(player,opponent):
    #return true if player wins
    #r>s, s>p, p>r
    if (player=='r' and opponent=='s') or (player=='s'and opponent=='p') or (player=='p' and opponent=='r'):
        return True


a=input("Press any key to continue and press 'q' to quit.")
while a!='q':
    print(play())
    a=input("Press any key to continue and press 'q' to quit.")