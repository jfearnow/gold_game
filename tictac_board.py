def draw():
    board = ''

    for i in range(-1,6):

        if i % 2 == 0:
            board += '|      ' * 4
            board += '\n|      |      |      |'

        else:
            board += ' _____ ' * 3

        board += '\n'
    print (board)

draw()