import csv
import os
import time
from board import Board
from player import ComputerPlayer
from scoring import score_nexus, score_titan

def contest(first, second):
    board = Board()
    roster = {"X": first, "O": second}
    totals = {first.label: {"nodes": 0, "pruned": 0}, second.label: {"nodes": 0, "pruned": 0}}
    turn = "X"
    turns = 0
    started = time.perf_counter()
    while not board.finished():
        actor = roster[turn]
        square, count = actor.move(board, turn)
        board.place(square, turn)
        totals[actor.label]["nodes"] += count.visited
        totals[actor.label]["pruned"] += count.cutoffs
        turns += 1
        turn = "O" if turn == "X" else "X"
    return board.winner() or "DRAW", turns, totals, time.perf_counter() - started

def write_table(filename, records):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)

def depth_study():
    records = []
    for level in range(1, 5):
        first_ai = ComputerPlayer("STUDY_AI", level, score_nexus)
        second_ai = ComputerPlayer("REFERENCE", level, score_nexus)
        outcomes, nodes, cuts, elapsed = [], 0, 0, 0.0
        for game_no in range(20):
            x, o = (first_ai, second_ai) if game_no % 2 == 0 else (second_ai, first_ai)
            winner, _, stats, duration = contest(x, o)
            if winner == "DRAW":
                outcomes.append("DRAW")
            else:
                outcomes.append("STUDY_AI" if (winner == "X" and x is first_ai) or (winner == "O" and o is first_ai) else "REFERENCE")
            nodes += sum(item["nodes"] for item in stats.values())
            cuts += sum(item["pruned"] for item in stats.values())
            elapsed += duration
        records.append({"depth": level, "games": 20, "ai_wins": outcomes.count("STUDY_AI"),
                        "opponent_wins": outcomes.count("REFERENCE"), "draws": outcomes.count("DRAW"),
                        "mean_nodes": round(nodes / 20, 2), "mean_pruned": round(cuts / 20, 2),
                        "mean_seconds": round(elapsed / 20, 6)})
    return records

def agent_battle():
    nexus = ComputerPlayer("NEXUS", 3, score_nexus)
    titan = ComputerPlayer("TITAN", 3, score_titan)
    records = []
    for number in range(1, 11):
        x, o = (nexus, titan) if number % 2 else (titan, nexus)
        winner, turns, stats, duration = contest(x, o)
        records.append({"game": number, "first": x.label, "winner": winner, "moves": turns,
                        "nexus_nodes": stats["NEXUS"]["nodes"], "titan_nodes": stats["TITAN"]["nodes"],
                        "nexus_pruned": stats["NEXUS"]["pruned"], "titan_pruned": stats["TITAN"]["pruned"],
                        "execution_time_seconds": round(duration, 6)})
    return records
