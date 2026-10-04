import argparse
import random
from board import Board
from player import ComputerPlayer
from scoring import score_nexus, score_titan
from arena import agent_battle, depth_study, write_table

def interactive():
    players = {"X": ComputerPlayer("NEXUS", 3, score_nexus),
               "O": ComputerPlayer("TITAN", 3, score_titan)}
    board, turn = Board(), "X"
    while not board.finished():
        board.render()
        chosen, metrics = players[turn].move(board, turn)
        print(f'{players[turn].label}: square {chosen + 1}; visited {metrics.visited}; pruned {metrics.cutoffs}')
        board.place(chosen, turn)
        turn = "O" if turn == "X" else "X"
    board.render()
    print("Winner:", board.winner() or "DRAW")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", choices=("depth", "battle", "play"))
    task = parser.parse_args().task
    random.seed(42)
    if task == "play":
        interactive()
    elif task == "depth":
        results = depth_study()
        write_table("results/depth_experiment.csv", results)
        for row in results:
            print(row)
    else:
        results = agent_battle()
        write_table("results/results.csv", results)
        for row in results:
            print(row)
        print("NEXUS wins:", sum(r["winner"] == "NEXUS" for r in results))
        print("TITAN wins:", sum(r["winner"] == "TITAN" for r in results))
        print("Draws:", sum(r["winner"] == "DRAW" for r in results))

if __name__ == "__main__":
    main()
