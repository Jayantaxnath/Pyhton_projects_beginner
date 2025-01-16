# Project_05
import random

def snake_water_gun():
    print("Welcome to Snake, Water, Gun Game!")
    print("Rules: Snake > Water, Water > Gun, Gun > Snake")
    print("Choose from: Snake (s), Water (w), Gun (g)")

    # Initialize score
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter the number of rounds you want to play: "))

    options = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}

    for _ in range(rounds):
        print("\nRound", _ + 1)
        user_choice = input("Enter your choice (s/w/g): ").lower()

        if user_choice not in options:
            print("Invalid choice! You lose this round.")
            computer_score += 1
            continue

        computer_choice = random.choice(['s', 'w', 'g'])
        print(f"You chose: {options[user_choice]}")
        print(f"Computer chose: {options[computer_choice]}")

        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 's' and computer_choice == 'w') or \
                (user_choice == 'w' and computer_choice == 'g') or \
                (user_choice == 'g' and computer_choice == 's'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    # Final results
    print("\nGame Over!")
    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You are the overall winner! 🎉")
    elif user_score < computer_score:
        print("Computer wins the game! Better luck next time!")
    else:
        print("It's an overall tie!")


# Run the game
snake_water_gun()
