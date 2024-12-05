
# text_file = "day_5/example.txt"
text_file = "day_5/part_1.txt"

def main():
    with open(text_file) as f:
        lines = f.readlines()
        page_ordering_rules = [x for x in lines if "|" in x]
        updates = [x for x in lines if "|" not in x][1:]
        order_dict = build_ordering_dictionary(page_ordering_rules)
        update_lists = [[int(x) for x in inner.split(",")] for inner in updates]
        return sum_valid_updates(update_lists, order_dict)


def build_ordering_dictionary(orderings):
    ordering_dict = {}
    for ordering in orderings:
        before, after = list(map(int, ordering.split("|")))
        ordering_dict[after] = ordering_dict.get(after, list()) + [before]
    return ordering_dict

def update_is_valid(update, ordering_rules):
    for i, up in enumerate(update):
        for must_be_before in update[i + 1:]:
            if must_be_before in ordering_rules.get(up, list()):
                return False
    return True

def sum_valid_updates(updates, ordering_rules):
    total = 0
    for update in updates:
        if update_is_valid(update, ordering_rules):
            # total += update[int(len(update) /2)]
            continue
        else:
            valid_update = validate_update(update, ordering_rules)
            total += valid_update[int(len(update) /2)]
    return total

def validate_update(update, ordering_rules):
    new_update = [update[0]]
    for value in update[1:]:
        index = len(new_update)
        for ordered in new_update[::-1]:
            if value in ordering_rules.get(ordered, list()):
                index -= 1
        new_update.insert(index, value)
    return new_update

        

print(main())