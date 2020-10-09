"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
    
    if xCount == oCount:
        return X

    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    if not result[action[0]][action[1]] == EMPTY:
        raise Exception("not a valid result")

    if player(board) == X:
        result[action[0]][action[1]] = X
    if player(board) == O:
        result[action[0]][action[1]] = O

    return result
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            # print("win across")
            if board[i][0] == X:
                return X
            if board[i][0] == O:
                return O
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            # print("win up and down")
            if board[0][i] == X:
                return X
            if board[0][i] == O:
                return O
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        # print("win diagonal top to bot")
        if board[0][0] == X:
            return X
        if board[0][0] == O:
            return O
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        # print("win diagonal bot to top")
        if board[0][2] == X:
            return X
        if board[0][2] == O:
            return O

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if not winner(board) == None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False 

    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        v = float('-inf')
        for action in actions(board):
            value = minvalue(board, action)
            if v < value:
                v = value
                opMove = action

    else:
        v = float('inf')
        for action in actions(board):
            value = maxvalue(board, action)
            if v > value:
                v = value
                opMove = action
    
    return opMove
    raise NotImplementedError

def maxvalue(board, action):
    v = float('-inf')
    moveResult = result(board, action)
    if terminal(moveResult):
        return utility(moveResult)
    for nextAction in actions(moveResult):
        v = max(v, minvalue(moveResult, nextAction))

    return v
    raise NotImplementedError

def minvalue(board, action):
    v = float('inf')
    moveResult = result(board, action)
    if terminal(moveResult):
        return utility(moveResult)
    for nextAction in actions(moveResult):
        v = min(v, maxvalue(moveResult, nextAction))

    return v
    raise NotImplementedError
