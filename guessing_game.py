import random
attemps_list=[]
attempts=0

pc_guess=random.randint(1,10)

print("Hello playing guessing game")
player_name=input("Enter your name: ")
wann_play=input(f"Do you want to start playing {player_name} enter Yes/No ?").lower()
if wann_play=='no':
    if not attemps_list:
        print("There's no high score")
        exit()
    else:
        print(f"Your high score {min(attemps_list)}")
while wann_play=='yes':
    try:
        player_guess=int(input("Enter Your guessing number from 1 to 10: "))
        if player_guess<1 or player_guess>10:
            raise ValueError("Please pick a number in rang from 1 to 10")
        attempts+=1
        attemps_list.append(attempts)
        if player_guess==pc_guess:
            print("You got it")
            print(f"Your attemps is {attempts}")
            wann_play=input("Do You want to play again Yes/No?  ").lower()
            if wann_play=='no':
                print("Good Bye see you again")
            else:
                attempts=0
                pc_guess=random.randint(1,10)
                continue
        if player_guess<pc_guess:
            print("It is lower than pc guess")
        elif player_guess>pc_guess:
            print("It is higher than pc guess")
    except ValueError as err:
        print(err)
