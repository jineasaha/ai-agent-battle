# Tic-Tac-Toe Agent Arena


## Project
A Python implementation of a Tic-Tac-Toe engine, two Minimax agents, Alpha-Beta pruning, heuristic scoring, configurable lookahead and automated experiments.

## Players
- NEXUS: depth 3 with a line-threat heuristic.
- TITAN: depth 3 with threat scoring plus center and corner preferences.

Both agents use Minimax with Alpha-Beta pruning. Random choice is used only when multiple legal moves have the same best score.

## Setup
Python 3.9 or newer is sufficient. The project uses only the Python standard library.

## Execute
Run commands from this directory:
- `python main.py depth` — compares depths 1 through 4 over 20 games per depth and saves `results/depth_experiment.csv`.
- `python main.py battle` — runs 10 alternating-start NEXUS/TITAN games and saves `results/results.csv`.
- `python main.py play` — displays an automated game in the terminal.

## Contents
- `board.py`: board representation and rules
- `scoring.py`: heuristic functions
- `search.py`: Minimax and Alpha-Beta
- `player.py`: AI player class
- `arena.py`: experiments, tournament and CSV writing
- `main.py`: command-line interface
- `REPORT.md`: brief findings and interpretation
- `results/`: generated experiment data
