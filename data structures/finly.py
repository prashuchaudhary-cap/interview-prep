Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ arrays length.


def kthLargest(arr, K):
    heap = []
    For i in range(len(arr)):
        heappush(heap, arr[i])

        If i > K:
            heappop(heap)

    Return heappop(heap)



Given a m x n grid filled with non-negative numbers, find a path frm top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


Def minPathSum(mat, m, n):
    Dp = [[0 for i in range(0, m)] for j in range(0, n)]
    Dp[0][0] = mat[0][0]

    For i in range(1, m):
        Dp[0][i] = Dp[0][i-1] + mat[0][i]

    For i in range(1, n):
        Dp[i][0] = Dp[i-1][0] + mat[i][0]

For i in range(1, m):
    For j in range(1, n):
        Dp[i][j] = min(Dp[i-1][j], Dp[i][j-1]) + mat[i][j]

Return Dp[m][n]

