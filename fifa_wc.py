import time, sys, random, threading

# Classes
class TxtQuestions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class McQuestions:
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options


# Variables
txt_questions_list = [
    TxtQuestions("In what year was the first FIFA Women’s World Cup?\n>> ", "1991"),
    TxtQuestions(
        "Which nation is the only one to top the FIFA World Rankings without ever winning a World Cup?\n>> ",
        "Belgium",
    ),
    TxtQuestions(
        "The 1966 final was played at which football stadium?\n>> ", "Wembley"
    ),
    TxtQuestions("Who was the top scorer in the 2002 FIFA World Cup?\n>> ", "Ronaldo"),
    TxtQuestions("Who won the 2018 FIFA World Cup?\n>> ", "France"),
    TxtQuestions("In what year was the inaugural tournament?\n>> ", "1930"),
    TxtQuestions("Which nation has won the most World Cups?\n>> ", "Brazil"),
    TxtQuestions("How often is the World Cup held?\n>> ", "every 4 years"),
    TxtQuestions(
        "Which 2 years did the scheduled tournaments not go ahead due to WWII?\n>> ",
        "1942 and 1946",
    ),
    TxtQuestions("What was the first World Cup trophy called?\n>> ", "Jules Rimet"),
    TxtQuestions(
        "How many times have North Korea qualified for the tournament?\n>> ",
        "2",
    ),
    TxtQuestions(
        "Who did Zinedine Zidane headbutt in the 2006 final?\n>> ",
        "Marco Materazzi",
    ),
    TxtQuestions("In what year did Spain win their first World Cup?\n>> ", "2010"),
    TxtQuestions(
        "What is the USA's highest finishing position at a World Cup?\n>> ", "3rd"
    ),
    TxtQuestions(
        "Who is the all-time leading World Cup goalscorer?\n>> ", "Miroslav Klose"
    ),
    TxtQuestions(
        "Which nation is the only one to participate in every tournament?\n>> ",
        "Brazil",
    ),
    TxtQuestions("How many World Cups did Pele win?\n>> ", "3"),
    TxtQuestions("In what year was Maradona's 'Hand of God' incident?\n>> ", "1986"),
    TxtQuestions(
        "What animal was the official mascot for the 1998 World Cup in France?\n>> ",
        "cockerel",
    ),
    TxtQuestions(
        "Which African footballer is the oldest person ever to score in a World Cup?\n>> ",
        "Roger Milla",
    ),
    TxtQuestions(
        "Who was the manager of the German national team when they won in 2014?\n>> ",
        "Joachim Low",
    ),
    TxtQuestions(
        "Which nation hosted the 1994 FIFA World Cup?\n>> ", "usa united states"
    ),
    TxtQuestions(
        "What was the final score in the 2014 final between Germany and Argentina?\n>> ",
        "1-0",
    ),
    TxtQuestions(
        "Which company have published sticker albums for every World Cup since 1970?\n>> ",
        "Panini",
    ),
    TxtQuestions(
        "What musical instrument was banned by FIFA after the 2010 World Cup?\n>> ",
        "vuvuzela",
    ),
    TxtQuestions("How many times have Italy won the World Cup so far?\n>> ", "4"),
    TxtQuestions(
        "Which British pop star performed at the opening ceremony of the 2018 tournament?\n>> ",
        "Robbie Williams",
    ),
    TxtQuestions(
        "Who was the youngest manager to win the World Cup?\n>> ",
        "Alberto Suppici",
    ),
    TxtQuestions(
        "A World Cup winning team has never been managed by someone of a different nationality. True or False?\n>> ",
        "True",
    ),
]
mc_questions_list = [
    McQuestions(
        "Which 3 countries will host the 2026 tournament?",
        "1",
        [
            "1 - USA, Canada, Mexico",
            "2 - Portugal, Spain, Ukraine",
            "3 - Germany, Poland, France",
        ],
    ),
    McQuestions(
        "Which 3 teams were in England's group in 2018?",
        "2",
        [
            "1 - Iceland, Portugal, Tunisia",
            "2 - Belgium, Tunisia, Panama",
            "3 - Wales, France, Senegal",
        ],
    ),
    McQuestions(
        "Which nation has only ever played a single World Cup game?",
        "1",
        ["1 - Indonesia", "2 - North Korea", "3 - Italy"],
    ),
    McQuestions(
        "Which 2 countries made their World Cup debuts in 2018?",
        "3",
        ["1 - Morocco and Panama", "2 - Ghana and Panama", "3 - Iceland and Panama"],
    ),
    McQuestions(
        "Which sports brand has supplied every World Cup since 1970 with balls?",
        "2",
        ["1 - Nike", "2 - Adidas", "3 - Puma"],
    ),
    McQuestions(
        "What colour was the ball used in the 1966 final?",
        "1",
        ["1 - Orange", "2 - Blue", "3 - White"],
    ),
    McQuestions(
        "In what year was the World Cup first broadcast on TV?",
        "3",
        ["1 - 1962", "2 - 1986", "3 - 1954"],
    ),
    McQuestions(
        "Which English player has won the Golden Boot award?",
        "2",
        ["1 - Alan Shearer", "2 - Gary Lineker", "3 - Michael Owen"],
    ),
    McQuestions(
        "How many teams qualify from the group stages to the knockout rounds?",
        "1",
        ["1 - 16", "2 - 20", "3 - 24"],
    ),
    McQuestions(
        "Which host nation had an orange as their tournament mascot?",
        "3",
        ["1 - France", "2 - Netherlands", "3 - Spain"],
    ),
    McQuestions(
        "Who won the Best Young Player Award in 2018?",
        "1",
        ["1 - Kylian Mbappe", "2 - Leroy Sane", "3 - Harry Kane"],
    ),
    McQuestions(
        "Before Qatar 2022, how many nations have won the FIFA World Cup?",
        "2",
        ["1 - 12 nations", "2 - 8 nations", "3 - 6 nations"],
    ),
    McQuestions(
        "Which nation was the first Asian country to reach the World Cup semi-finals?",
        "2",
        ["1 - Japan", "2 - South Korea", "3 - Malaysia"],
    ),
]

random_typeofq = 0
random_qnum = 0
input_ans = ""
question = ""

user_score = 0
keeper_score = 0

shot_placement_input = "1"
shot_placement = ""

# Functions
def start_game():
    typing_print("\nWelcome to the FOOTBALL ROOM!\n\n")
    typing_print(
        "It's come down to a penalty shootout in the FINAL of the World Cup 2022. WIN it for your country!"
    )
    print(
        """
                      ,;;;:.
                     ;;''''`:
                     ;(  O O|              ,;;,
                      |   _\|              \  |
                       \__-/              ,' /
                       |   |             /  /
                 _,--''`---'''-------.,-'  /
               ,'  /          `.     |  _,'
             ,'    |====== WM =|     |-'
            \      ,======|  |=|''---'
           / `.  ,' \      \/ /
         ,'. ,'`'   | --._    |
       ,'  ,'       |         |
   __,' _,'         \    -._  |
  `- ,-'            |---------)
 ';;'               ;:::::::::|
                   ;:::::::::::\

                  /::::::;:::::|
                 /_:::::/\:::::_\

                 / `-:_/  \,-' |
                /    /     \   |
                |   |      | _,)
                \_,-\      |   |
                 \   |     |   |
                  |__|      \,-|
                  /##|      |  |
                 \##/       |  |
                ,-'''-.     |,-|
               // \_/ \\    `.##\

               |\_/ \_/|      `--`
               \/ \_/ \/
                `-...-'
"""
    )
    time.sleep(0.5)
    typing_print(
        "Getting a question right increases your chances of scoring a goal, so get them all right!\nScore 5 and CONQUER this room!\n\n"
    )
    time.sleep(1.5)
    typing_print("You take the first shot.\n")
    time.sleep(1.5)
    shot_placement_menu()


def shot_placement_menu():
    global shot_placement_input, shot_placement
    typing_print("\nWhere do you want to place your penalty?\n\n")

    print("Bottom left corner (1)")
    print("Bottom right corner (2)")
    print("Middle (3)")
    print("Top left corner (4)")
    print("Top left corner (5)")

    shot_placement_input = input("\nChoose which number you'd like to shoot at\n>> ")

    if shot_placement_input.isdigit() == False:
        typing_print("\nThat doesn't seem to be a number mate, try again\n")
        shot_placement_menu()

    while int(shot_placement_input) >= 1 or int(shot_placement_input) <= 5:
        if int(shot_placement_input) == 1:
            shot_placement = (
                "Your shot was slotted into the left corner, incredible penalty!\n"
            )
        elif int(shot_placement_input) == 2:
            shot_placement = "Your shot was beautifully placed into the right corner, absolute quality!\n"
        elif int(shot_placement_input) == 3:
            shot_placement = "You've gone for the panenka and it's paid off! The keeper did not see that coming!\n"
        elif int(shot_placement_input) == 4:
            shot_placement = "WOW! A rocket of a shot into the top left bins, Ronaldo would be proud of that\n"
        elif int(shot_placement_input) == 5:
            shot_placement = "Was that a bird or a plane? NO, it was the ball flying into the top right of the net! Keeper had no chance\n"
        elif int(shot_placement_input) < 1 or int(shot_placement_input) > 5:
            typing_print("\n\nYou can't shoot there mate, try again")
            shot_placement_menu()
        break

    generate_question()


def generate_question():
    global random_typeofq, random_qnum, question, input_ans

    random_typeofq = random.randint(0, 1)
    if random_typeofq == 0:
        random_qnum = random.randint(0, (len(txt_questions_list) - 1))
        question = txt_questions_list[random_qnum].question
    else:
        random_qnum = random.randint(0, (len(mc_questions_list) - 1))
        question = f"{mc_questions_list[random_qnum].question}\n{mc_questions_list[random_qnum].options}\n\n>> "

    timer = threading.Timer(60.0, answer_check)
    timer.start()
    input_ans = typing_input(f"\n{question}").lower()
    timer.cancel()
    answer_check()


def answer_check():
    global user_score, keeper_score

    random_score_chance = random.randint(1, 10)

    if input_ans == "" or input_ans.isspace() == True:
        typing_print("You didn't even kick the ball!\n")
        typing_print(f"Correct answer was {txt_questions_list[random_qnum].answer}")
        score_check()
        txt_questions_list.pop(random_qnum)
    elif random_typeofq == 0:
        if input_ans in (txt_questions_list[random_qnum].answer).lower():
            if random_score_chance >= 1 and random_score_chance <= 8:
                txt_questions_list.pop(random_qnum)
                user_score += 1
                print(
                    """
   _____  ____          _      _
  / ____|/ __ \   /\   | |    | |
 | |  __| |  | | /  \  | |    | |
 | | |_ | |  | |/ /\ \ | |    | |
 | |__| | |__| / ____ \| |____|_|
  \_____|\____/_/    \_\______(_)


"""
                )
                typing_print(f"{shot_placement}Score {user_score} - {keeper_score}\n")
                score_check()
            elif random_score_chance > 8:

                keeper_score += 1
                typing_print(
                    f"\nGreat shot, but the keeper's on fire! Penalty saved!\nScore {user_score} - {keeper_score}\n"
                )
                txt_questions_list.pop(random_qnum)
                score_check()
        else:
            if random_score_chance == 9 or random_score_chance == 10:
                user_score += 1
                print(
                    """
   _____  ____          _      _
  / ____|/ __ \   /\   | |    | |
 | |  __| |  | | /  \  | |    | |
 | | |_ | |  | |/ /\ \ | |    | |
 | |__| | |__| / ____ \| |____|_|
  \_____|\____/_/    \_\______(_)


"""
                )
                typing_print(
                    f"\n\nYou got the question WRONG, but the keeper has had a nightmare and fumbled the ball, lucky goal!\nCorrect answer was {txt_questions_list[random_qnum].answer}\n\n"
                )
                typing_print(f"Score {user_score} - {keeper_score}\n")
                txt_questions_list.pop(random_qnum)
                score_check()
            else:

                typing_print(
                    f"\nYou've had a howler, the ball is in row Z!\nCorrect answer was {txt_questions_list[random_qnum].answer}\n\n"
                )
                typing_print(f"{user_score} - {keeper_score}\n")
                txt_questions_list.pop(random_qnum)
                score_check()
    elif random_typeofq == 1:
        if (
            input_ans == mc_questions_list[random_qnum].answer
            and input_ans.isdigit() == True
            and int(input_ans) > 0
            and int(input_ans) < 3
        ):
            if random_score_chance >= 1 and random_score_chance <= 8:
                mc_questions_list.pop(random_qnum)
                user_score += 1
                print(
                    """
   _____  ____          _      _
  / ____|/ __ \   /\   | |    | |
 | |  __| |  | | /  \  | |    | |
 | | |_ | |  | |/ /\ \ | |    | |
 | |__| | |__| / ____ \| |____|_|
  \_____|\____/_/    \_\______(_)


"""
                )
                typing_print(f"{shot_placement}Score {user_score} - {keeper_score}\n")
                score_check()
            elif random_score_chance > 8:

                keeper_score += 1
                typing_print(
                    f"\nGreat shot, but the keeper's on fire! Penalty saved!\nScore {user_score} - {keeper_score}\n"
                )
                mc_questions_list.pop(random_qnum)
                score_check()
        else:
            if input_ans.isdigit() == False or int(input_ans) < 1 or int(input_ans) > 3:
                typing_print("\nThat isn't an option mate, you've had a nightmare!\n")
                score_check()
            elif random_score_chance == 9 or random_score_chance == 10:
                user_score += 1
                print(
                    """
   _____  ____          _      _
  / ____|/ __ \   /\   | |    | |
 | |  __| |  | | /  \  | |    | |
 | | |_ | |  | |/ /\ \ | |    | |
 | |__| | |__| / ____ \| |____|_|
  \_____|\____/_/    \_\______(_)


"""
                )
                typing_print(
                    f"\n\nYou got the question WRONG, but the keeper has had a nightmare and fumbled the ball, lucky goal!\nCorrect answer was {mc_questions_list[random_qnum].answer}\n\n"
                )
                typing_print(f"Score {user_score} - {keeper_score}\n")
                mc_questions_list.pop(random_qnum)
                score_check()
            else:
                typing_print(
                    f"\nYou've had a howler, the ball is in row Z!\nCorrect answer was {mc_questions_list[random_qnum].answer}\n\n"
                )
                typing_print(f"Score {user_score} - {keeper_score}\n")
                mc_questions_list.pop(random_qnum)
                score_check()


def score_check():
    if user_score == 4:
        time.sleep(1.25)
        typing_print("\nONE MORE GOAL AND YOU WIN.\n")
        time.sleep(1)
        shot_placement_menu()
    elif user_score < 5 and keeper_score < 5:
        time.sleep(1)
        shot_placement_menu()
    elif user_score < 5 and keeper_score == 5:
        loss_screen()
    elif user_score == 5 and keeper_score < 5:
        win_screen()


def loss_screen():
    typing_print(
        "You fell under the pressure and failed to beat the keeper 5 times...\nYou failed your country"
    )
    end()


def win_screen():
    typing_print("\n\nYOU HAVE WON THE WORLD CUP, YOU'RE IN THE HISTORY BOOKS!\n\n\n")
    print(
        """"        ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣶⣦⣶⣶⣶⣶⣶⣤⣶
⣿⡅⠀⣀⣀⣀⣀⣀⣁⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣀⣄⣨⣁⣄⡄⠀⢸⡿
⣿⡇⠀⢿⡟⠛⠛⠛⠛⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠛⠛⠛⠛⣿⡇⠀⣾⡟
⢹⣧⠀⢸⣧⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⠀⣿⠇⠀⣿⠇
⠈⣿⡆⠀⣿⡄⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⢸⣿⠀⢸⡿⠨
⠀⢹⣷⠀⢻⣧⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⢀⣾⠇⢠⣿⠃⠀
⠀⠀⢻⣧⠈⢿⣦⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⣼⡟⠀⣾⡏⠀⠀
⠀⠀⠈⢿⣇⠈⣿⣆⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢀⣼⡟⢀⣾⠏⠀⠀⠀
⠀⠀⠀⠀⢻⣧⡛⢻⣧⡀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⢀⣾⠟⢠⣾⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣤⠹⣿⣆⠀⠹⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⢀⣴⡿⠃⣰⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣦⡈⠻⣷⣄⢻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢃⣴⡿⠋⣠⣾⡟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡈⠛⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠿⠋⣠⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣷⣄⡈⢻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⢁⣤⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣶⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣯⣶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣶⣦⣄⣀⣀⠀⢀⣀⣀⣤⣴⣶⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣿⠀⠈⣿⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣶⣶⣾⣿⣶⣶⣿⣶⣶⣶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣠⣿⣅⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣹⣿⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡾⠟⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠻⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⣶⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣶⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀WORLD CUP 2022 ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    )
    end()


def end():
    end_input = typing_input("Play again (1) or exit room? (2)\n>> ")
    if end_input == "1":
        start_game()
    elif end_input == "2":
        exit()
    else:
        typing_print("That option doesn't exist mate, try again")
        end()


def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)


def typing_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    value = input()
    return value


start_game()
