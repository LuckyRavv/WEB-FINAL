import random

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    print("You can go left or right.")

def choose_direction():
    direction = input("Which way do you want to go? (left/right): ").lower()
    return direction

def encounter(direction):
    if direction == "left":
        print("You encounter a wild beast!")
        fight_or_flee()
    elif direction == "right":
        print("You find a treasure chest!")
        open_chest()
    else:
        print("Invalid direction! Please choose left or right.")
        main()

def fight_or_flee():
    action = input("Do you want to (fight) or (flee)? ").lower()
    if action == "fight":
        if random.choice([True, False]):
            print("You fought bravely and defeated the beast!")
        else:
            print("You were defeated by the beast. Game over.")
    elif action == "flee":
        print("You ran away safely!")
    else:
        print("Invalid action! Please choose fight or flee.")
        fight_or_flee()

def open_chest():
    if random.choice([True, False]):
        print("You found gold coins! You win!")
    else:
        print("The chest is empty. Better luck next time!")

def main():
    intro()
    direction = choose_direction()
    encounter(direction)

if __name__ == "__main__":
    main()