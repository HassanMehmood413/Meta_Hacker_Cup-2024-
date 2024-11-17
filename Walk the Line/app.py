def solve():
    import sys

    # Set the default input filename
    input_filename = 'input.txt'

    # Open the input file
    with open(input_filename, 'r') as input_source:
        data = input_source.read().splitlines()

    T = int(data[0])  # number of test cases
    output = []

    index = 1
    for t in range(1, T + 1):
        # Read the values of N and K
        N, K = map(int, data[index].split())
        index += 1
        S = [int(data[index + i]) for i in range(N)]
        index += N
        
        # Sorting the times for optimal crossings
        S.sort()

        # Simulate the crossing strategy and calculate the total time
        total_time = 0

        if N == 1:
            total_time = S[0]
        elif N == 2:
            total_time = S[1]
        else:
            while len(S) > 3:
                a, b = S[0], S[1]  # Two fastest
                c, d = S[-2], S[-1]  # Two slowest
                total_time += 2 * b + a + d
                S = S[:-2]

            if len(S) == 3:
                total_time += S[2] + S[1] + S[0]
            elif len(S) == 2:
                total_time += S[1]
            elif len(S) == 1:
                total_time += S[0]

        if total_time <= K:
            output.append(f"Case #{t}: YES")
        else:
            output.append(f"Case #{t}: NO")

    # Write the output to a file
    with open("output.txt", "w") as f:
        f.write("\n".join(output))

# Example usage
if __name__ == "__main__":
    solve()
