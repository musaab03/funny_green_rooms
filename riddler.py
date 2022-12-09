# A room of riddles to beat the Riddler of Gotham.
import sys, time

def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

lives_q1 = 3
lives_q2 = 3
lives_q3 = 3
lives_q4 = 3
lives_q5 = 3

typing_print("\n\nWelcome to The Riddler Room\n")
typing_print(
    "\nIn this room you will have 5 riddles to solve, to escape the Riddle Room\n"
)
typing_print("\nYou will have 3 lives per riddle\n")
typing_print("\nGood Luck, Gotham Needs You!!\n")

def question_one():
    global lives_q1
    typing_print("\nRiddle 1:- I can be cracked. I can be made. I can be told. I can be played. What am I?\n")
    answer = input("\n\nType your answer here: ").lower()
    if answer == "a joke" or answer == "joke":
        typing_print("\nYou are correct\n\n")
    else:
        lives_q1 -= 1
        if lives_q1 >=1:
            typing_print("\nThat is incorrect, try again\n\n")
            typing_print(f"\nYou have {str(lives_q1)} lives left\n")
            question_one()
        else:
            typing_print("\nThat is incorrect, you have 0 lives.\n")            
question_one()    

def question_two():
    global lives_q2
    typing_print("\nRiddle 2:- What English word has three consecutive double letters?\n")
    answer = input("\n\nType your answer here: ").lower()
    if answer == "a bookkeeper" or answer == "bookkeeper":
        typing_print("\nYou are correct\n\n")
    else:
        lives_q2 -= 1
        if lives_q2 >=1:
            typing_print("\nThat is incorrect, try again\n\n")
            typing_print(f"\nYou have {str(lives_q2)} lives left\n")
            question_two()
        else:
            typing_print("\nThat is incorrect, you have 0 lives.\n")            
question_two()  

def question_three():
    global lives_q3
    typing_print("\nRiddle 3:- I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?\n")
    answer = input("\n\nType your answer here: ").lower()
    if answer == "a map" or answer == "map":
        typing_print("\nYou are correct\n\n")
    else:
        lives_q3 -= 1
        if lives_q3 >=1:
            typing_print("\nThat is incorrect, try again\n\n")
            typing_print(f"\nYou have {str(lives_q3)} lives left\n")
            question_three()
        else:
            typing_print("\nThat is incorrect, you have 0 lives.\n")            
question_three()  

def question_four():
    global lives_q4
    typing_print("\nRiddle 4:- What Is The Beginning Of Eternity, The End Of Time And Space, The Beginning Of Every End, And The End Of Every Race?\n")
    answer = input("\n\nType your answer here: ").lower()
    if answer == "The letter e" or answer == "The letter E" or answer == "E" or answer == "e":
        typing_print("\nYou are correct\n\n")
    else:
        lives_q4 -= 1
        if lives_q4 >=1:
            typing_print("\nThat is incorrect, try again\n\n")
            typing_print(f"\nYou have {str(lives_q4)} lives left\n")
            question_four()
        else:
            typing_print("\nThat is incorrect, you have 0 lives.\n")            
question_four()    

def question_five():
    global lives_q5
    typing_print("\nRiddle 5:-What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats?\n")
    answer = input("\n\nType your answer here: ").lower()
    if answer == "a river" or answer == "river":
        typing_print("\nYou are correct\n\n")
    else:
        lives_q5 -= 1
        if lives_q5 >=1:
            typing_print("\nThat is incorrect, try again\n\n")
            typing_print(f"\nYou have {str(lives_q5)} lives left\n")
            question_five()
        else:
            typing_print("\nThat is incorrect, you have 0 lives.\n")            
question_five()    

# User gets to answer the question
# we see if the user's answer is correct
# if they get the anserr right they move on to the next one
# if they get it wrong they lose a life, they get another chance to answer the same question
# if they lose three lives they are out of the game


# User gets to answer the question
# we see if the user's answer is correct
# if they get the anserr right they move on to the next one
# if they get it wrong they lose a life, they get another chance to answer the same question
# if they lose three lives they are out of the game