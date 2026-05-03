import random

# Hey! This function just says hi and explains the rules so the player isn't confused.
def print_welcome():
    print("--- Welcome to the Game of Pig! ---")
    print("How to play:")
    print("You and the computer take turns rolling a die.")
    print("Roll a 2 through 6? Awesome, those points get added to your total.")
    print("Roll a 1? Bummer, your whole score goes back to zero.")
    print("The first one to hit 40 points is the winner!")
    print("-----------------------------------")

# This is where we handle the math for the rolls. 
# It checks if someone rolled a 1 and resets them if they did.
def check_dice(current_total, dice_roll):
    if dice_roll == 1:
        return 0  # Back to square one!
    else:
        return current_total + dice_roll

# This just prints out the current scores so we can see who is winning.
def display_scoreboard(player_name, player_score, computer_score):
    print(f"\n--- CURRENT STANDINGS ---")
    print(f"{player_name}: {player_score}")
    print(f"Computer: {computer_score}")
    print("-------------------------")

# This is the actual game loop. It keeps running until someone wins.
def play_game(player_name):
    player_score = 0
    computer_score = 0
    
    # We keep the game going in a loop until the "break" hits.
    while True:
        input(f"\n{player_name}, hit Enter to roll...")
        
        # Picking a random number from 1 to 6 for both players.
        player_roll = random.randint(1, 6)
        comp_roll = random.randint(1, 6)
        
        print(f"{player_name} rolled a {player_roll}")
        print(f"Computer rolled a {comp_roll}")
        
        # Updating the scores using the logic from our check_dice function.
        player_score = check_dice(player_score, player_roll)
        computer_score = check_dice(computer_score, comp_roll)
        
        # Showing the updated scoreboard.
        display_scoreboard(player_name, player_score, computer_score)
        
        # Here we check if the game is over.
        if player_score >= 40 and computer_score >= 40:
            # Handling a tie or a close call if both pass 40 at the same time.
            if player_score == computer_score:
                print("No way! It's actually a tie!")
            elif player_score > computer_score:
                print(f"You both passed 40, but {player_name} had the lead! You win!")
            else:
                print("Close one, but the Computer had a higher score. Computer wins!")
            break
        elif player_score >= 40:
            print(f"Nice job {player_name}, you win!")
            break
        elif computer_score >= 40:
            print("The computer beat you to 40. Better luck next time!")
            break

# This is where the program actually starts.
def main():
    print_welcome()
    name = input("What's your name? ")
    play_game(name)

# This makes sure the game runs when you hit 'play' on the script.
if __name__ == "__main__":
    main()
