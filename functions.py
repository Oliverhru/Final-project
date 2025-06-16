import random

def choose_difficulty():
    choose_mode = input("Would you like to choose your mode? yes or no: ").lower()
    
    if choose_mode == 'yes':
        selected_character = input("Please select to play as player_001 or player_456: ").lower()
        if selected_character == "player_001":
            return "easy"
        else: 
            return "hard"
    else:
        mode = random.randint(1, 2)
        if mode == 1:
            print("You will now play as player_001")
            return "easy"
        else:
            print("You will now be playing as player_456")
            return "hard"

def play_easy_mode():
    rounds = 0
    move_left = True 
    
    while rounds < 5:
        choice = input("We will now begin, please move left or right: ").lower()
        
        if move_left and choice == 'left' or not move_left and choice == 'right':
            print("Correct, keep pushing through!!!")
        else:
            print("Wrong!!! Now you have died...")
            return

        move_left = not move_left 
        rounds += 1

    print(f"You have now completed all {rounds} rounds!")

def play_hard_mode():
    rounds = 0
    while rounds < 10:
        choice = input("We will now begin, please move left or right: ").lower()
        if random.choice(["left", "right"]) == choice:
            rounds += 1
            print("Great job! just a few more")
        else:
            print("Wrong!!! Now you have died...")
            return
    
    print(f"You have now completed all {rounds} rounds!")

def continue_program():
    again = input("Would you like to try again? Enter yes or no: ").lower()
    return again == "yes"