text_file = "day_2/input_part_1"
# text_file = "day_2/easy_input"


def check_values_validity(index, lesser_value, greater_value, retry=True):
    if greater_value - lesser_value > 3 or greater_value - lesser_value <= 0:
        if retry:
            # If failed, try again with one less element
            return any(safety_check(numbers[:index - x] + numbers[index - x + 1:], False) for x in range(index + 1))
        return False
    return True

def safety_check(numbers, retry=True):
    previous_value = int(numbers[0])
    increasing = True
    if previous_value >= int(numbers[1]):
        increasing = False
    safe = True
    for n in range(1, len(numbers)):
        current_value = int(numbers[n])
        if increasing:
            safe = check_values_validity(n, previous_value, current_value, retry)
        elif not increasing:
            safe = check_values_validity(n, current_value, previous_value, retry)
        if not safe:
            break
        previous_value = current_value
    return safe


with open(text_file) as f:
    lines = f.readlines()
    safe_count = 0
    for line in lines:
        numbers = line.split(" ")
        if len(numbers) <= 1:
            safe_count += 1
            continue
        if safety_check(numbers):
            safe_count += 1
        
        

print(safe_count)
