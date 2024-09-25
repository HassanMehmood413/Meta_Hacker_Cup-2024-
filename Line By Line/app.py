def can_cross_bridge(N, K, S):
    if N == 1:
        return S[0] <= K
    if N == 2:
        return max(S[0], S[1]) <= K

    S.sort()  # Sort the crossing times
    total_time = 0

    while len(S) > 3:
        # Two strategies: 1st and 2nd fastest with slowest
        option1 = S[1] + S[0] + S[-1] + S[1]  # Two fastest go, one returns, two slowest go, fastest returns
        # Strategy: Fastest goes with two slowest, fastest returns, 2nd fastest crosses with the fastest.
        option2 = S[-1] + S[0] + S[-2] + S[0]  # Slowest two go, fastest returns, fastest two go

        # Choose the minimum of the two options
        total_time += min(option1, option2)
        
        # Remove the two slowest people who have crossed the bridge
        S = S[:-2]

    # Handle the last 3 or fewer people
    if len(S) == 3:
        total_time += S[2] + S[0] + S[1]  # 3 people cross: all three go together
    elif len(S) == 2:
        total_time += S[1]  # Just the slowest crossing
    elif len(S) == 1:
        total_time += S[0]  # Only one crossing

    return total_time <= K

def process_test_cases(T, test_cases):
    results = []
    for i, (N, K, S) in enumerate(test_cases, 1):
        result = "YES" if can_cross_bridge(N, K, S) else "NO"
        results.append(f"Case #{i}: {result}")
    return results

# Input handling
T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    S = [int(input()) for _ in range(N)]
    test_cases.append((N, K, S))

# Process and output results
results = process_test_cases(T, test_cases)
for result in results:
    print(result)
