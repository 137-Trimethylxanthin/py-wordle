"""
Wordle spiel mit Python ohen pygame oder tkinter
in diesem spiel hast du 6 versuche um das wort zu erraten das wort hat 5 buchstaben
wenn ein buchstabe in dem wort vorhanden ist wird er gelb hinterlegt
wenn ein buchstabe auf der richtigen Stelle ist, wird er grün hinterlegt
wenn ein buchstabe nicht in dem wort vorhanden ist, wird er grau hinterlegt
"""

import os
import random
import time
from msvcrt import getch

def key_press_detection():
    k: str = getch()
    if k == b'\x08':
        k = "backspace"
    else:
        k = str(k, "utf-8")
    return k


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def confirm_enter():
    input("")


def greeting():
    clear()
    print("Willkommen zum Wordle Spiel")
    print("Du hast 6 Versuche um das Wort zu erraten")
    print("Das Wort hat 5 Buchstaben")
    print("Wenn ein Buchstabe in dem Wort vorhanden ist wird er gelb hinterlegt")
    print("Wenn ein Buchstabe auf der richtigen Stelle ist, wird er grün hinterlegt")
    print("Wenn ein Buchstabe nicht in dem Wort vorhanden ist, wird er grau hinterlegt")
    print("Hast du alles verstanden? Wenn ja drücke Enter")
    input()
    clear()
    print("Dann fangen wir mal an")
    print("hab spaß")


def check_if_all_correct() -> bool:
    columns: int = infos_os("c")
    lines: int = infos_os("l")

    if columns >= 200 and lines >= 55:
        return True
    else:
        print(f"zurzeit größe ist, Columns: {columns} Lines: {lines}")
        return False


def word(word: str):
    """
    ╔═══════╗
    ║       ║
    ║       ║
    ║       ║
    ╚═══════╝
    """
    w: list = []
    tc: int = infos_os("c")
    for i in range(len(word)):
        w.append(word[i])
    print()
    print(" " * (tc // 2 - 37) + f"╔═══════╗" + " " * 5 + "╔═══════╗" + " " * 5 + "╔═══════╗" + " " * 5 + "╔═══════╗" + " " * 5 + "╔═══════╗")
    print(" " * (tc // 2 - 37) + f"║       ║" + " " * 5 + "║       ║" + " " * 5 + "║       ║" + " " * 5 + "║       ║" + " " * 5 + "║       ║")
    print(" " * (tc // 2 - 37) + f"║   {w[0]}   ║" + " " * 5 + f"║   {w[1]}   ║" + " " * 5 + f"║   {w[2]}   ║" + " " * 5 + f"║   {w[3]}   ║" + " " * 5 + f"║   {w[4]}   ║")
    print(" " * (tc // 2 - 37) + f"║       ║" + " " * 5 + "║       ║" + " " * 5 + "║       ║" + " " * 5 + "║       ║" + " " * 5 + "║       ║")
    print(" " * (tc // 2 - 37) + f"╚═══════╝" + " " * 5 + "╚═══════╝" + " " * 5 + "╚═══════╝" + " " * 5 + "╚═══════╝" + " " * 5 + "╚═══════╝")


def draw(l: list) -> None:
    tc_size: int = infos_os("c")
    one: str = ""
    tow: str = ""
    three: str = ""
    four: str = ""
    five: str = ""
    six: str = ""

    for i in range(30):
        if i < 5:
            one += l[i]
        elif i < 10:
            tow += l[i]
        elif i < 15:
            three += l[i]
        elif i < 20:
            four += l[i]
        elif i < 25:
            five += l[i]
        elif i < 30:
            six += l[i]

    clear()
    print(" " * (tc_size // 2 - 13) + "Py Wordl v0.2")
    print()
    print()
    word(one)
    print()
    print()
    word(tow)
    print()
    print()
    word(three)
    print()
    print()
    word(four)
    print()
    print()
    word(five)
    print()
    print()
    word(six)


def tui():
    guess: list = []
    count: int = 0
    i_will_die: bool = True
    for i in range(30):
        guess.append(" ")
    clear()
    correct: bool = check_if_all_correct()
    while correct == False:
        print("du brauchst 200 Collumns, und 55 Lines ")
        print("Weiter with enter")
        input()
        clear()
        correct = check_if_all_correct()
    draw(guess)
    while i_will_die:
        k = writing()
        print(k, "done writing", count)
        if k == "backspace":
            count -= 1
            guess[count] = " "
            print("")
        elif k == "enter" and count > 5:
            i_will_die = False
        elif k == "enter":
            print("enter")
        elif k == "space":
            print("space")
            guess[count] = " "
            count += 1
        else:
            print("else")
            guess[count] = k
            count += 1
        draw(guess)
        print(k, ":done drawnig", count, ":count", )

    print("you win")
    input()


def writing():
    k = key_press_detection()
    return k


def infos_os(need: str):
    match need:
        case "c":
            return os.get_terminal_size().columns
        case "l":
            return os.get_terminal_size().lines
        case _:
            print("dosent exist")


if __name__ == "__main__":
    greeting()
    tui()
