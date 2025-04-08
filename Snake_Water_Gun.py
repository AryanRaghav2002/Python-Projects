import random
'''
-1 for Snake
0 for water
1 for Gun
'''
def Enter_Game():
    computer=random.choice([0,-1,1])
    you=int(input('''   Choose amongst:
                -1 for snake
                0 for water
                1 for gun
            Enter your choice: '''))
    choice_dict={-1:"Snake" , 0:"Water" , 1:"Gun" }

    print(f"You chose {choice_dict[you]} and Computer chose {choice_dict[computer]}")
    if(computer==you):
        print("It is a draw!")
    else:
        if(computer==0 and you==-1):
            print("You win!")
        elif(computer==-1 and you==0):
            print("Computer wins!")
        elif(computer==0 and you==1):
            print("Computer wins!")
        elif(computer==1 and you==0):
            print("You win!")
        elif(computer==1 and you==-1):
            print("Computer wins!")
        elif(computer==-1 and you==1):
            print("You win!")

        else:
            print("Something went wrong!")
    



Choice=input('''Do you want to enter the game of Snake water Gun? 
        Yes or No
Enter your choice: ''')

if Choice=="Yes" or Choice=="yes":
    print("             The Game is started!")
    Enter_Game()
elif Choice=="No" or Choice=="no":
    print("             The game is exited!")
else:
    print(f"Please select {"Yes"} or {"No"}")
