# Guessing Number Game

Welcome to the Guessing Number Game! This is a simple Python console-based game where the player tries to guess a randomly generated number between 1 and 10.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Clone the Repository

```bash
git clone https://github.com/naglaamossleh2016/guessing_game.git


Certainly! Here's a simple example of a Python program for a guessing number game between 1 and 10, along with an updated README.md:

guessing_game.py:

python
Copy code
import random

def guess_number():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Set the number of attempts
    max_attempts = 3
    
    print("Welcome to the Guessing Number Game!")
    print(f"Guess the number between 1 and 10. You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        try:
            # Get user input for the guess
            guess = int(input("Enter your guess: "))
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempt} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_number()
README.md:

markdown
Copy code
# Guessing Number Game

Welcome to the Guessing Number Game! This is a simple Python console-based game where the player tries to guess a randomly generated number between 1 and 10.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Clone the Repository

```bash
git clone https://github.com/your-username/guessing-number-game.git

### How to Play
<ul><li>The game will generate a random number between 1 and 10.</li>
<li>You need to guess the number.<li>
<li>After each guess, the game will provide feedback (too high, too low, or correct).</li>
<li>Keep guessing until you find the correct number or run out of attempts.</li></ul>
### Features
Randomly generated number between 1 and 10.
User input validation.
Feedback on each guess.
Limit on the number of attempts.
Contributing
Contributions are welcome! If you find any issues or want to enhance the game, feel free to open a pull request.
