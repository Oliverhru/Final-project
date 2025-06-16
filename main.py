from functions import *

print("**** Welcome to Stepping Stones Game ****")
program_continued = True

while program_continued:
    difficulty = choose_difficulty()

    if difficulty == "easy":
        play_easy_mode()
    elif difficulty == "hard":
        play_hard_mode()

    program_continued = continue_program()
    
