import numpy as np


def read_input_lines(puzzle_id, split=True, ints=True):
    with open(f"../input/{puzzle_id}.txt", "r") as file:
        lines = file.readlines()
    lines = [line[:-1] for line in lines if line.endswith("\n")]
    lines = [line for line in lines if line]

    if split:
        lines = [line.split() for line in lines]

    if ints:
        lines = np.array(lines, dtype=np.int64)

    return lines
