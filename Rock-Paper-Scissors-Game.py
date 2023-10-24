import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_rps(num_rounds):
    user_score = 0
    computer_score = 0

    print(f"Welcome to Rock-Paper-Scissors Game! You will play {num_rounds} rounds.")

    for round in range(1, num_rounds + 1):
        print(f"\nRound {round}")
        print("Choose: rock, paper, or scissors (type 'quit' to exit)")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'quit':
            print("Thanks for playing!")
            break

        if user_choice not in ('rock', 'paper', 'scissors'):
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your score: {user_score}  Computer score: {computer_score}")

    print("Final Scores:")
    print(f"Your score: {user_score}  Computer score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        num_rounds = int(input("Enter the number of rounds: "))
        play_rps(num_rounds)
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    num_rounds = int(input("Enter the number of rounds: "))
    play_rps(num_rounds)
