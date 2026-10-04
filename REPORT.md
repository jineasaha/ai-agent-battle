# Brief Report: Tic-Tac-Toe Agent Arena

## Aim
The assignment explores the effect of search depth and heuristic design by running two AI players against each other.

## Design
The board engine stores nine squares and handles valid moves, win detection and termination. A recursive Minimax search evaluates possible continuations. Alpha-Beta bounds stop exploring branches that cannot improve the current choice. Each search tracks visited nodes and cutoffs.

## Agent strategies
NEXUS uses a line-threat heuristic that rewards its own open lines and penalizes the opponent's. TITAN combines similar line evaluation with center and corner preferences. Both use depth 3 in the tournament and the same search algorithm.

## Experiments
The depth study uses the NEXUS evaluation for both sides and tests depths 1, 2, 3 and 4 over 20 games at each level, alternating the first player. The battle consists of ten games, with the starting agent alternating between NEXUS and TITAN. Generated measurements are stored in the CSV files in `results/`.

## Interpretation
Use the recorded wins, draws, visited nodes, cutoffs and runtime together. Greater depth examines more future states and may increase computation, while Alpha-Beta pruning avoids branches that cannot change a decision. Heuristic differences can influence move selection, but a small number of Tic-Tac-Toe games is not enough to claim a strategy is universally superior. Execution time depends on the computer and should be regenerated on the submission machine.

## Reproduction
Run `python main.py depth` and `python main.py battle` from the project directory to generate the experiment data. The report should be read alongside the actual CSV output.
