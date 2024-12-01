import time 

# PART 1 : Function to calculate the total distance between two lists of numbers
def calculate_total_distance(filename):
    # Read and parse input
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance
    total_distance = 0
    for l, r in zip(left_list, right_list):
        total_distance += abs(l - r)
    
    return total_distance

# PART 2 : Function to calculate the similarity score between two lists of numbers
def calculate_similarity_score(filename):
    left_list = []
    right_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
    
    # Count occurrences in right list
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1
    
    # Calculate similarity score
    total_score = 0
    for num in left_list:
        total_score += num * right_counts.get(num, 0)
    
    return total_score

def main() : 
    
    # Part 1
    result = calculate_total_distance('input.txt')
    print(f"Total distance: {result}")
    
    # Part 2
    result = calculate_similarity_score('input.txt')
    print(f"Similarity score: {result}")

if __name__ == "__main__" :
    time_start = time.time()
    main()
    time_end = time.time()
    print("Time: ", time_end - time_start)
    