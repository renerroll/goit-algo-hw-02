from collections import deque


def check_palindrome(param):
    if len(param) == 0:
        return "Empty input"

    prepared_phrase = param.lower().replace(" ", "")

    chars_dq = deque(prepared_phrase)
    if chars_dq == deque(reversed(chars_dq)):
        return f"{param} ось це точно паліндром"

    return f"{param} це не паліндром"


def is_palindrome(param):
    if len(param) == 0:
        return "Нічого не введено"

    prepared_phrase = param.lower().replace(" ", "")

    chars_dq = deque(prepared_phrase)
    while len(chars_dq) > 1:
        if chars_dq.popleft() != chars_dq.pop():
            return f"{param} це не паліндром"

    return f"{param}  ось це точно паліндром"


if __name__ == "__main__":
    try:
        txt = input("Введи речення для перевірки: ")
        test1 = check_palindrome(txt)
        print("перевірка1: ", test1)
        test2 = is_palindrome(txt)
        print("перевірка2: ", test2)

    except KeyboardInterrupt as err:
        print(err)
    except ValueError as err:
        print(err)