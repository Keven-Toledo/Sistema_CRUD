def red(txt):
    text = f'\033[1;31m{txt}\033[m'
    print(text)


def yellow(txt):
    text = f'\033[1;33m{txt}\033[m'
    print(text)


def blue(txt):
    text = f'\033[1;34m{txt}\033[m'
    print(text)


def black(txt):
    text = f'\033[1;40m{txt}\033[m'
    print(text)


def green(txt):
    text = f'\033[1;32m{txt}\033[m'
    print(text)


def white(txt):
    text = f'\033[1m{txt}'
    print(text)
