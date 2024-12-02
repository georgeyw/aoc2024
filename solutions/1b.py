from collections import defaultdict

from utils import read_input_lines


def count_occurrences(l):
    out_dict = defaultdict(int)
    for x in l:
        out_dict[x] += 1
    return out_dict


if __name__ == "__main__":
    data = read_input_lines("1a", split=True, ints=True)
    dict1 = count_occurrences(data[:, 0])
    dict2 = count_occurrences(data[:, 1])

    total = 0
    for key in dict1:
        total += key * dict1[key] * dict2[key]
    print(total)
