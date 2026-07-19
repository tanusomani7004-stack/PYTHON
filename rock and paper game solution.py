import random

while True:
    a=int(input("enter your choosen number between 1 to 3 here 1 is rock, 2 is paper, 3 is scissor "))
    if a==1:
        print(" you choose rock")
    elif a==2:
        print("you choose paper")
    elif a==3:
        print("you choose scissor")
    else:
        print("choose no between 1 to 3")
        continue
    
    choice= random.randint(1,3)
    if choice==1:
        print(" computer choose rock")
    elif choice==2:
        print("computer choose paper")
    else:
        print("computer choose scissor")
    
    if a==choice:
        print("its a tie")
        continue
    elif a==1 and choice==3 or a==3 and choice==2 or a==2 and choice==1:
        print("you wins")
        break
    else:
        print("computer wins")
        break
