#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

class BoardElements:
    X='X'
    O='O'
    _='_'

def getStateOfBoard(board):
    """Returns the current state of a given board string"""

    def checkIsEmpty(board):
        """Checks if a given board is empty"""
        if board == '_________':
            return True
        else:
            return False

    def checkIsValid(board):
        """Checks if players could have arrived at the current board"""
        
        def elementDifference(board):
            """Returns the difference between no. crosses and no. noughts"""

            def countElement(element, board):
                """Count the number of noughts, crosses or empties"""
                count = 0
                for char in board:
                    if char == element:
                        count = count + 1
                return count

            numCrosses = countElement(BoardElements.X, board)
            numNoughts = countElement(BoardElements.O, board)
            return numCrosses - numNoughts

        difference = elementDifference(board)
        if -1 <= difference <= 1:
            return True
        else:
            return False

    def checkWin(element, board):
        return


    # elif checkDraw(board):
        # return BoardState.DRAW

    def checkFull(board):
        for char in board:
            if char == '_':
                return False
        return True

    # catch any other possibilities that I may have forgotten
    # return error

    if checkIsEmpty(board):
        return BoardState.EMPTY
    elif not checkIsValid(board):
        return BoardState.INVALID
    elif checkWin(BoardElements.X, board):
         return BoardState.CROSSES_WIN
    elif checkWin(BoardElements.O, board):
        return BoardState.NOUGHTS_WIN
    elif checkFull(board):
        return BoardState.DRAW
    else:
        # just in case I missed a case
        raise ValueError("Board does not match any of the states")

# leave unchanged
for arg in sys.argv[1:]:
    print(getStateOfBoard(arg))

