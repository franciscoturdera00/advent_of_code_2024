
from typing import Dict, Set
from networkx import Graph, DiGraph, simple_cycles, enumerate_all_cliques


# text_file = "day_23/example.txt"
text_file = "day_23/input.txt"

def main():
    lan_map = read_input(text_file)
    return find_maximal_clique(lan_map)

def find_maximal_clique(lan_map): # part 2
    DG = Graph(lan_map)
    all_cliques = list(enumerate_all_cliques(DG))
    largest_clique = sorted(all_cliques.pop())
    return ",".join(largest_clique)


def find_all_trios(lan_map): # part 1
    DG = DiGraph(lan_map)
    cycles = list(simple_cycles(DG))
    trio = list(filter(lambda c: len(c) == 3, cycles))
    historian_with_dups = list(filter(lambda c: any(player.startswith("t") for player in c), trio))
    historian = list(set(map(lambda f: tuple(sorted(f)), historian_with_dups)))
    return len(historian)

def read_input(file):
    lan_map: Dict[str, Set[str]] = dict()
    with open(file) as f:
        line = f.readline()
        while line:
            user1, user2 = line.split("-")
            if "\n" in user2:
                user2 = user2[:-1]
            curr1 = lan_map.get(user1, list())
            curr1.append(user2)
            curr2 = lan_map.get(user2, list())
            curr2.append(user1)
            lan_map[user1] = curr1
            lan_map[user2] = curr2
            line = f.readline()
    # for l, i in lan_map.items():
    #     print(l, i)
    return Graph(lan_map)

# for trio in main():
#     print(trio)
print(main())