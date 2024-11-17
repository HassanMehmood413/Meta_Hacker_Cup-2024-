def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    index = 0
    T = int(lines[index].strip())  # Read the number of test cases
    index += 1
    test_cases = []
    
    for _ in range(T):
        N = int(lines[index].strip())  # Read the number of points for this test case
        index += 1
        points = []
        
        for i in range(N):
            x, y = map(int, lines[index].strip().split())  # Read each point
            points.append((x, y))
            index += 1
        
        test_cases.append(points)  # Store each test case's points
    
    return test_cases

def is_collinear(points):
    if len(points) <= 2:
        return True  # Two or fewer points are always collinear
    
    x0, y0 = points[0]
    for i in range(1, len(points)):
        x1, y1 = points[i]
        # Check if the slope between points (x0, y0) and (x1, y1) is consistent
        if (x1 - x0) * (points[1][1] - y0) != (points[1][0] - x0) * (y1 - y0):
            return False
    return True

def solve(points):
    # Check if all points are collinear
    return "YES" if is_collinear(points) else "NO"

def write_output(file_path, results):
    with open(file_path, 'w') as f:
        for i, result in enumerate(results):
            f.write(f"Case #{i + 1}: {result}\n")

input_file_path = r'd:\meta hacker cup 2024\End\input.txt'
output_file_path = r'd:\meta hacker cup 2024\End\output.txt'

test_cases = read_input(input_file_path)
results = [solve(points) for points in test_cases]
write_output(output_file_path, results)
