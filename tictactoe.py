"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
PLAYER = EMPTY


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
    if PLAYER == EMPTY:
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
    result = copy.deepcopy(board)
    
    if result[action] != EMPTY:
            raise Exception("not a valid result")
    
    if player == X:
        result[action] = X
    if player == O:
        result[action] = O
    
    return result
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if not terminal:
        winner = None
    else:
        if utility < 0:
            winner = O
        elif utility > 0:
            winner = X
        else:
            winner = None
    
    return winner
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if all(flag!=EMPTY for (_, _, flag) in board):
        return True
    
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return True
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True
        
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            if board[i][0] == X:
                return 1
            if board[i][0] == O:
                return -1
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            if board[0][i] == X:
                return 1
            if board[0][i] == O:
                return -1
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == X:
            return 1
        if board[0][0] == O:
            return -1
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] == X:
            return 1
        if board[0][2] == O:
            return -1
                
    if all(flag!=EMPTY for (_, _, flag) in board):
        return 0
    
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player == X:
        v = maxvalue(board)
    if player == O:
        v = minvalue(board)
        
    return v
    raise NotImplementedError
    
def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, minvalue(result(board,action)))
    return v
    raise NotImplementedError
    
def minvalue(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, maxvalue(result(board,action)))
    return v
    raise NotImplementedError
