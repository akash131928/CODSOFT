import random
def main():
    # generating random choice for computer
    l=['rock','paper','scissors']
    computer_choice=random.choice(l)

    # user choice
    user_choice=str(input("Enetr your choice (rock/paper/scissors) "))

    if user_choice in l :
        print("")
    else:
        print("invalid choice")
        user_choice=str(input("Enetr your choice (rock/paper/scissors) "))

    # declaring winner
    if(user_choice=='rock' and computer_choice=='rock'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\nits a tie")

    elif(user_choice=='rock' and computer_choice=='paper'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\ncomputer wins")

    elif(user_choice=='rock' and computer_choice=='scissors'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\nYou win")

    elif(user_choice=='paper' and computer_choice=='rock'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\nYou win")

    elif(user_choice=='paper' and computer_choice=='paper'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\nits a tie")

    elif(user_choice=='paper' and computer_choice=='scissors'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\ncomputer wins")

    elif(user_choice=='scissors' and computer_choice=='rock'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\ncomputer wins")

    elif(user_choice=='scissors' and computer_choice=='paper'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\nYou win")

    elif(user_choice=='scissors' and computer_choice=='scissors'):
        print("user choice:",user_choice,"\ncompueter choice:",computer_choice,"\nits a tie")

    # play again
    play_agn=input("\nDo you want to play again? (yes/no) ")

    if (play_agn!="yes"):
        print("\nThanks for playing")

    else:
        main()

main()




