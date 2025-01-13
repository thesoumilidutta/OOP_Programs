from random import randint

dic={'r':1,'p':2,'s':3}

rounds=7
user_wins,comp_wins=0,0
while (user_wins<4 and comp_wins<4) and rounds!=0:
    userInput=-1

    randomInput=randint(1,3)
    while userInput not in dic:
        userInput=input("Enter your choice Rock(r)/Paper(p)/Scissors(s)").lower()
    if randomInput==userInput:
        print("tie")
        continue
    elif randomInput==1:
        if dic[userInput]==2:
            print("You win!")
            user_wins+=1
        else:
            print("Computer wins")
            comp_wins+=1
    elif randomInput==2:
        if dic[userInput]==1:
            print("Computer wins")
            comp_wins+=1
        else:
            print("You win!")
            user_wins+=1
    else:
        if dic[userInput]==1:
            print("You win!")
            user_wins+=1
        else:
            print("Computer wins")
            comp_wins+=1
       
    rounds-=1

if user_wins>comp_wins:
    print("Hurray! You win the game.")
else:
    print("Uh oh , computer wins the game. Better luck next time.")
    