import sys, time


def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typing_input(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


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
    Answer_4 = input("Type your answer here: \n").capitalize()

    if Answer_4 != "True":
        print(
            "                           Nope, that is actually the wrong answer! Please try again.\n"
        )
        Answer_4 = input("Type your answer here: \n").capitalize()

    elif Answer_4 == "True":
        print("                               ☆  Yes, it is in fact true! ☆")
        print("                          \n   .     .  .    +     .      .          . ")
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
        print("                       .    .     '#####''#######''######'    .      . ")
        print("                        .         .   .     000     .        .       . ")
        print(
            "                   .. .. ..................O000O........................ ...... ..."
        )
        final_question_intro = [
            " ",
            "Are you ready for your final question? \n Get the next question right and you will be free to leave this room and celebrate Christmas with your friends and family. \n       ፠.፠   Hit the 'ENTER' key Now!   ፠.፠",
        ]
        typing_print(*final_question_intro, sep="\n\n")

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
