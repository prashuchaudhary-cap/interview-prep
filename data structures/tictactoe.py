def printBoard(board):
    for i in range(0, 3):
        line = ""
        for j in range(0, 3):
            line = line + str(board[i][j]) + " "
        print(line + "\n")


def printTurnMessage(player):
    print('Player-{player}s turn. Enter any number from 1-9 to indicate your move.'.format(player=player))


def getIntegerInput():
    try:
        return int(input())
    except ValueError:
        return 0


def getValidInput(board):
    num = getIntegerInput()
    i, j = getBoardPosition(num)

    while (num > 9 or num < 1) or board[i][j] != '_':
        print('Invalid input. Please try again.')
        num = getIntegerInput()
        i, j = getBoardPosition(num)

    return num


def anyPlayerWon(board):
    for i in range(0, 3):
        hline = "".join(board[i])
        vline = "".join([board[j][i] for j in range(0, 3)])
        dline = ""

        if i == 0:
            dline = "".join([board[i][i] for i in range(0, 3)])
        elif i == 2:
            dline = "".join([board[i][0], board[1][1], board[0][i]])

        if hline == 'XXX' or vline == 'XXX' or dline == 'XXX':
            return 'X'
        elif hline == 'OOO' or vline == 'OOO' or dline == 'OOO':
            return 'O'

    return None


def getBoardPosition(number):
    number -= 1
    return number // 3, number % 3


def setPlayerMarker(player, number, board):
    i, j = getBoardPosition(number)
    board[i][j] = player


def startGame():
    turns = 0
    players = ['O', 'X']
    board = [['_', '_', '_'] for i in range(0, 3)]
    playerWon = None

    while(turns <= 9):
        currentPlayer = players[turns % 2]

        printBoard(board=board)

        if turns >= 3:
            playerWon = anyPlayerWon(board=board)
            if playerWon:
                break

        printTurnMessage(player=currentPlayer)
        num = getValidInput(board=board)
        setPlayerMarker(player=currentPlayer, number=num, board=board)

        turns += 1

    if playerWon:
        print('Game Over : Player {player} has won'.format(player=playerWon))
    else:
        print('Game Over : Draw')


