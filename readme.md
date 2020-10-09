# **CS50 STUDENTS, TAKE NOTE**
### This repository contains my homework submission for the tic tac toe problem set. If you have not already submitted your homework, please keep in mind cs50's academic honesty policy. In other words, spoiler warning!

----

This program includes a tic tac toe AI that will play optimally against you using a **Minimax Algorithm**, a common algorithm used in adversarial multi-agent problems.

This style AI requires the following:
* *S(0)*, an initial state of the board (all empty squares)
* *Players(S)*, returns which player to move in state S
* *Actions(S)*, returns legal moves in state S
* *Results(S, A)*, returns state after action A taken in state S
* *Terminal(A)*, checks if state S is a terminal state
* *Utility(S)*, final numerical value for terminal state S

These components can be seen in **tictactoe.py** in addition to several functions pertaining to the Minimax algorithm. Briefly, the Minimax algorithm works by assigning one agent with the role of *maximizing* the score (in this case Player X) and the other agent with the role of *minimizing* the score (Player O). In the `minimax` method, you can see this algorithm at work. If it is Player X's turn, this agent will "put on the hat" of Player O, calling a `minvalue` method in order to anticipate Player O's move given Player X's decision. This is an recursive function where Player O then has to anticipate Player X's moves using `maxvalue`, on and on, until the utility function returns a value from a terminal state (in the case of tic tac toe, this will either be -1, 0 (for a tie) or 1).

**runner.py** contains the UI functionality of the tic tac toe game and can be opened from the terminal to start a game. Please, note that you may need to install the requirements found in **requirements.txt** by running `pip3 install -r requirements.txt`.

Example of Game:
![alt text](tictactoe.PNG)