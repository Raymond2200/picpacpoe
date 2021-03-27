currentPlayer = 1
board = {
        "a1":0, "b1":0, "c1":0,
        "a2":0, "b2":0, "c2":0,
        "a3":0, "b3":0, "c3":0
    }

def resetBoard():
    global board
    board = {
        "a1":0, "b1":0, "c1":0,
        "a2":0, "b2":0, "c2":0,
        "a3":0, "b3":0, "c3":0
    }

def winnercheck():
    global currentPlayer
    if board["a1"] == 1 and board['a2'] == 1 and board['a3'] == 1 or board['b1'] == 1 and board['b2'] == 1 and board['b3'] == 1 or board['c1'] ==1 and board['c2'] == 1 and board['c3'] == 1 or board['a1'] == 1 and board['b1'] == 1 and board['c1'] == 1 or board['a2'] == 1 and board['b2'] == 1 and board['c2'] == 1 or board['a3'] == 1 and board['b3'] == 1 and board['c3'] == 1 or board['a1'] == 1 and board['b2'] == 1 and board['c3'] == 1 or board['a3'] == 1 and board['b2'] == 1 and board['c1'] == 1:
        print(" Player 1 is the winner")
        currentPlayer = 0
    elif  board['a1'] == 2 and board['a2'] == 2 and board['a3'] == 2 or board['b1'] == 2 and board['b2'] == 2 and board['b3'] == 2 or board['c1'] == 2 and board['c2'] == 2 and board['c3'] == 2 or board['a1'] == 2 and board['b1'] == 2 and board['c1'] == 2 or board['a2'] == 2 and board['b2'] == 2 and board['c2'] == 2 or board['a3'] == 2 and board['b3'] == 2 and board['c3'] == 2 or board['a1'] == 2 and board['b2'] == 2 and board['c3'] == 2 or board['a3'] == 2 and board['b2'] == 2 and board['c1'] == 2:
        print("player 2 is the winner")
        currentPlayer = 0
    elif board['a1'] != 0 and board['a2'] != 0 and board['a3'] != 0 and board['b1'] != 0 and board['b2'] != 0 and board['b3'] != 0 and board['c1'] != 0 and board['c2'] != 0 and board['c3'] != 0:
        print('the game is a tie')
        currentPlayer = 0
        render()


def play():
    global currentPlayer
    global board
    incoming = input(f"player{currentPlayer} select your next move:")
    incoming = incoming.lower()
    if incoming.lower() == "new":
        resetBoard()
    # elif incoming.lower not in ['a1','a2','a3','b1','b2','b3','c1','c2','c3']:
    #     print("invalid move please try again")
    #     play
    elif board[incoming] != 0:
        print("Bogus move, please try another!")
        play
    elif currentPlayer == 1:
        board[incoming] = 1
        currentPlayer = 2
    elif currentPlayer == 2:
        board[incoming] = 2
        currentPlayer = 1
          


def tequa(a):
    if board[a] == 0:
        return "   "
    elif board[a] == 1:
        return " X "
    elif board[a] == 2:
        return " O "


def drawboard():
    v = "|"
    h = "   -----------"
    print("    A   B   C")
    print("1) " + tequa("a1") + v + tequa("b1") + v + tequa("c1"))
    print(h)
    print("2) " + tequa("a2") + v + tequa("b2") + v + tequa("c2"))
    print(h)
    print("3) " + tequa("a3") + v + tequa("b3") + v + tequa("c3"))


def render():
    global currentPlayer
    if currentPlayer != 0:
        play()
        drawboard()
        winnercheck()
        render()
    elif currentPlayer == 0:
        print("New Game")
        currentPlayer = 1
        render()

render()