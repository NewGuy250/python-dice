import random

# Function to get the number of sides for the dice
def get_sides():
    while True:
        try:
            sides = int(input("Enter the number of sides on the dice: "))
            if sides < 2:  # Ensure the dice has at least 2 sides
                print("Number of sides must be 2 or greater.", end="\n\n")
                continue
            return sides
        except ValueError:
            print("Please enter a valid number.", end="\n\n")

# Function to get the number of dice to roll
def get_number_of_dice():
    while True:
        try:
            dice = int(input("Enter the number of dice you want to roll: "))
            if dice < 1:  # Ensure at least 1 die is rolled
                print("Number of dice must be 1 or greater.", end="\n\n")
                continue
            return dice
        except ValueError:
            print("Please enter a valid number.", end="\n\n")

# Function to perform the dice rolls
def get_roll(sides, dice):
    res = list()
    for _ in range(dice):  # Roll the dice the specified number of times
        res.append(random.randint(1, sides))
    return res

# Main function to run the dice game
def main():
    print("Welcome to my dice game!")
    while True:
        # Get user inputs
        sides = get_sides()
        dice = get_number_of_dice()
        roll = get_roll(sides, dice)

        # Display the roll results
        print(f"You rolled a total of {sum(roll)} ({', '.join(map(str, roll))})", end="\n\n") # Convert list of ints into str
        
        # Ask the user if they want to play again
        play_again = input("Do you want to roll again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break  # Exit the main loop

# Check if the script is run directly
if __name__ == "__main__":
    main()
