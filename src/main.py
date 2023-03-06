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

if os.name == "nt":
    from msvcrt import getch
else:
    from getch import getch


def choose_word() -> list:
    w: str = ""
    l: list = []
    words: list = ["Abend", "Birne", "Chaos", "Droge", "Eiche", "Fahne", "Gans", "Haube", "Ideen", "Junge", "Kabel",
                   "Lampe", "Mauer", "Nadel", "Ortse", "Pfote", "Quark", "Rente", "Sonne", "Tiger"]
    w = random.choice(words)
    for i in range(len(w)):
        l.append(w[i])
    return l


global old_guess1
global old_guess2
global old_guess3
global old_guess4
global old_guess5
global old_guess6
global search_word
search_word = choose_word()


def decode_key(k: str) -> str:
    if k == b'\x08':
        k = ""
    else:
        k = str(k, "utf-8")
    return k


def key_press_detection():
    k: str = getch()
    if os.name == "nt":
        k = decode_key(k)
    else:
        if k == "\n":
            k = "enter"
        if k == "\t":
            k = "tab"
        if k == "\x1b":
            k = "esc"
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


def compare_word(guess: list) -> list:
    """
    w = word
    g = guess
    if a letter is on the right place it will be green
    if a letter is in the word it will be yellow and it can only be used once per letter so if there a 2 "a" in the word and you guess 3 "a" it will be yellow 2 times
    if a letter is not in the word it will be white
    """
    g:list = guess
    w:list = [str(), str(), str(), str(), str()]
    w.clear()
    for i in range(5):
        w.append(search_word[i])

    o: list = [str(), str(), str(), str(), str()]
    for i in range(5):
        if w[i] == g[i]:
            o[i] += str(color(1))
            w[i] = "_"
        elif g[i] in w:
            o[i] += str(color(2))
            w[w.index(g[i])] = "_"
        else:
            o[i] += str(color(3))

    return o


def color(case: int) -> str:
    if case == 1:
        return "\033[32m"  # green
    elif case == 2:
        return "\033[33m"  # yellow
    elif case == 3:
        return "\033[37m"  # white
    elif case == 4:
        return "\033[31m"  # red
    elif case == 5:
        return "\033[0m"  # reset


def word(word: str, colo:list) -> str:
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

    white = color(3)
    print()
    print(" " * (tc // 2 - 37) + colo[0] + f"╔═══════╗" + " " * 5 + colo[1] + "╔═══════╗" + " " * 5 + color(
        5) + colo[2]+ "╔═══════╗" + " " * 5 + colo[3]+ "╔═══════╗" + " " * 5 + colo[4]+ "╔═══════╗")
    print(" " * (
                tc // 2 - 37) + colo[0] + f"║       ║" + " " * 5 + colo[1] + "║       ║" + " " * 5 + colo[2] + "║       ║" + " " * 5 + colo[3] + "║       ║" + " " * 5 + colo[4] + "║       ║")
    print(" " * (
                tc // 2 - 37) + colo[0] + "║   "+white+f"{w[0]}"+ colo[0] +"   ║" + " " * 5 + colo[1] + "║   "+white+f"{w[1]}"+ colo[1] +"   ║" + " " * 5 + colo[2] + "║   "+white+f"{w[2]}"+ colo[2] +"   ║" + " " * 5 + colo[3] + "║   "+white+f"{w[3]}"+ colo[3] +"   ║" + " " * 5 + colo[4]+ "║   "+white+f"{w[4]}"+ colo[4] +"   ║")
    print(" " * (
                tc // 2 - 37)+ colo[0] + f"║       ║" + " " * 5+ colo[1] + "║       ║" + " " * 5 + colo[2]+ "║       ║" + " " * 5+ colo[3] + "║       ║" + " " * 5 + colo[4]+ "║       ║")
    print(" " * (
                tc // 2 - 37)+ colo[0] + f"╚═══════╝" + " " * 5 + colo[1] + "╚═══════╝" + " " * 5 + colo[2]+ "╚═══════╝" + " " * 5 + colo[3]+ "╚═══════╝" + " " * 5 + colo[4]+ "╚═══════╝"+ color(5))


# TODO: make this shit usable and to not have to hard code the pattern
""" 
def kastel(w: str) -> tuple[str, str, str, str, str]:
    tc: int = infos_os("c")
    l1 = f"╔═══════╗" + " " * 5
    l2 = f"║       ║" + " " * 5
    l3 = f"║   {w}   ║" + " " * 5
    l4 = f"║       ║" + " " * 5
    l5 = f"╚═══════╝" + " " * 5
    return l1, l2, l3, l4, l5
"""


def draw(l: list, g: list, turn: int) -> None:
    global old_guess1
    global old_guess2
    global old_guess3
    global old_guess4
    global old_guess5
    global old_guess6
    tc_size: int = infos_os("c")
    one: str = ""
    tow: str = ""
    three: str = ""
    four: str = ""
    five: str = ""
    six: str = ""
    one_l: list = []
    tow_l: list = []
    three_l: list = []
    four_l: list = []
    five_l: list = []
    six_l: list = []

    for i in range(30):
        if i < 5:
            one_l.append(l[i])
        elif i < 10:
            tow_l.append(l[i])
        elif i < 15:
            three_l.append(l[i])
        elif i < 20:
            four_l.append(l[i])
        elif i < 25:
            five_l.append(l[i])
        elif i < 30:
            six_l.append(l[i])


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
    print(" " * (tc_size // 2 - 14) + "Py Wordle v0.3")
    print()
    print()
    if turn > 1:
        colo = compare_word(one_l)
    else:
        colo = [color(3) for i in range(5)]
    word(one, colo)
    print()
    print()
    if turn > 2:
        colo = compare_word(tow_l)
    else:
        colo = [color(3) for i in range(5)]
    word(tow, colo)
    print()
    print()
    if turn > 3:
        colo = compare_word(three_l)
    else:
        colo = [color(3) for i in range(5)]
    word(three, colo)
    print()
    print()
    if turn > 4:
        colo = compare_word(four_l)
    else:
        colo = [color(3) for i in range(5)]
    word(four, colo)
    print()
    print()
    if turn > 5:
        colo = compare_word(five_l)
    else:
        colo = [color(3) for i in range(5)]
    word(five, colo)
    print()
    print()
    if turn > 6:
        colo = compare_word(six_l)
    else:
        colo = [color(3) for i in range(5)]
    word(six, colo)


def tui():
    my_guess: list = []
    turn: int = 1
    guess: list = []
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
    draw(guess, search_word, turn)
    for i in range(6): #TODO: Endscreen mit win screen :)
        my_guess.clear()
        guess = guessing(turn, guess)
        for i in range(5):
            my_guess.append(guess[turn * 5 - 5 + i])
        if search_word == my_guess:
            break
        turn += 1
    print(" ".join(guess))
    input("press enter to exit")


def guessing(turn: int, guess: list) -> list:
    count: int = (turn - 1) * 5
    i_will_die: bool = True
    while i_will_die:
        k = key_press_detection()
        print(k, "done writing", count)
        if k == "" and 0 < count != (turn - 1) * 5:
            count -= 1
            guess[count] = " "
        elif k == "" and count == (turn - 1) * 5:
            pass
        elif k == "enter" and count == turn * 5:
            i_will_die = False
            turn += 1
        elif count > 29:
            pass
        elif turn * 5 <= count:
            pass
        elif k == "enter":
            pass
        elif k == "space":
            guess[count] = " "
            count += 1
        elif k == "esc":
            pass
        else:
            print("else")
            guess[count] = k
            count += 1
        draw(guess, search_word, turn)
        print(k, ":done drawnig", count, ":count", turn, ":turn", guess, ":guess", search_word, ":search_word")
    return guess


def infos_os(need: str) -> int:
    if need == "c":
        return os.get_terminal_size().columns
    elif need == "l":
        return os.get_terminal_size().lines
    else:
        return 0


if __name__ == "__main__":
    greeting()
    tui()
