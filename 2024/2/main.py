import time 

def is_safe(levels):
    if len(levels) < 2:
        return True
        
    # Check if increasing or decreasing
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    is_increasing = all(d > 0 for d in differences)
    is_decreasing = all(d < 0 for d in differences)
    
    # Check adjacent differences
    valid_diffs = all(1 <= abs(d) <= 3 for d in differences)
    
    return (is_increasing or is_decreasing) and valid_diffs

def is_safe_with_dampener(levels):
    # First check if already safe without modification
    if is_safe(levels):
        return True
        
    # Try removing each level one at a time
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]  # Create new list without level at index i
        if is_safe(modified_levels):
            return True
            
    return False

def count_safe_reports(filename, use_dampener=False):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            if use_dampener:
                safe_count += is_safe_with_dampener(levels)
            else:
                safe_count += is_safe(levels)
    return safe_count


def main():
    result1 = count_safe_reports('input.txt')
    print(f"Part 1 - Safe reports: {result1}")
    
    result2 = count_safe_reports('input.txt', use_dampener=True)
    print(f"Part 2 - Safe reports with dampener: {result2}")

if __name__ == "__main__":
    time_start = time.time()
    main()
    time_end = time.time()
    print("Time:", time_end - time_start)