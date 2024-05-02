def rock_paper_scissors_game():
    import random
    start_game = input('Welcome to the rock-paper-scissors game!\n')
    user_choice = input('Please choose rock, paper, or scissors: ')

    while True:
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win! Rock smashes scissors.")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win! Paper covers rock.")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win! Scissors cut paper.")
        else:
            print("You lose! Computer wins.")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break  # Exit the game loop if the user doesn't want to play again
        else:
            user_choice = input('Please choose rock, paper, or scissors: ')

rock_paper_scissors_game()