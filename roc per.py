import random
def call():
    word="rock paper scissor"
    computerChoice=word.split()
    a=random.choice(computerChoice)
    b=str(input("enter your choice :"))
    print()
    print("computer choice is:",a)
    print()
    if(a==b):
        print("match draw play again")
        call()
    else:
        if(a=="rock"):
            if(b=="paper"):
                print("You win")
            else:
                print("You loose")
        elif(a=="paper"):
            if(b=="scissor"):
                print("You win")
            else:
                print("You loose")
        elif(a=="scissor"):
            if(b=="rock"):
                print("You win")
            else:
                print("You loose")
call()