import numpy as np

from utils import read_input_lines


if __name__ == "__main__":
    data = read_input_lines("1", split=True, ints=True)
    data = np.array(data)
    list1 = data[:, 0]
    list1.sort()
    list2 = data[:, 1]
    list2.sort()

    total_diffs = 0
    for i in range(len(list1)):
        a = list1[i]
        b = list2[i]
        total_diffs += abs(a - b)
    print(total_diffs)
