def python_food():
    width = 80
    text = 'spam & eggs'
    left_margin = (width - len(text)) // 2
    print(' ' * left_margin, text)


def center_tect(*args, sep=' ', end='\n', file=None, flush=False):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text, end=end, file=file, flush=flush)

with open('centred.txt', mode='w') as centred_file:
    python_food()
    center_tect('spam and eggs', file=centred_file)
    center_tect('spam, spam and eggs', file=centred_file)
    center_tect(9, file=centred_file)
    center_tect('spam, spam, spam and eggs', file=centred_file)
    # center_tect(python_food())
    center_tect('first', 'second', 3, 4, 'spam', sep=':', file=centred_file)