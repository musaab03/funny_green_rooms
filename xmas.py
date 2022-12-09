import sys, time


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


print(
    f"                                                               ☆                "
)
print("                                                    ☆       Question 4     ☆")
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
        print(*final_question_intro, sep="\n")

    else:
        print(
            "                           \n Nope, that is actually the wrong answer! Please try again.\n"
        )
        question_4()


question_4()
