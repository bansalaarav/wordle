from colorama import init, Fore, Back, Style
import random

init(convert=True)
count = 0
a = 1


congrats_words = {
    1: "Genius",
    2: "Magnificent",
    3: "Impressive",
    4: "Splendid",
    5: "Great",
    6: "Phew"
}

answer = ""
letters = {
    "l_1": "",
    "l_2": "",
    "l_3": "",
    "l_4": "",
    "l_5": ""
}


def check_guess(guess):
    global answer, letters

    for letter in guess:
        if letter in answer and guess.index(letter) == answer.index(letter):
            letters[f"l_{guess.index(letter)+1}"] = "green"
        elif letter in answer:
            letters[f"l_{guess.index(letter)+1}"] = "yellow"
        else:
            letters[f"l_{guess.index(letter)+1}"] = ""

    print_guess_answer(guess.upper())


def box(word, color):
    _box_top = box_top(color)
    _box_middle = box_middle(word, color)
    _box_bottom = box_bottom(color)
    return _box_top, _box_middle, _box_bottom


def box_top(color):
    if color == "yellow":
        color = Back.YELLOW
    elif color == "green":
        color = Back.GREEN
    else:
        color = Back.WHITE
    box = f"""
{Fore.BLACK + color}╔═══╗{Style.RESET_ALL}
"""
    return box.strip()


def box_middle(word, color):
    global count
    if color == "yellow":
        color = Back.YELLOW
    elif color == "green":
        color = Back.GREEN
    else:
        color = Back.WHITE
    box = f"""
{Fore.BLACK + color}║ {word[count]} ║{Style.RESET_ALL}
"""
    count += 1
    return box.strip()


def box_bottom(color):
    if color == "yellow":
        color = Back.YELLOW
    elif color == "green":
        color = Back.GREEN
    else:
        color = Back.WHITE
    box = f"""
{Fore.BLACK + color}╚═══╝{Style.RESET_ALL}
"""
    return box.strip()


def print_guess_answer(guess):
    global letters

    _box_1_top, _box_1_middle, _box_1_bottom = box(guess, letters["l_1"])
    _box_2_top, _box_2_middle, _box_2_bottom = box(guess, letters["l_2"])
    _box_3_top, _box_3_middle, _box_3_bottom = box(guess, letters["l_3"])
    _box_4_top, _box_4_middle, _box_4_bottom = box(guess, letters["l_4"])
    _box_5_top, _box_5_middle, _box_5_bottom = box(guess, letters["l_5"])
    print(f"""
{_box_1_top} {_box_2_top} {_box_3_top} {_box_4_top} {_box_5_top}
{_box_1_middle} {_box_2_middle} {_box_3_middle} {_box_4_middle} {_box_5_middle}
{_box_1_bottom} {_box_2_bottom} {_box_3_bottom} {_box_4_bottom} {_box_5_bottom}
    """)

    if letters["l_1"] == letters["l_2"] == letters["l_3"] == letters["l_4"] == letters["l_5"] == "green":
        print(f"{Fore.GREEN}{congrats_words[a]}!{Style.RESET_ALL}")
        exit()


def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if(str[i] == str[j]):
                return False
    return True


unique = False

while not unique:
    with open("possible_words.txt", "r") as f:
        words = f.read().splitlines()
        answer = random.choice(words)
        if check_unique(answer):
            unique = True

while a < 7:
    word = input("> ").strip().lower()
    if len(word) != 5:
        pass
    else:
        with open("words.txt", "r") as f:
            words = f.read().splitlines()

        if word in words:
            check_guess(word)
            a += 1
    count = 0
print(f"{Fore.RED}{answer.upper()}{Style.RESET_ALL}")
