#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# all possible board states
class BoardState:
    INVALID_BOARD="INVALID_BOARD"   # The entered string is invalid
    INVALID_GAME='INVALID_GAME'     # A game you could never arrive at
    EMPTY='EMPTY'                   # Nothing on the board
    IN_PROGRESS='IN_PROGRESS'       # Valid game in progress
    DRAW='DRAW'
    CROSSES_WIN='CROSSES_WIN'
    NOUGHTS_WIN='NOUGHTS_WIN'

class BoardElements:
    CROSS='X'
    NOUGHT='O'
    EMPTY='_'
    
def getStateOfBoard(board):
    """Returns the current state of a given board string"""

    def checkValidLength(board):
        """Checks the board is the right length"""
        validLength = 9
        if len(board) == validLength:
            return True
        else:
            return False
    
    def checkValidChars(board):
        """Checks the board only contains allowed characters"""

        def isValidChar(char):
            """Checks individual character validity"""
            if char == BoardElements.EMPTY or char == BoardElements.CROSS or char == BoardElements.NOUGHT:
                return True
            else:
                return False
        
        for char in board:
            if not isValidChar(char):
                return False
        return True

    def checkIsEmpty(board):
        """Checks if a given board is empty"""
        if board == '_________':
            return True
        else:
            return False

    def checkValidElementDifference(board):
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

            numCrosses = countElement(BoardElements.CROSS, board)
            numNoughts = countElement(BoardElements.NOUGHT, board)
            return numCrosses - numNoughts

        difference = elementDifference(board)
        if -1 <= difference <= 1:
            return True
        else:
            return False

    def checkThreeInRow(element, board):
        """Checks to see if an element has three in a row"""

        # the indexes of all possible three-in-a-rows
        winningArrangements = [
            [0,1,2],    # Row   0
            [3,4,5],    # Row   1
            [6,7,8],    # Row   2
            [0,3,6],    # Col   0
            [1,4,7],    # Col   1
            [2,5,8],    # Col   2
            [0,4,8],    # Diag  0
            [2,4,6],    # Diag  1
        ]

        def getBoardCharsFromArrangement(arrangement, board):
            """Gets the characters on a tested board for a given arrangement"""

            index0 = arrangement[0]
            index1 = arrangement[1]
            index2 = arrangement[2]
            char0 = board[index0]
            char1 = board[index1]
            char2 = board[index2]
            return [char0, char1, char2]
        
        winningArray = [element, element, element]

        for arrangement in winningArrangements:
            if getBoardCharsFromArrangement(arrangement, board) == winningArray:
                return True
        return False

    def checkFull(board):
        """Checks there are no empty characters in board"""
        for char in board:
            if char == '_':
                return False
        return True

    if not checkValidLength(board) or not checkValidLength(board):
        return BoardState.INVALID_BOARD
    elif checkIsEmpty(board):
        return BoardState.EMPTY
    # if difference between O and X is > 1 or both have won, the game is invalid
    elif not checkValidElementDifference(board) or (checkThreeInRow(BoardElements.CROSS, board) and checkThreeInRow(BoardElements.NOUGHT, board)):
        return BoardState.INVALID_GAME
    elif checkThreeInRow(BoardElements.CROSS, board):
        return BoardState.CROSSES_WIN
    elif checkThreeInRow(BoardElements.NOUGHT, board):
        return BoardState.NOUGHTS_WIN
    elif checkFull(board):
        return BoardState.DRAW
    else:
        return BoardState.IN_PROGRESS
    # catching some error catching just in case I missed a case
    # raise ValueError("Board does not match any of the states")

# leave unchanged
for arg in sys.argv[1:]:
    print(getStateOfBoard(arg))

