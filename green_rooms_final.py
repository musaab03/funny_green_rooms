import time, sys, random, threading

# Main Game
room_choice_input = ""
xmas = True
pens = True
riddler = True
quiz = True


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


def main_game():
    typing_print("\nWELCOME TO THE FUNNY GREEN ESCAPE ROOMS!\n\n")
    time.sleep(0.5)
    typing_print("We have designed 4 fantastic fun rooms for your enjoyment!\n")
    typing_print(
        "\nYou only have ONE opportunity to conquer each room once you have left them!"
    )
    typing_print("\n\nCreated by Adam, Andrew, Jade and Musaab\n")
    room_choice_menu()


def room_choice_menu():
    global xmas, pens, riddler, quiz

    if xmas == False and pens == False and riddler == False and quiz == False:
        time.sleep(2)
        typing_print("\n\nYOU HAVE COMPLETED THE GAME!\n\n")
        quit()

    print("\nRoom Selection:")
    if xmas == True:
        print("\nChristmas Quiz - Made by Jade (1)")
    else:
        print("\nChristmas Quiz - Made by Jade (1) ✓")
    if pens == True:
        print("Penalty Shootout - Made by Musaab (2)")
    else:
        print("Penalty Shootout - Made by Musaab (2) ✓")
    if riddler == True:
        print("Riddler Room - Made by Adam (3)")
    else:
        print("Riddler Room - Made by Adam (3) ✓")
    if quiz == True:
        print("Quiz Master - Made by Andrew (4)")
    else:
        print("Quiz Master - Made by Andrew (4) ✓")
    print("\nQuit Game (5)")

    room_choice_input = typing_input(
        "\nChoose the number of which room you would like to play\n>> "
    )

    if room_choice_input.isdigit() == False:
        typing_print("\nThat doesn't seem to be a number, please try again\n")
        room_choice_menu()

    while int(room_choice_input) >= 1 or int(room_choice_input) <= 5:
        if int(room_choice_input) == 1 and xmas == True:
            xmas = False
            xmas_start()
        elif int(room_choice_input) == 2 and pens == True:
            pens = False
            penalties_start()
        elif int(room_choice_input) == 3 and riddler == True:
            riddler = False
            riddler_start()
        elif int(room_choice_input) == 4 and quiz == True:
            quiz = False
            quiz_start()
        elif int(room_choice_input) == 5:
            quit()
        elif int(room_choice_input) < 1 or int(room_choice_input) > 5:
            typing_print("\nThat room doesn't exist! Try again")
            room_choice_menu()
        break

    while xmas == False or pens == False or riddler == False or quiz == False:
        if int(room_choice_input) == 1:
            typing_print("\nYou've already attempted this room!\n")
            room_choice_menu()
        elif int(room_choice_input) == 2:
            typing_print("\nYou've already attempted this room!\n")
            room_choice_menu()
        elif int(room_choice_input) == 3:
            typing_print("\nYou've already attempted this room!\n")
            room_choice_menu()
        elif int(room_choice_input) == 4:
            typing_print("\nYou've already attempted this room!\n")
            room_choice_menu()


# Christmas Room


def xmas_start():
    typing_print(
        "\n                                                       It's nearly time for\n"
    )
    print(
        "                                                    *፠* C H R I S T M A S !!! *፠*\n"
    )
    print(" .")
    print(
        "   *               *                         .            *_ ==__                                                    *             *"
    )
    print(
        "     *   . /\       *   . /\         ___           *        ('')              *     *   . /\       *   . /\  "
    )
    print(
        "   .      /  \   *  .    /  \   * __|___|__               <(  . )>                 .     /  \   *  .    /  \   *"
    )
    print(
        '  *       /  \           /  \       (", )   ___    *    . _(_ :_)_           *           /  \           /  \          *   '
    )
    print(
        "    *    /    \    *    /    \     <(.  )> |___|           |    | .                     /    \    *    /    \ "
    )
    print(
        "'     *   `||` ..        `||` .. __(_:_ _)__ |_       . ============     *           *   `||` ..        `||` .     *         * \n"
    )
    typing_print(
        "                                                          \n Get these Christmas quiz questions right,\n"
    )
    typing_print(
        "                       ..and you will be free to leave this room and celebrate Christmas with your loved ones.\n\n"
    )
    typing_print(
        "                                                      ☆  Best of Luck  ☆   \n"
    )
    print(
        "                                                   From Santa's little elves' \n\n"
    )
    print("                                                                  .-(_) ")
    print("                                                               / _/      ")
    print(
        "                                                            .-'   \         "
    )
    print("                                                           /       '.   ")
    print(
        "                                                        ,-~--~-~-~-~-,      "
    )
    print(
        "                                                        {__.._...__..._}             ,888, "
    )
    print(
        "                                       ,888,          /\##'  6  6   '##/\          ,88' `88, "
    )
    print(
        "                                     ,88' '88,__     |(\`    (__)    `/)|     __,88'     `88 "
    )
    print(
        "                                    ,88'   .8(_ \_____\_    '----'    _/_____/ _)8.       8' "
    )
    print(
        "                                    88    (___)\ \      '-.__    __.-'      / /(___) "
    )
    print(
        "                                    88    (___)88 |          '--'          | 88(___) "
    )
    print(
        "                                    8'      (__)88,___/                \___,88(__) "
    )
    print(
        "                                              __`88,_/__________________\_,88`__ "
    )
    print(
        "                                             /    `88,       |88|       ,88'    \   "
    )
    print(
        "                                            /        `88,    |88|    ,88'        \ "
    )
    print(
        "                                           /____________`88,_\88/_,88`____________\ "
    )
    print(
        "                                          /88888888888888888;8888;88888888888888888\ "
    )
    print(
        "                                         /^^^^^^^^^^^^^^^^^^`/88\^^^^^^^^^^^^^^^^^^\ "
    )
    print(
        "                                      '---------------------' ' ' ' ---------------------'   \n\n"
    )

    def start_game():
        Start_question_1 = input(
            "Ready to start the game?        ፠.፠   Hit the 'ENTER' key Now!   ፠.፠ \n\n"
        )

        print(
            "                                                                ☆                "
        )
        print(
            "                                                    ☆       Question 1      ☆"
        )
        print(
            "                                                                ☆               \n"
        )

        typing_print(
            "                  The song 'All I want for Christmas,' by Mariah Carey has been one of the top Christmas hits for over 10 years. \n"
        )
        typing_print(
            "                                     Naming Mariah Carey the unofficial 'pop princess of Christmas'. \n"
        )

        typing_print(
            "                            The song broke Spotify's single-day record with 10.82 million plays in just 24 hours. \n\n"
        )

        typing_print(
            "                                      Q: In what year was the song officially released?\n"
        )

        Question_1 = ["1992", "2001", "1994", "1997?"]
        print(*Question_1, sep="\n")
        Answer_1 = input("\nType your answer here:\n")

        while Answer_1 != "1994":
            print("              Oh no! Sorry wrong answer, but give it another go.")
            print("                            ___           ___  ")
            print("                           (o o)         (o o)  ")
            print("                          (  V  ) oh no!(  V  ) ")
            print("                          --m-m-----------m-m-- \n\n")
            Answer_1 = input("Type your answer here:\n")

        if Answer_1 == "1994":
            print("")  # New line
            print("                                   ☆  YES correct! ☆ \n")
            print(
                "                               .     .  .    +     .      .          . "
            )
            print("                        .       .      .     #       .           . ")
            print(
                "                           .      .         ####            .      .      . "
            )
            print("                        .      .   ':. .:##''##:.#.:#'  .      . ")
            print("                            .      .  #### ### #### #  . ")
            print(
                "                         .       #:.    .:#'###''##:.    .:#'  .        .       . "
            )
            print(
                "                    .               #########'##########         .        . "
            )
            print(
                "                           .    '#:.   '#### '### '####'  .:#    .       . "
            )
            print(
                "                       .    .     '#####''#######''######'    .      . "
            )
            print(
                "                        .         .   .     000     .        .       . "
            )
            print(
                "                   .. .. ..................O000O........................ ...... ...\n\n"
            )

            next_question = input(
                "Ready for your next question?     ፠.፠   Hit the 'ENTER' key Now!   ፠.፠ \n\n"
            )

        print(
            "                                                                ☆                "
        )
        print(
            "                                                    ☆       Question 2      ☆"
        )
        print(
            "                                                                ☆               "
        )
        print("")  # space
        print(
            "                                                   *                       __o            * "
        )
        print(
            "                                          *                               /_| _       "
        )
        print(
            "                                             K  *     K                   O'_)/ \       * "
        )
        print(
            "                                            <')____  <')____   ____ __*   V   \  ) __  * "
        )
        print(
            "                                             \ ___ )--\ ___ )------( (    (___|__)/ /     * "
        )
        print(
            "                                           *  |   |    |   |      * \ \____| |___/ /  * "
        )
        print(
            "                                              |*  |    |   |Ho Ho Ho \____________/       * \n\n "
        )

        Question_1 = [
            " ",
            "                                Santa flies with 9 reindeer but only 8 pull the sleigh.",
            " ",
            "                            This reindeer flies solo because he is the smartest of all the deer.",
            " ",
            "                                   He has his own duties to perform",
            "                         like checking if all the children are sleeping,"
            " and so guides Santa around.",
            " ",
            "                                             Q.  Which reindeer is it?",
        ]
        print(*Question_1, sep="\n")
        print("")  # New Line
        Question_2 = [
            "Dasher",
            "Dancer",
            "Prancer",
            "Vixen",
            "Comet",
            "Blitzen",
            "Rudolph",
            "Donner",
            "Cupid",
        ]
        print(*Question_2, sep="\n")
        print("")  # New line
        Answer_2 = input("Type your answer here:").capitalize()
        print("")

        while Answer_2 != "Rudolph":
            print("")  # New Line
            print("             Oh no, sorry wrong answer. But try again!")
            print("                            ___           ___  ")
            print("                           (o o)         (o o)  ")
            print("                          (  V  ) oh no!(  V  ) ")
            print("                          --m-m-----------m-m-- \n")
            Answer_2 = input("Type your answer here:").capitalize()
            print("")
        if Answer_2 == "Rudolph":
            print("                   ☆  YES correct! ☆\n")
            next_question = input(
                "Ready for your next question?       ፠.፠   Hit the 'ENTER' key Now!   ፠.፠ \n\n"
            )

        print(
            f"                                                                ☆                "
        )
        print(
            "                                                    ☆       Question 3     ☆"
        )
        print(
            "                                                                 ☆              \n\n"
        )
        typing_print(
            "             Q. Using the same list of deer from the list above, \n which Reindeer is Rudolph's Dad? \n\n"
        )
        typing_print(
            "                                                ...(pst, by the way).. \n"
        )
        typing_print(
            "                              You only have 3 Chances to get this right, before this game will restart! \n"
        )
        print(*Question_2, sep="\n")

        chances = 2
        Answer_3 = input("Type your answer here: \n").capitalize()

        while Answer_3 != "Donner" and chances > 0:
            print(
                "                Oh no! Sorry wrong answer and you have lost 1 chance!"
            )
            print("                         But try again. You can do this! \n\n")
            chances -= 1
            Answer_3 = input("Type your answer here:").capitalize()

        if Answer_3 == "Donner":
            print(
                "                                                ☆  YES correct! ☆ \n"
            )
            print("")
            print(
                "                                                                                    * "
            )
            print(
                "                     *                                                           * "
            )
            print("                                    *          /)___________/) ")
            print(
                "                                              / ,--o ______/ /       *         * "
            )
            print(
                "                                            / /__\       / |               * "
            )
            print("                        *                  /  {''}]     /  | ")
            print(
                "                                           .--{~`/--.   )  \__              * "
            )
            print("                                          /   { }    \ /     / ")
            print("                                *         /_/   ~  /_//'  / / ")
            print("                                     .-==w======w|     / /  ")
            print("                                    /  |-(__)(__)/__| /_/ ")
            print("                                   /   | \  |\  |__ ) / ")
            print(
                "                                  /   / //_/ /_/   / /              * "
            )
            print("                     *           /  _/_/________  / / ")
            print("                                /  (            (/ / ")
            print("                               /    \==========   / ")
            print(
                "                           */      (___________/                    * "
            )
            print("                     \/ \/         \/  \/     _/ /    * ")
            print("                      |\/|   /      \\_/     \\_/ ")
            print("                      .. | _/________ |\/|    / ")
            print("                     /_/|_\/          .. |  _/ ")
            print("                      __/ )|         /_/|_\// ")
            print(
                "                    VV--   \         __/ )|             *               * "
            )
            print("                       |_   |       VV--   \ ")
            print("                      / / / )          |_   |               * ")
            print("                      |_|_/\_ \____    / / / ) ")
            print("                      ////  '-----`  |_|_/\_ \____ ")
            print("                                   ////  '-----`  \n\n")
            next_question = input(
                "Ready for your next question?       ፠.፠   Hit the 'ENTER' key Now!   ፠.፠ \n"
            )

        else:
            print(
                "                                   Oh no! Looks like you ran out of chances. \n\n"
            )
            print("                                            _____________,--, ")
            print(
                "                                              | | | | | | |/ .-.\   HANG IN THERE "
            )
            print(
                "                                          |_|_|_|_|_|_/ /   `.      SANTA "
            )
            print("                                          |_|__|__|_; |      \ ")
            print("                                          |___|__|_/| |     .'`} ")
            print("                                          |_|__|__/ | |   .'.'`\ ")
            print(
                "                                         |__|__|/  ; ;  / /    \.-^-. "
            )
            print(
                "                                           ||__|_;   \ \  ||    /`___. \ "
            )
            print(
                "                                           |_|___/\  /;.`,\\   {_'___.;{} "
            )
            print(
                "                                           |__|_/ `;`__|`-.;|  |C` e e`\ "
            )
            print(
                "                                          |___`L  \__|__|__|  | `'-o-' } "
            )
            print(
                "                                          ||___|\__)___|__||__|\   ^  /`\ "
            )
            print(
                "                                          |__|__|__|__|__|_{___}'.__.`\_.'} "
            )
            print(
                "                                          ||___|__|__|__|__;\_)-'`\   {_.-; "
            )
            print(
                "                                          |__|__|__|__|__|/` (`\__/     '-' "
            )
            print("                                          |_|___|__|__/`      | ")
            print(
                "                                  -   ---|__|___|__/`         \------------------- "
            )
            print(
                "                                     -.__.-.|___|___;`            |.__.-.__.-.__.-.__ "
            )
            print(
                "                                      |     |     ||             |  |     |     | "
            )
            print(
                "                                     -' '---' '---' \             /-' '---' '---' '-- "
            )
            print(
                "                                       |     |    '.        .' |     |     |     | "
            )
            print(
                "                                   '---' '---' '---' `-===-'`--' '---' '---' '---' \n\n"
            )
            print("                       \n\n This game will restart. \n")
            start_game()

    start_game()

    print(
        f"                                                               ☆                "
    )
    print(
        "                                                    ☆       Question 4     ☆"
    )
    print(
        "                                                                ☆               \n"
    )

    typing_print(
        "             Q. Gingerbread men were eaten by single women in Tudor times in the hope it would help them find a husband? \n\n"
    )
    print(
        "                      *              ,-.       *          ,-.         *        ,-.             * "
    )
    print(
        "                                   _(*_*)_              _(*_*)_              _(*_*)_                   . "
    )
    print(
        "                      .           (_  o  _)   *        (_  o  _)      .     (_  o  _)           * "
    )
    print(
        "                              *     / o \         .      / o \     *          / o \                    * "
    )
    print(
        "                          *        (_/ \_)              (_/ \_)      .       (_/ \_)                   . \n"
    )

    typing_print(
        "                                                         Is this True or False?. \n\n"
    )

    def question_4():
        Answer_4 = input("Type your answer here: \n").capitalize()
        if Answer_4 == "True":
            print("                               ☆  Yes, it is in fact true! ☆")
            print(
                "                          \n   .     .  .    +     .      .          . "
            )
            print("                        .       .      .     #       .           . ")
            print(
                "                           .      .         ####            .      .      . "
            )
            print("                        .      .   ':. .:##''##:.#.:#'  .      . ")
            print("                            .      .  #### ### #### #  . ")
            print(
                "                         .       #:.    .:#'###''##:.    .:#'  .        .       . "
            )
            print(
                "                    .               #########'##########         .        . "
            )
            print(
                "                           .    '#:.   '#### '### '####'  .:#    .       . "
            )
            print(
                "                       .    .     '#####''#######''######'    .      . "
            )
            print(
                "                        .         .   .     000     .        .       . "
            )
            print(
                "                   .. .. ..................O000O........................ ...... ..."
            )
            final_question_intro = [
                " ",
                "Are you ready for your final question? \n Get the next question right and you will be free to leave this room and celebrate Christmas with your friends and family.\n\n       ፠.፠   Hit the 'ENTER' key Now!   ፠.፠",
            ]
            print(*final_question_intro, sep="\n")

        else:
            print(
                "                           \n Nope, that is actually the wrong answer! Please try again.\n"
            )
            question_4()

    question_4()

    print(
        f"                                                               ☆                "
    )
    print(
        "                                                    ☆       Question 5      ☆"
    )
    print(
        "                                                                ☆               \n\n"
    )

    typing_print(
        "                                         It might be illegal to drink and drive \n"
    )
    typing_print(
        "      but it is customary to leave some treats out on Christmas eve for Santa and his reindeer, to help him along his merry way. \n\n"
    )

    print(
        "                         Q. Which alcoholic beverage should you leave out for Santa during his peak time of delivery?"
    )

    Question_5 = [
        "Gin & Tonic",
        "Budweiser",
        "Mulled Wine",
        "Cheeky Vimto",
        "Espresso Martini",
        "Sherry",
        "Port",
        "Guinness",
    ]
    print(*Question_5, sep="\n")
    Answer_5 = input("\nType your answer here: \n\n").capitalize()

    while Answer_5 != "Sherry":
        print(
            "              Nope that is the wrong answer, would you like to go again?"
        )
        print("                            ___               ___  ")
        print("                           (o o)             (o o)  ")
        print("                          (  V  )  Oh dear! (  V  ) ")
        print("                          --m-m-------------- m-m-- \n")

        Answer_5 = input("Type your answer here: \n\n").capitalize()

    if Answer_5 == "Sherry":
        print("")  # Space
        end_xmas_game = [
            "                              Yes, you did it!                        ",
            "  ",
            "                    ☆ .☆ .☆   GAME ROOM COMPLETE  ☆ .☆ .☆",
            "  ",
            "You completed all the questions in this room!",
            " ",
            "The door is now open for you to go and collect your presents from Santa!",
        ]
        print(*end_xmas_game, sep="\n\n")

    print("                                   |,\/,| |[_' |[_]) |[_]) \\//  ")
    print("                                   ||\/|| |[_, ||'\, ||'\,  ||")
    print("                             ")
    print(
        "                                         ___ __ __ ____  __  __  ____  _  _    __    __"
    )
    print(
        "                                        // ' |[_]| |[_]) || ((_' '||' |,\/,|  //\\  ((_'"
    )
    print(
        "                                        \\_, |[']| ||'\, || ,_))  ||  ||\/|| //``\\ ,_))"
    )
    print(
        "                                                                                            "
    )
    print("                             ")
    print("                                                                      ,;7,")
    print("                                                                    _ ||:|,")
    print("                                                  _,---,_           )'  '|")
    print("                                                .'_.-.,_ '.         ',')  j")
    print("                                               /,'   ___}  \        _/   /")
    print("                                   .,         ,1  .''  =\ _.''.   ,`';_ |")
    print("                                 .'  \        (.'T ~, (' ) ',.'  /     ';',")
    print("                                 \   .\(\O/)_. \ (    _Z-'`>--, .'',      ;")
    print("                                  \  |   I  _|._>;--'`,-j-'    ;    ',  .'")
    print("                                 __\_|   _.'.-7 ) `'-' '       (      ;'")
    print("                               .'.'_.'|.' .'   \ ',_           .'\   /")
    print("                               | |  |.'  /      \   \          l  \ /")
    print("                               | _.-'   /        '. ('._   _ ,.'   \i")
    print("                             ,--' ---' / k  _.-,.-|__L, '-' ' ()    ;")
    print("                              '._     (   ';   (    _-}             |")
    print("                               / '     \   ;    ',.__;         ()   /")
    print("                              /         |   ;    ; ___._._____.: :-j")
    print("                             |           \,__',-' ____: :_____.: :-\ ")
    print("                             |               F :   .  ' '        ,  L")
    print("                             ',             J  |   ;             j  |")
    print("                               \            |  |    L            |  J")
    print("                                ;         .-F  |    ;           J    L")
    print("                                 \___,---' J'--:    j,---,___   |_   |")
    print("                                          |   |'--' L       '--| '-'|")
    print("                                            '.,L     |----.__   j.__.'")
    print("                                             | '----'   |,   '-'  }")
    print("                                             j         / ('-----';') ")
    print("                                            { '---'--;'  }       |")
    print("                                            |        |   '.----,.'")
    print("                                            ',.__.__.'    |=, _/")
    print("                                             |     /      |    '.")
    print("                                             |'= -x       L___   '--,")
    print("                                             L   __\          '-----'")
    print("                                              '.____)")

    def end():
        end_input = typing_input("Play again (1) or exit room? (2)\n>> ")
        if end_input == "1":
            riddler_start()
        elif end_input == "2":
            room_choice_menu()
        else:
            typing_print("That option doesn't seem to exist, try again")
            end()

    end()


# Penalties Room


class TxtQuestions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class McQuestions:
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options


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
    TxtQuestions(
        "How often is the World Cup held?\n>> ", ["every 4 years", "1 every 4 years"]
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


def penalties_start():
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
        print("Top right corner (5)")

        shot_placement_input = input(
            "\nChoose which number you'd like to shoot at\n>> "
        )

        if shot_placement_input.isdigit() == False:
            typing_print("\nThat doesn't seem to be a number mate, try agai7n\n")
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
                typing_print("\nYou can't shoot there mate, try again")
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
            question = f"{mc_questions_list[random_qnum].question}\n{mc_questions_list[random_qnum].options}\nPick the number\n\n>> "
        input_ans = typing_input(f"\n{question}").lower()
        answer_check()

    def answer_check():
        global user_score, keeper_score, txt_questions_list, mc_questions_list

        random_score_chance = random.randint(1, 10)

        if input_ans == "" or input_ans.isspace() == True:
            if random_typeofq == 0:
                typing_print("You didn't even kick the ball!\n")
                typing_print(
                    f"Correct answer was {txt_questions_list[random_qnum].answer}\n"
                )
                score_check()
                txt_questions_list.pop(random_qnum)
            elif random_typeofq == 1:
                typing_print("You didn't even kick the ball!\n")
                typing_print(
                    f"Correct answer was {mc_questions_list[random_qnum].answer}\n"
                )
                score_check()
                mc_questions_list.pop(random_qnum)
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
                    typing_print(
                        f"{shot_placement}Score {user_score} - {keeper_score}\n"
                    )
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
                    keeper_score += 1
                    typing_print(
                        f"\nYou've had a howler, the ball is in row Z!\nCorrect answer was {txt_questions_list[random_qnum].answer}\n\n"
                    )
                    typing_print(f"Score {user_score} - {keeper_score}\n")
                    txt_questions_list.pop(random_qnum)
                    score_check()
        elif random_typeofq == 1:
            if (
                input_ans == mc_questions_list[random_qnum].answer
                and input_ans.isdigit() == True
                and int(input_ans) > 0
                and int(input_ans) <= 3
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
                    typing_print(
                        f"{shot_placement}Score {user_score} - {keeper_score}\n"
                    )
                    score_check()
                elif random_score_chance > 8:

                    keeper_score += 1
                    typing_print(
                        f"\nGreat shot, but the keeper's on fire! Penalty saved!\nScore {user_score} - {keeper_score}\n"
                    )
                    mc_questions_list.pop(random_qnum)
                    score_check()
            else:
                if (
                    input_ans.isdigit() == False
                    or int(input_ans) < 1
                    or int(input_ans) > 3
                ):
                    keeper_score += 1
                    typing_print(
                        f"\nThat isn't an option mate, you've had a nightmare!\nCorrect answer was {mc_questions_list[random_qnum].answer}\n\n"
                    )
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
                    keeper_score += 1
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
            time.sleep(1.25)
            loss_screen()
        elif user_score == 5 and keeper_score < 5:
            time.sleep(1.5)
            win_screen()

    def loss_screen():
        typing_print(
            "\n\nYou fell under the pressure and failed to beat the keeper 5 times...\nYou failed your country\n\n"
        )
        end()

    def win_screen():
        typing_print(
            "\n\nYOU HAVE WON THE WORLD CUP, YOU'RE IN THE HISTORY BOOKS!\n\n\n"
        )
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
            room_choice_menu()
        else:
            typing_print("That option doesn't exist, please try again")
            end()

    start_game()


# Riddler Room

lives_q1 = 3
lives_q2 = 3
lives_q3 = 3
lives_q4 = 3
lives_q5 = 3


def riddler_start():
    typing_print("\n\nWelcome to The Riddler Room\n")
    typing_print(
        "\nIn this room you will have 5 riddles to solve, to escape the Riddle Room\n"
    )
    typing_print("\nYou will have 3 lives per riddle\n")
    typing_print("\nGood Luck, Gotham Needs You!!\n")

    def question_one():
        global lives_q1
        typing_print(
            "\nRiddle 1:- I can be cracked. I can be made. I can be told. I can be played. What am I?\n"
        )
        answer = input("\n\nType your answer here: ").lower()
        if answer == "a joke" or answer == "joke":
            typing_print("\nYou are correct\n\n")
        else:
            lives_q1 -= 1
            if lives_q1 >= 1:
                typing_print("\nThat is incorrect, try again\n\n")
                typing_print(f"\nYou have {str(lives_q1)} lives left\n")
                question_one()
            else:
                typing_print("\nThat is incorrect, you have 0 lives.\n")

    question_one()

    def question_two():
        global lives_q2
        typing_print(
            "\nRiddle 2:- What English word has three consecutive double letters?\n"
        )
        answer = input("\n\nType your answer here: ").lower()
        if answer == "a bookkeeper" or answer == "bookkeeper":
            typing_print("\nYou are correct\n\n")
        else:
            lives_q2 -= 1
            if lives_q2 >= 1:
                typing_print("\nThat is incorrect, try again\n\n")
                typing_print(f"\nYou have {str(lives_q2)} lives left\n")
                question_two()
            else:
                typing_print("\nThat is incorrect, you have 0 lives.\n")

    question_two()

    def question_three():
        global lives_q3
        typing_print(
            "\nRiddle 3:- I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?\n"
        )
        answer = input("\n\nType your answer here: ").lower()
        if answer == "a map" or answer == "map":
            typing_print("\nYou are correct\n\n")
        else:
            lives_q3 -= 1
            if lives_q3 >= 1:
                typing_print("\nThat is incorrect, try again\n\n")
                typing_print(f"\nYou have {str(lives_q3)} lives left\n")
                question_three()
            else:
                typing_print("\nThat is incorrect, you have 0 lives.\n")

    question_three()

    def question_four():
        global lives_q4
        typing_print(
            "\nRiddle 4:- What Is The Beginning Of Eternity, The End Of Time And Space, The Beginning Of Every End, And The End Of Every Race?\n"
        )
        answer = input("\n\nType your answer here: ").lower()
        if (
            answer == "The letter e"
            or answer == "The letter E"
            or answer == "E"
            or answer == "e"
        ):
            typing_print("\nYou are correct\n\n")
        else:
            lives_q4 -= 1
            if lives_q4 >= 1:
                typing_print("\nThat is incorrect, try again\n\n")
                typing_print(f"\nYou have {str(lives_q4)} lives left\n")
                question_four()
            else:
                typing_print("\nThat is incorrect, you have 0 lives.\n")

    question_four()

    def question_five():
        global lives_q5
        typing_print(
            "\nRiddle 5:-What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats?\n"
        )
        answer = input("\n\nType your answer here: ").lower()
        if answer == "a river" or answer == "river":
            typing_print("\nYou are correct\n\n")
        else:
            lives_q5 -= 1
            if lives_q5 >= 1:
                typing_print("\nThat is incorrect, try again\n\n")
                typing_print(f"\nYou have {str(lives_q5)} lives left\n")
                question_five()
            else:
                typing_print("\nThat is incorrect, you have 0 lives.\n")

    question_five()

    def end():
        end_input = typing_input("Play again (1) or exit room? (2)\n>> ")
        if end_input == "1":
            riddler_start()
        elif end_input == "2":
            room_choice_menu()
        else:
            typing_print("That option doesn't seem to exist, try again")
            end()

    end()


# Quiz Room

points_bal = 0
points_max = 0


def quiz_start():
    def typing_print_fast(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)

    def welcome_part1():
        typing_print("\nWELCOME TO THE QUIZ MASTER'S ROOM\n\n")
        typing_print("WILL YOU BEAT THE QUIZ MASTER?\n\n")
        typing_print(
            "THE QUIZ MASTER WAS BORN FROM THE PRIME ORDEAL SOUP FOLLOWING THE BIG BANG 13.6 BILLION YEARAS AGO!\n\n"
        )
        typing_print("HE HAS ALL OF THE KNOWLEDGE IN THE UNIVERSE!\n\n")
        typing_print(
            "WITHIN HIS REALM, FOR THOSE SPECIES THAT HAVE EATEN FROM THE APPLE OF KNOWLEDGE, THEY MUST PROVE THEIR WORTH OR ELSE!\n\n"
        )
        typing_print("WILL YOU BEAT THE QUIZ MASTER AND SAVE THE HUMAN RACE?\n\n")
        typing_print(
            "OR WILL HE PROVE WE ARE UNWORTHY TO EXIST AND DESTROY THE WHOLE EARTH?\n\n"
        )
        typing_print(
            "THE FUTURE OF THE EARTH AND ALL LIVING BEINGS ON IT, IS IN YOUR HANDS.\n\n"
        )
        time.sleep(3)

    welcome_part1()

    def quiz_master():
        typing_print("              THE QUIZ MASTER              \n")
        typing_print_fast(
            r'''
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
        typing_print(
            "Human. This is a general knowledge quiz and the future of your Earth depends on it.\n\n"
        )
        typing_print(
            "Do not think that I, The Quiz Master, will hesitate to end the existence of everything on your fragile planet.\n\n"
        )
        typing_print(
            "Accurately answer as many questions as possible to earn points.\n\n"
        )
        typing_print(
            "To beat I, The Quiz Master, you must score 14 or more points from a maximum of 20 available points.\n\n"
        )
        typing_print(
            "Prove to me, that you are worthy of an intellectual existence.\n\n"
        )
        time.sleep(3)

    def continue_exit():
        typing_print(
            "\nWILL YOU ACCEPT THE INVITATION TO SAVE THE EARTH AND BECOME A HERO?\n\n"
        )
        answer = input("Please respond with 'Y' to continue or 'N' to exit? -> ")
        if answer == "Y" or answer == "y":
            welcome_part2()
        elif answer == "N" or answer == "n":
            room_choice_menu()
        else:
            print(
                "\nThat is an incorrect response. Please specify 'Y' to continue or 'N' to exit.\n"
            )
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

    def question1():
        global points_bal
        global points_max
        question_num = "One"
        subject = "Biology"
        question_text = "In which part of the body would you find your funny bone?"
        points = 1
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        options = ["1 - Mouth, 2 - Head, 3 - Elbow, 4 - Knee"]
        print(f"Please select one from the following options:\n\n    {options}\n")
        answer = input(
            "What is the correct answer? Please type the number associated to your selection ANSWER -> "
        )
        correct_answer = "3"
        if answer == correct_answer:
            points_bal += points
            points_max += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        elif answer == "1" or answer == "2" or answer == "3":
            points_max += points
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}."
            )
        else:
            print(
                "\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n"
            )
            time.sleep(3)
            question1()

    question1()
    time.sleep(5)

    def question2():
        global points_bal
        global points_max
        question_num = "Two"
        subject = "History"
        question_text = (
            "How many wives did King Henry The 8th of England have during his lifetime?"
        )
        points = 2
        points_max += points
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        answer = input(
            "Please specify an integer / number and NOT a word / string. ANSWER -> "
        )
        correct_answer = "6"
        if answer == correct_answer:
            points_bal += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            answer != correct_answer
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )

    question2()
    time.sleep(5)

    def question3():
        global points_bal
        global points_max
        question_num = "Three"
        subject = "Sport"
        question_text = (
            "In which year did the England football team win their first World Cup?"
        )
        points = 1
        points_max += points
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        answer = input(
            "Please specify an integer / number that is 4 characters long e.g. 1945. ANSWER -> "
        )
        correct_answer = "1966"
        if answer == correct_answer:
            points_bal += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            answer != correct_answer
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )

    question3()
    time.sleep(5)

    def question4():
        global points_bal
        global points_max
        question_num = "Four"
        subject = "Geography"
        question_text = "In which body of water would you find the Galapagos Islands?"
        points = 2
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        options = [
            "1 - Atlantic Ocean, 2 - Indian Ocean, 3 - Pacific Ocean, 4 - Gulf Of Mexico"
        ]
        print(f"Please select one from the following options:\n\n    {options}\n")
        answer = input(
            "What is the correct answer? Please type the number associated to your selection ANSWER -> "
        )
        correct_answer = "3"
        if answer == correct_answer:
            points_bal += points
            points_max += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        elif answer == "1" or answer == "2" or answer == "3":
            points_max += points
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            print(
                "\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n"
            )
            time.sleep(3)
            question4()

    question4()
    time.sleep(5)

    def question5():
        global points_bal
        global points_max
        question_num = "Five"
        subject = "Mathematics"
        question_text = "What is the answer to the equation 110 x 55 = ?"
        points = 3
        points_max += points
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        answer = input("Please specify an integer / number. ANSWER -> ")
        correct_answer = "6050"
        if answer == correct_answer:
            points_bal += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            answer != correct_answer
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )

    question5()
    time.sleep(5)

    def question6():
        global points_bal
        global points_max
        question_num = "Six"
        subject = "Economics"
        question_text = "You have £2,000 in cash and you keep hold of it under your mattress.\n\nIn one year, the government reports a consumer price index inflation rate of 12%.\n\n“In real terms”, in todays' money, how much buying power does your £2,000 have when the government makes the announcement?"
        points = 3
        points_max += points
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        answer = input(
            "Please specify an integer / number without the £ symbol e.g. 1234. ANSWER -> "
        )
        correct_answer = "1760"
        if answer == correct_answer:
            points_bal += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            answer != correct_answer
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nYou scored 0 points.\n\nThe correct answer is {correct_answer}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )

    question6()
    time.sleep(5)

    def question7():
        global points_bal
        global points_max
        question_num = "Seven"
        subject = "Observation"
        question_text = "Do I, The Quiz Master, have any bad habits?"
        points = 1
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        options = ["1 - Alcohol, 2 - Smoking, 3 - Swearing, 4 - Flashing"]
        print(f"Please select one from the following options:\n\n    {options}\n")
        answer = input(
            "What is the correct answer? Please type the number associated to your selection ANSWER -> "
        )
        correct_answer = "2"
        if answer == correct_answer:
            points_bal += points
            points_max += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        elif answer == "1" or answer == "3" or answer == "4":
            points_max += points
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            print(
                "\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n"
            )
            time.sleep(3)
            question7()

    question7()
    time.sleep(5)

    def question8():
        global points_bal
        global points_max
        question_num = "Eight"
        subject = "Mythology"
        question_text = "In Greek Mythology, which creature protects the entrance to the Underworld?"
        points = 2
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        options = ["1 - Hades, 2 - Cerebus, 3 - Poseidon, 4 - Medusa"]
        print(f"Please select one from the following options:\n\n    {options}\n")
        answer = input(
            "What is the correct answer? Please type the number associated to your selection ANSWER -> "
        )
        correct_answer = "2"
        if answer == correct_answer:
            points_bal += points
            points_max += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        elif answer == "1" or answer == "2" or answer == "3":
            points_max += points
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            print(
                "\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n"
            )
            time.sleep(3)
            question8()

    question8()
    time.sleep(5)

    def question9():
        global points_bal
        global points_max
        question_num = "Nine"
        subject = "Movies"
        question_text = "Which movie is the highest grossing movie of all time?"
        points = 2
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        options = ["1 - Wiazard Of Oz, 2 - Jurassic World, 3 - Titanic, 4 - Avatar"]
        print(f"Please select one from the following options:\n\n    {options}\n")
        answer = input(
            "What is the correct answer? Please type the number associated to your selection ANSWER -> "
        )
        correct_answer = "4"
        if answer == correct_answer:
            points_bal += points
            points_max += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        elif answer == "1" or answer == "2" or answer == "3":
            points_max += points
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            print(
                "\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n"
            )
            time.sleep(3)
            question9()

    question9()
    time.sleep(5)

    def question10():
        global points_bal
        global points_max
        question_num = "Ten"
        subject = "Enviromental Science"
        question_text = "For the same mass of gas, which of these gases has the greatest impact on climate change and increasing temperatues?"
        points = 3
        question = f"\n\nQuestion - {question_num}\n\nSubject - {subject}\n\nPoints Available - {points}\n\nQUESTION -> {question_text}\n"
        print(question)
        options = ["1 - Carbon Dioxide, 2 - Methane, 3 - Oxygen, 4 - Nitrogen"]
        print(f"Please select one from the following options:\n\n    {options}\n")
        answer = input(
            "What is the correct answer? Please type the number associated to your selection ANSWER -> "
        )
        correct_answer = "2"
        if answer == correct_answer:
            points_bal += points
            points_max += points
            print(
                f"\nCORRECT. WELL DONE YOU.\n\nNumber of points won is {points}.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        elif answer == "1" or answer == "3" or answer == "4":
            points_max += points
            print(
                f"\nINCORRECT. OOPSY DAISY.\n\nThe correct answer is {correct_answer}.\n\nYou scored 0 points.\n\nYour total points achieved is {points_bal} from a maximum available of {points_max}.\n"
            )
        else:
            print(
                "\nThat is an incorrect response. Next time please specify an integer between 1 and 4.\n"
            )
            time.sleep(3)
            question10()

    question10()
    time.sleep(3)

    print(
        f"Your final points tally is {points_bal}. But was it enough to beat The Quiz Master?"
    )
    time.sleep(3)

    def end_of_game():
        if points_bal >= 14:
            print("\n\nCONGRATULATIONS! WOO HOO!\n\n")
            typing_print("\nYOU BEAT THE DASTARDLY QUIZ MASTER!\n\n")
            typing_print("\nYOU HAVE SAVED THE EARTH AND ALL LIVING THINGS ON IT!\n\n")
            typing_print(
                "\nYOU ARE A HERO AND YOUR NAME WILL BE SANG THROUGHOUT THE AGES!\n\n"
            )
            time.sleep(2)
            typing_print_fast(
                r"""
            
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.
        
        """
            )
            typing_print_fast(
                r"""        
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
        """
            )
            time.sleep(2)
            typing_print("\nYou escaped The Quiz Master's Room victorious!\n\n")
            time.sleep(3)

        elif points_bal <= 13:
            print("\n\nOH NO! WHAT WENT WRONG?\n")
            typing_print("\n# THE QUIZ MASTER WAS TOO GOOD FOR YOU!\n\n")
            typing_print("\nTHE EARTH WILL PERISH AND EVERYTHING IS OVER!\n\n")
            typing_print("\nGOODBYE... FOREVER!\n\n")
            time.sleep(2)
            typing_print_fast(
                r"""
            
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.
        
        """
            )
            print("\n.....5.....\n\n")
            time.sleep(1)
            print("\n.....4.....\n\n")
            time.sleep(1)
            print("\n.....3.....\n\n")
            time.sleep(1)
            print("\n.....2.....\n\n")
            time.sleep(1)
            print("\n.....1.....\n\n")
            print(
                r"""
        
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.
        
        """
            )
            time.sleep(1)
            typing_print_fast("\n.....BOOM....\n\n")
            print(
                r"""
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
            typing_print(
                "\nYou failed to escape The Quiz Master's Room victorious.\n\n"
            )
            time.sleep(3)

    end_of_game()

    def end():
        end_input = typing_input("Play again (1) or exit room? (2)\n>> ")
        if end_input == "1":
            riddler_start()
        elif end_input == "2":
            room_choice_menu()
        else:
            typing_print("That option doesn't seem to exist, try again")
            end()

    end()


main_game()
