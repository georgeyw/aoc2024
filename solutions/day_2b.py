import numpy as np 

from utils import read_input_lines
from day_2a import check_safe


if __name__ == "__main__":
    data = read_input_lines("2", split=True, ints=False)
    data = [np.array(x, dtype=np.int64) for x in data]
    
    count = 0

    for line in data:
        safe = False
        if check_safe(line, distance=3):
            safe = True
        for i in range(len(line)):
            new_line = line.copy()
            new_line = np.delete(new_line, i)
            if check_safe(new_line, distance=3):
                safe = True
        if safe:
            count += 1

    print(count)
