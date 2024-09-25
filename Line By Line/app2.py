import math

def solve():
    T = int(input())  # number of test cases
    for t in range(1, T + 1):
        # Read input values
        N, P = map(int, input().split())
        
        # Calculate the new probability P'
        P_prime = 100 * (P / 100) ** ((N - 1) / N)
        
        # Calculate the increase in probability
        increase = P_prime - P
        
        # Print the result with required precision
        print(f"Case #{t}: {increase:.12f}")

# Sample Input
solve()