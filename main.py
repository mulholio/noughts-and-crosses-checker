import sys

# board states take the form of 9 char strings
# "X", "O", "_"

# all possible board states
class BoardState:
    EMPTY='EMPTY'               # nothing on the board
    INVALID='INVALID'           # a state you could never arrive at
    NOUGHTS_WIN='NOUGHTS_WIN'
    CROSSES_WIN='CROSSES_WIN'
    DRAW='DRAW'


def getStateOfBoard(board):
    return BoardState.DRAW

# leave unchanged
for arg in sys.argv[1:]:
    print(getStateOfBoard(arg))

