"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
PLAYER = None
WINNER = None


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

    global PLAYER

    if PLAYER == None:
        PLAYER = X
    elif PLAYER == X:
        PLAYER = O
    else:
        PLAYER = X

    return PLAYER
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
    print("result function")
    print(action)

    result = copy.deepcopy(board)

    # print(action)
    # print("x")
    if not result[action[0]][action[1]] == EMPTY:
        raise Exception("not a valid result")

    if PLAYER == X:
        result[action[0]][action[1]] = X
    if PLAYER == O:
        result[action[0]][action[1]] = O

    return result
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    global WINNER
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            if board[i][0] == X:
                WINNER = X
                return WINNER
            if board[i][0] == O:
                WINNER = O
                return WINNER
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            if board[0][i] == X:
                WINNER = X
                return WINNER
            if board[0][i] == O:
                WINNER = O
                return WINNER
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == X:
            WINNER = X
            return WINNER
        if board[0][0] == O:
            WINNER = O
            return WINNER
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] == X:
            WINNER = X
            return WINNER
        if board[0][2] == O:
            WINNER = O
            return WINNER

    return WINNER

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if not winner(board) == None:
        print("Terminal resulted true")
        return True
    if any(cell==EMPTY for (_, _, cell) in board) == False:
        print("Terminal resulted true")
        return True

    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if WINNER == X:
        return 1
    if WINNER == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    options = set()
    for action in actions(board):
        if PLAYER == X:
            value = maxvalue(board, action)
        elif PLAYER == O:
            value = minvalue(board, action)
        options.add((action, value))

    if PLAYER == X:
        opMove = max(options, key = lambda i : i[1])[0]
    elif PLAYER == O:
        opMove = min(options, key = lambda i : i[1])[0]
    return opMove
    raise NotImplementedError

def maxvalue(board, action):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    moveResult = result(board, action)
    for nextAction in actions(moveResult):
        v = max(v, minvalue(moveResult, nextAction))
    # print("maxvalue function")
    # print(action)
    return v
    raise NotImplementedError

def minvalue(board, action):
    if terminal(board):
        return utility(board)
    v = float('inf')
    moveResult = result(board, action)
    for nextAction in actions(moveResult):
        v = min(v, maxvalue(moveResult, nextAction))

    return v
    raise NotImplementedError
