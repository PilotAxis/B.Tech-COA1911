#You are given an array `arr` of `n` integers. Your task is to find the minimum number of subsets whose sum is equal to a target number `K`. If no such subsets exist, return `-1`. Also, print those subsets.

def minSubsets(arr, n, K):
    # Initialize the DP table
    dp = [[0 for _ in range(K + 1)] for _ in range(n + 1)]
    path = [[[] for _ in range(K + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(n + 1):
        for j in range(K + 1):
            # If sum is 0, then answer is 0
            if j == 0:
                dp[i][j] = 0
            # If there are no elements and sum is not 0, then answer is infinity
            elif i == 0:
                dp[i][j] = float('inf')
            # If the current element's value is greater than the current sum j, 
            # then we exclude the current element
            elif arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
                path[i][j] = path[i - 1][j]
            # Else, we consider two cases, one where we exclude the current element
            # and one where we include the current element and take the minimum of both
            else:
                exclude = dp[i - 1][j]
                include = 1 + dp[i - 1][j - arr[i - 1]]
                if include < exclude:
                    dp[i][j] = include
                    path[i][j] = path[i - 1][j - arr[i - 1]] + [arr[i - 1]]
                else:
                    dp[i][j] = exclude
                    path[i][j] = path[i - 1][j]
    
    # If the final answer is infinity, then no subset sums up to K
    if dp[n][K] == float('inf'):
        return -1, []
    else:
        return dp[n][K], path[n][K]

# Test the function
arr = [2, 5, 1, 2, 3, 4, 5, 9, 6, 3, 1, 4, 2, 2, 2, 6]
K = 9
n = len(arr)
print(minSubsets(arr, n, K))  # Output: 2


'''Constraints:

- `1 <= T <= 100`
- `1 <= n <= 10^4`
- `-10^9 <= arr[i] <= 10^9`
- `1 <= K <= 10^9`
'''

# Time Complexity: O(n * K)
# Space Complexity: O(n * K)