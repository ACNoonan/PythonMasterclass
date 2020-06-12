def python_food():
    width = 80
    text = 'spam & eggs'
    left_margin = (width - len(text)) // 2
    print(' ' * left_margin, text)


def center_text(*args, sep=' '):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return ' ' * left_margin + text

with open('menu.txt', 'w') as menu:
    s1 = (center_text('spam and eggs'))
    print(s1, file=menu)
    s2 = (center_text('spam, spam and eggs'))
    print(s2, file=menu)
    s3 = (center_text(9))
    print(s3, file=menu)
    s4 = (center_text('spam, spam, spam and eggs'))
    print(s4, file=menu)
    s5 = (center_text('first', 'second', 3, 4, 'spam', sep=':'))
    print(s5, file=menu)

