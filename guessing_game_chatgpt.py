import random

def display_high_score(attempts_list):
    if not attempts_list:
        print("There's no high score")
    else:
        print(f"Your high score: {min(attempts_list)}")

def play_guessing_game():
    attempts_list = []
    pc_guess = random.randint(1, 10)

    print("Hello! Welcome to the guessing game")
    player_name = input("Enter your name: ")

    while True:
        wann_play = input(f"Do you want to start playing, {player_name}? Enter Yes/No: ").lower()

        if wann_play == 'no':
            display_high_score(attempts_list)
            exit()

        elif wann_play == 'yes':
            attempts = 0

            while True:
                try:
                    player_guess = int(input("Enter your guess (1-10): "))

                    if player_guess < 1 or player_guess > 10:
                        raise ValueError("Please pick a number in the range from 1 to 10")

                    attempts += 1
                    attempts_list.append(attempts)

                    if player_guess == pc_guess:
                        print("You got it!")
                        print(f"Your attempts: {attempts}")

                        play_again = input("Do you want to play again? Yes/No: ").lower()
                        if play_again == 'no':
                            print("Goodbye! See you again.")
                            exit()
                        else:
                            attempts = 0
                            pc_guess = random.randint(1, 10)
                            break

                    elif player_guess < pc_guess:
                        print("It is lower than the PC guess")

                    elif player_guess > pc_guess:
                        print("It is higher than the PC guess")

                except ValueError as err:
                    print(err)

if __name__ == "__main__":
    play_guessing_game()
