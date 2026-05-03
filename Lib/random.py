"""Random variable generators.
import random

# 1. Function to print welcome message and instructions
def print_welcome():
    print("--- Welcome to the Game of Pig! ---")
    print("Instructions:")
    print("Each round, you and the computer roll a die.")
    print("If you roll a 2-6, it's added to your score.")
    print("If you roll a 1, your total score resets to 0.")
    print("First to reach 40 points wins!")
    print("-----------------------------------")

# 2. Function to check the dice roll and update score
def check_dice(current_total, dice_roll):
    if dice_roll == 1:
        return 0  # Score resets to 0
    else:
        return current_total + dice_roll

# 3. Function to display the scoreboard
def display_scoreboard(player_name, player_score, computer_score):
    print(f"\n--- SCOREBOARD ---")
    print(f"{player_name}: {player_score}")
    print(f"Computer: {computer_score}")
    print("------------------")

# 4. Main game logic function
def play_game(player_name):
    player_score = 0
    computer_score = 0
    
    # Use an infinite loop as required by rubric
    while True:
        input(f"\n{player_name}, press Enter to roll for the next round...")
        
        # Get random rolls for both
        player_roll = random.randint(1, 6)
        comp_roll = random.randint(1, 6)
        
        print(f"{player_name} rolled a {player_roll}")
        print(f"Computer rolled a {comp_roll}")
        
        # Update scores using the check_dice function (No globals!)
        player_score = check_dice(player_score, player_roll)
        computer_score = check_dice(computer_score, comp_roll)
        
        # Display current status
        display_scoreboard(player_name, player_score, computer_score)
        
        # Check for win conditions
        if player_score >= 40 and computer_score >= 40:
            if player_score == computer_score:
                print("It's a TIE!")
            elif player_score > computer_score:
                print(f"Both over 40, but {player_name} is closer to the lead! {player_name} wins!")
            else:
                print("Both over 40, but Computer rolled higher! Computer wins!")
            break
        elif player_score >= 40:
            print(f"Congratulations {player_name}, you win!")
            break
        elif computer_score >= 40:
            print("The computer hit 40 first. You lose!")
            break

# 5. Main function to start everything
def main():
    print_welcome()
    name = input("Please enter your name: ")
    play_game(name)

if __name__ == "__main__":
    main()
