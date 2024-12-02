text_file = "input_part_1"
# text_file = "easy_input"
safe_count = 0


def safety_check(numbers, retry=False):
    previous_value = int(numbers[0])
    increasing = True
    if previous_value >= int(numbers[1]):
        increasing = False
    safe = True
    for n in range(1, len(numbers)):
        current_value = int(numbers[n])
        if increasing:
            if current_value - previous_value > 3 or current_value - previous_value <= 0:
                if not retry and n < len(numbers):
                    return any(safety_check(numbers[:n - x] + numbers[n - x + 1:], True) for x in range(0,len(numbers)))
                safe = False
                break
        else:
            if previous_value - current_value > 3 or previous_value - current_value <= 0:
                if not retry and n < len(numbers):
                    return any(safety_check(numbers[:n - x] + numbers[n - x + 1:], True) for x in range(0,len(numbers)))
                safe = False
                break
        previous_value = current_value
    return safe


with open(text_file) as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split(" ")
        if len(numbers) <= 1:
            safe_count += 1
            continue
        if safety_check(numbers):
            safe_count += 1
        
        

print(safe_count)

# Low: 638
# High: 644