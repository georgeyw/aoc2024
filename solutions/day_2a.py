import numpy as np 

from utils import read_input_lines


def check_decreasing(list):
    out = True
    for i in range(len(list)-1):
        if list[i] <= list[i+1]:
            out = False
    return out

def check_increasing(list):
    out = True
    for i in range(len(list)-1):
        if list[i] >= list[i+1]:
            out = False
    return out

def check_distance(list, distance):
    out = True
    for i in range(len(list)-1):
        if abs(list[i] - list[i+1]) > distance:
            out = False
    return out


def check_safe(list, distance):
    if check_decreasing(list) or check_increasing(list):
            if check_distance(list, distance=3):
                return True 
    return False


if __name__ == "__main__":
    data = read_input_lines("2", split=True, ints=False)
    data = [np.array(x, dtype=np.int64) for x in data]
    
    count = 0
    for line in data:
        if check_safe(line, distance=3):
            count += 1

    print(count)
