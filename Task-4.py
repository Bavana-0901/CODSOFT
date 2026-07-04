import random

print("===================================")
print("   ROCK PAPER SCISSORS GAME")
print("===================================")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print()

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYour Choice     : {user_choice.capitalize()}")
    print(f"Computer Choice : {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        print("Result: It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nScore Board")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Scores")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")
        print("Thanks for playing!")
        break

    print()