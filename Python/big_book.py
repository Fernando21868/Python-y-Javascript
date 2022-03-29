import random

try:
    import pyperclip
except ImportError:
    pass


def main():
    print('''L3375P34]< (leetspeek)
By Al Sweigart al@inventwithpython.com

Enter your leet message:''')
    english = input('> ')
    print()
    leetspeak = englishToLeetspeak(english)
    print(leetspeak)

    try:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass


def englishToLeetspeak(message):
    char_mapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']}
    leetspeak = ''
    for char in message:
        if char.lower() in char_mapping and random.random() <= 0.70:
            posibble_replacements = char_mapping[char.lower()]
            leet_replacement = random.choice(posibble_replacements)
            leetspeak += leetspeak+leet_replacement
        else:
            leetspeak = leetspeak+char
    return leetspeak


if __name__ == '__main__':
    main()
