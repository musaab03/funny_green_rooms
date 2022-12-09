import time, sys

def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typing_print_fast(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

# def exit_game():
# Run code to code to stage 2 of main room

def welcome_part1():
  typing_print("\nWELCOME TO THE QUIZ MASTER'S ROOM\n\n")
  typing_print("WILL YOU BEAT THE QUIZ MASTER?\n\n")
  typing_print("THE QUIZ MASTER WAS BORN FROM THE PRIME ORDEAL SOUP FOLLOWING THE BIG BANG 13.6 BILLION YEARAS AGO!\n\n")
  typing_print("HE HAS ALL OF THE KNOWLEDGE IN THE UNIVERSE!\n\n")
  typing_print("WITHIN HIS REALM, FOR THOSE SPECIES THAT HAVE EATEN FROM THE APPLE OF KNOWLEDGE, THEY MUST PROVE THEIR WORTH OR ELSE!\n\n")
  typing_print("WILL YOU BEAT THE QUIZ MASTER AND SAVE THE HUMAN RACE?\n\n")
  typing_print("OR WILL HE PROVE WE ARE UNWORTHY TO EXIST AND DESTROY THE WHOLE EARTH?\n\n")
  typing_print("THE FUTURE OF THE EARTH AND ALL LIVING BEINGS ON IT, IS IN YOUR HANDS.\n\n")
  time.sleep(3)
welcome_part1()

def quiz_master():
    typing_print("              THE QUIZ MASTER              \n")
    typing_print_fast(r'''
                      ____...                                  
             .-"--"""".__     .
            |            `    |
  (         `._....------.._.:          
   )         .()''        ``().                                
  '          () .=='  `===  `-.         
   . )       (         g)                                
    )         )     /        J          
   (          |.   /      . (                                  
   $$         (.  (_'.   , )|`                                 
   ||         |\`-....--'/  ' \                                
  /||.         \\ | | | /  /   \.                              
 //||(\         \`-===-'  '     \o.                            
.//7' |)         `. --   / (     OObaaaad888b.                 
(<<. / |     .a888b`.__.'d\     OO888888888888a.               
 \  Y' |    .8888888aaaa88POOOOOO888888888888888.              
  \  \ |   .888888888888888888888888888888888888b              
   |   |  .d88888P88888888888888888888888b8888888.             
   b.--d .d88888P8888888888888888a:f888888|888888b             
   88888b 888888|8888888888888888888888888\8888888
    '''
    )
quiz_master()

def welcome_part2():
    typing_print("\n\nThese are the instructions from The Quiz Master\n\n")
    typing_print("Human. This is a general knowledge quiz and the future of your Earth depends on it.\n\n")
    typing_print("Do not think that I, The Quiz Master, will hesitate to end the existence of everything on your fragile planet.\n\n")
    typing_print("Accurately answer as many questions as possible to earn points.\n\n")
    typing_print("To beat I, The Quiz Master, you must score 14 or more points from a maximum of 20 available points.\n\n")
    typing_print("Prove to me, that you are worthy of an intellectual existence.\n\n")
    time.sleep(3)

def continue_exit():
    typing_print("\nWILL YOU ACCEPT THE INVITATION TO SAVE THE EARTH AND BECOME A HERO?\n\n")
    answer=input("Please respond with 'Y' to continue or 'N' to exit? -> ")
    if answer == "Y" or answer == "y":
        welcome_part2 ()
    elif answer == "N" or answer == "n":
        exit_game()
    else:
        print("\nThat is an incorrect response. Please specify 'Y' to continue or 'N' to exit.\n")
        continue_exit()
continue_exit()

print("READY...\n")
time.sleep(1)
print("STEADY...\n")
time.sleep(1)
print("BE PATIENT...\n")
time.sleep(1)
print("AND...\n")
time.sleep(1)
print("GO! GO! GO!\n")

points_bal = 0
points_max = 0

def question1():
    global points_bal
    global points_max
    question_num = "One"
    subject = "Biology"
    question_text ="In which part of the body would you find your funny bone?"
    points = 1    
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    options = ["1 - Mouth, 2 - Head, 3 - Elbow, 4 - Knee"]
    print(f"Please select one from the following options:\n\n    {options}\n")
    answer=input("What is the correct answer? Please type the number associated to your selection ANSWER -> ")
    correct_answer="3"
    if answer == correct_answer:
        points_bal += points
        points_max += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    elif answer == "1" or answer == "2" or answer == "3":
        points_max += points
        print(f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.")
    else:
        print("\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n")
        time.sleep(3)
        question1()
question1()
time.sleep(5)

def question2():
    global points_bal
    global points_max
    question_num = "Two"
    subject = "History"
    question_text ="How many wives did King Henry The 8th of England have during his lifetime?"
    points = 2
    points_max += points
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    answer=input("Please specify an integer / number and NOT a word / string. ANSWER -> ")
    correct_answer="6"
    if answer == correct_answer:
        points_bal += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:
        answer != correct_answer
        print(f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
question2()
time.sleep(5)

def question3():
    global points_bal
    global points_max
    question_num = "Three"
    subject = "Sport"
    question_text ="In which year did the England football team win their first World Cup?"
    points = 1
    points_max += points
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    answer=input("Please specify an integer / number that is 4 characters long e.g. 1945. ANSWER -> ")
    correct_answer="1966"
    if answer == correct_answer:
        points_bal += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:    
        answer != correct_answer
        print(f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
question3()
time.sleep(5)

def question4():
    global points_bal
    global points_max
    question_num = "Four"
    subject = "Geography"
    question_text ="In which body of water would you find the Galapagos Islands?"
    points = 2
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    options = ["1 - Atlantic Ocean, 2 - Indian Ocean, 3 - Pacific Ocean, 4 - Gulf Of Mexico"]
    print(f"Please select one from the following options:\n\n    {options}\n")
    answer=input("What is the correct answer? Please type the number associated to your selection ANSWER -> ")
    correct_answer="3"
    if answer == correct_answer:
        points_bal += points
        points_max += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    elif answer == "1" or answer == "2" or answer == "3":
        points_max += points
        print(f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:
        print("\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n")
        time.sleep(3)
        question4()
question4()
time.sleep(5)

def question5():
    global points_bal
    global points_max
    question_num = "Five"
    subject = "Mathematics"
    question_text ="What is the answer to the equation 110 x 55 = ?"
    points = 3
    points_max += points
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    answer=input("Please specify an integer / number. ANSWER -> ")
    correct_answer="6050"
    if answer == correct_answer:
        points_bal += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:    
        answer != correct_answer
        print(f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
question5()
time.sleep(5)

def question6():
    global points_bal
    global points_max
    question_num = "Six"
    subject = "Economics"
    question_text ="You have £2,000 in cash and you keep hold of it under your mattress.\n\nIn one year, the government reports a consumer price index inflation rate of 12%.\n\n“In real terms”, in todays' money, how much buying power does your £2,000 have when the government makes the announcement?"
    points = 3
    points_max += points
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    answer=input("Please specify an integer / number without the £ symbol e.g. 1234. ANSWER -> ")
    correct_answer="1760"
    if answer == correct_answer:
        points_bal += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:    
        answer != correct_answer
        print(f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
question6()
time.sleep(5)

def question7():
    global points_bal
    global points_max
    question_num = "Seven"
    subject = "Observation"
    question_text ="Do I, The Quiz Master, have any bad habits?"
    points = 1
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    options = ["1 - Alcohol, 2 - Smoking, 3 - Swearing, 4 - Flashing"]
    print(f"Please select one from the following options:\n\n    {options}\n")
    answer=input("What is the correct answer? Please type the number associated to your selection ANSWER -> ")
    correct_answer="2"
    if answer == correct_answer:
        points_bal += points
        points_max += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    elif answer == "1" or answer == "3" or answer == "4":
        points_max += points
        print(f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:
        print("\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n")
        time.sleep(3)
        question7()
question7()
time.sleep(5)

def question8():
    global points_bal
    global points_max
    question_num = "Eight"
    subject = "Mythology"
    question_text ="In Greek Mythology, which creature protects the entrance to the Underworld?"
    points = 2
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    options = ["1 - Hades, 2 - Cerebus, 3 - Poseidon, 4 - Medusa"]
    print(f"Please select one from the following options:\n\n    {options}\n")
    answer=input("What is the correct answer? Please type the number associated to your selection ANSWER -> ")
    correct_answer="2"
    if answer == correct_answer:
        points_bal += points
        points_max += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    elif answer == "1" or answer == "2" or answer == "3":
        points_max += points
        print(f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:
        print("\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n")
        time.sleep(3)
        question8()
question8()
time.sleep(5)

def question9():
    global points_bal
    global points_max
    question_num = "Nine"
    subject = "Movies"
    question_text ="Which movie is the highest grossing movie of all time?"
    points = 2
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    options = ["1 - Wiazard Of Oz, 2 - Jurassic World, 3 - Titanic, 4 - Avatar"]
    print(f"Please select one from the following options:\n\n    {options}\n")
    answer=input("What is the correct answer? Please type the number associated to your selection ANSWER -> ")
    correct_answer="4"
    if answer == correct_answer:
        points_bal += points
        points_max += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    elif answer == "1" or answer == "2" or answer == "3":
        points_max += points
        print(f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:
        print("\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n")
        time.sleep(3)
        question9()
question9()
time.sleep(5)

def question10():
    global points_bal
    global points_max
    question_num = "Ten"
    subject = "Enviromental Science"
    question_text ="For the same mass of gas, which of these gases has the greatest impact on climate change and increasing temperatues?"
    points = 3
    question=f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
    print(question)
    options = ["1 - Carbon Dioxide, 2 - Methane, 3 - Oxygen, 4 - Nitrogen"]
    print(f"Please select one from the following options:\n\n    {options}\n")
    answer=input("What is the correct answer? Please type the number associated to your selection ANSWER -> ")
    correct_answer="2"
    if answer == correct_answer:
        points_bal += points
        points_max += points
        print(f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    elif answer == "1" or answer == "3" or answer == "4":
        points_max += points
        print(f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n")
    else:
        print("\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n")
        time.sleep(3)
        question10()
question10()
time.sleep(3)

print(f"Your final points tally is {points_bal}. But was it enough to beat The Quiz Master?")
time.sleep(3)

def end_of_game():
    if points_bal >= 14:
        print("\n\nCONGRATULATIONS! WOO HOO!\n\n")
        typing_print ("\nYOU BEAT THE DASTARDLY QUIZ MASTER!\n\n")
        typing_print ("\nYOU HAVE SAVED THE EARTH AND ALL LIVING THINGS ON IT!\n\n")
        typing_print ("\nYOU ARE A HERO AND YOUR NAME WILL BE SANG THROUGHOUT THE AGES!\n\n")
        time.sleep(2)
        typing_print_fast(r"""
            
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.
        
        """)
        typing_print_fast(r"""        
            .=.,
            ;c =\
          __|  _/
        .'-'-._/-'-._
       /..   ____    \
      /' _  [<_->] )  \
     (  / \--\_>/-/'._ )
      \-;_/\__;__/ _/ _/
       '._}|==o==\{_\/
        /  /-._.--\  \_
       // /   /|   \ \ \
      / | |   | \;  |  \ \
     / /  | :/   \: \   \_\
    /  |  /.'|   /: |    \ \
    |  |  |--| . |--|     \_\
    / _/   \ | : | /___--._) \
   |_(---'-| >-'-| |       '-'
          /_/     \_\
        """)
        time.sleep(2)
        typing_print("\nYou escaped The Quiz Master's Room victorious!")
        time.sleep(3)

    elif points_bal <= 13:
        print("\n\nOH NO! WHAT WENT WRONG?\n")
        typing_print("\n# THE QUIZ MASTER WAS TOO GOOD FOR YOU!\n\n")
        typing_print("\nTHE EARTH WILL PERISH AND EVERYTHING IS OVER!\n\n")
        typing_print("\nGOODBYE... FOREVER!\n\n")
        time.sleep(2)
        typing_print_fast(r"""
            
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.
        
        """)
        print("\n.....5.....\n\n")
        time.sleep(1)
        print("\n.....4.....\n\n")
        time.sleep(1)
        print("\n.....3.....\n\n")
        time.sleep(1)
        print("\n.....2.....\n\n")
        time.sleep(1)
        print("\n.....1.....\n\n")
        print(r"""
        
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.
        
        """)
        time.sleep(1)
        typing_print_fast("\n.....BOOM....\n\n")
        print(r"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠤⠖⠛⣷⣶⣶⠿⢿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⣾⣿⠋⠀⠀⠀⢾⣿⠏⠀⠀⠀⠀⠈⠛⠻⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢻⣷⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣤⣤⣠⣶⣿⡅⠀⠀⠀⣤⣤⣴⣶⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠆⠀⠹⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⣰⡿⠋⠉⢹⣿⠁⠉⠀⠀⠀⠀⠀⣿⠏⠀⠀⠀⠀⢀⣠⣤⠀⠀⠀⠀⠲⣤⣄⣀⣀⠀⠀⠀⠙⢻⣷⣦⡀⠀⠀⠀
⠀⣰⣿⠇⠀⠀⠸⠿⠂⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠠⣿⡏⠁⠀⠀⠀⠀⠀⠈⢿⠁⠀⠀⠀⠀⠀⠸⣿⠉⢿⣆⠀⠀
⢰⣿⡁⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⡀⠛⢿⣦⠀⠀⡀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠛⢀⠀⣿⡄⠀
⢸⡿⠁⠀⠀⢿⣄⠀⡀⠀⠀⠀⠀⢀⣤⣀⣀⣀⣤⣿⣷⣶⡿⠻⣿⣿⠿⣷⣦⣄⣸⣷⠀⠀⠀⢠⣄⠀⠀⠈⠛⠿⣿⠀
⠸⣿⣾⠃⠀⠀⠛⠿⠃⠀⠀⠰⣤⣴⣿⠿⠿⠿⠿⠛⠉⠉⠀⠀⡄⠀⢰⣿⠟⢿⣿⣿⣄⡀⢰⣿⡟⠀⠀⠀⠀⠀⢹⡇
⠀⢸⣿⢸⡆⠀⠶⠿⠀⣀⡀⠠⣬⣭⣭⣀⠀⣆⠀⠀⢠⠀⠀⣰⠃⣰⣿⣿⠏⠀⠀⣉⣿⣿⠀⠙⠷⠀⠀⢠⣶⡀⣸⣧
⠀⠸⣿⣿⣷⡄⠀⠀⠘⠋⠁⠀⠀⠀⠉⡛⢷⣽⣦⠀⢸⡄⠀⣿⢀⣿⣿⣿⡶⠒⠛⢋⡅⠀⠀⠀⢀⣴⢀⡼⠟⠛⠟⠁
⠀⠀⠈⠙⠻⣷⣶⣦⣴⡾⠛⠶⠦⣶⠾⢿⣶⣬⣿⡆⠸⣧⢠⡇⢸⣿⣿⣭⣥⣄⣀⣈⣤⣶⣦⣴⣿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣽⣿⠀⢿⠈⣧⣼⢹⣿⣀⣀⠉⠛⠛⠉⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⢿⡛⢹⣿⡄⠸⠇⣿⡇⠘⣿⡉⢉⣛⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⡿⢛⣉⣣⣾⣿⠛⣿⣷⠀⡀⢸⣇⢸⡟⠛⣿⡇⢠⡟⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣅⠀⠀⡉⠛⢿⣅⣀⣿⣿⠀⣿⣄⣉⣹⣧⡴⢾⣯⡀⠈⠋⠉⢻⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣏⣀⣾⣏⠀⠀⠈⠙⠿⠿⠋⢻⡟⠋⠛⢿⡀⠀⠸⠀⠀⣀⠀⠀⣽⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⢿⣷⣀⣀⣼⣦⠀⠀⠀⢁⣀⣠⣶⡀⠀⣀⣀⣀⣼⣤⣾⣿⡿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⣿⣷⣶⣿⠿⠟⣿⠛⠿⣶⣿⣿⠿⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⣰⠃⣿⡇⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢻⣇⠀⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠘⣿⠀⣿⠀⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣿⠀⣿⠀⣿⡆⠸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣯⣾⡟⠀⠁⠀⢿⣇⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⣻⣷⠿⠋⠀⡀⠀⠀⠸⢿⡄⠀⢻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠛⠁⠀⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """
        )
        time.sleep(2)
        typing_print("\nTHE EARTH IS NO MORE AND ALL HAS RETURNED TO SPACE DUST.")
        time.sleep(3)
        typing_print("\nYou failed to escape The Quiz Master's Room victorious.")
        time.sleep(3)
end_of_game()

# Would you like to play again or exit to the main room?
