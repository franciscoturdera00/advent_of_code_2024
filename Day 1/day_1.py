import bisect
import functools

# text_file = "Day 1\\test_input"
text_file = "Day 1\\part_1"

def get_sorted_lists(lines):
    list_1 = list()
    list_2 = list()
    for line in lines:
        a, _, _, b = line.split(" ")
        bisect.insort_left(list_1, a)
        bisect.insort_left(list_2, b)
    return list_1, list_2


def get_distance(list_1, list_2):
    total_distance = 0
    for index in range(0, len(list_1)):
        total_distance += abs(abs(int(list_1[index])) - abs(int(list_2[index])))
    return total_distance

def get_count_of(list_input):
    res = dict()
    list_input = list(map(int, list_input))
    for n in list_input:
        res[int(n)] = list_input.count(n)
    return res

with open(text_file) as f:
    lines = f.readlines()
    list_1, list_2 = get_sorted_lists(lines)
    appearance = get_count_of(list_2)
    similarity_score = 0
    for n in list_1:
        similarity_score += int(n) * appearance.get(int(n), 0)
    print(similarity_score)
