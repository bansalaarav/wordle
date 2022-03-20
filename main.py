from colorama import Fore, Back, Style

count = 0


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


def print_guess_answer(word):
    _box_1_top, _box_1_middle, _box_1_bottom = box(word, "yellow")
    _box_2_top, _box_2_middle, _box_2_bottom = box(word, "green")
    _box_3_top, _box_3_middle, _box_3_bottom = box(word, "yellow")
    _box_4_top, _box_4_middle, _box_4_bottom = box(word, "")
    _box_5_top, _box_5_middle, _box_5_bottom = box(word, "green")
    print(f"""
{_box_1_top} {_box_2_top} {_box_3_top} {_box_4_top} {_box_5_top}
{_box_1_middle} {_box_2_middle} {_box_3_middle} {_box_4_middle} {_box_5_middle}
{_box_1_bottom} {_box_2_bottom} {_box_3_bottom} {_box_4_bottom} {_box_5_bottom}
    """)


a = 0

while a < 6:
    word = input("> ").strip().upper()
    if len(word) != 5:
        print("Please enter a 5 letter word!")
    else:
        print_guess_answer(word)
        a += 1
