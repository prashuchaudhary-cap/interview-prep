There are two aspects to DP -

1. Identifying your states
2. Identifying your recurrence relation with those states


///// Given denominations D [1, 2], find the number of ways amount A 4 can be possibly made out using D uniquely : 3.x


n = 1001
denom = [1,3,4]
dp = [-1 for i in range(n+1)]

def coin(n):
    if dp[n] != -1:
        return dp[n]

    if n <= 0:
        return 0

    if n in denom:
        return 1

    ans = 10**10
    for i in denom:
        if n-i >= 0:
            ans = min(ans, 1 + coin(n-i))

    dp[n] = ans
    return ans

n = 4
w = 5
dp = [ [ -1 for j in range(n+1) ] for i in range(w+1) ]
wts = [2, 1, 3, 1]
vals = [3, 2, 1, 1]


# It’s important to note that we’ve defined f(idx, weight) to be the maximum value we can obtain
# assuming we’re at index idx with weight weight left over.


def weight(weightleft, idx):
    if dp[weightleft][idx] != -1:
        return dp[weightleft][idx]

    if idx >= n:
        return 0

    ans = weight(weightleft, idx+1)

    if wts[idx] <= weightleft:
        ans = max(ans, vals[idx] + weight(weightleft - wts[idx], idx+1))

    dp[weightleft][idx] = ans

    return ans



def allowed(i, j, x, y, banned_set):
    s = "{} {} {} {}"
    options = [
        s.format(i, j, x, y),
        s.format(x, y, i, j)
     ]

    for opt in options:
        if opt in banned_set:
            return False
    return True

def calc(lst, i, j, banned_set):
    result = 0
    if i-1 >= 0 and allowed(i, j, i-1, j, banned_set):
            result += lst[i-1][j]
    if j-1 >= 0 and allowed(i, j, i, j-1, banned_set):
            result += lst[i][j-1]

    return result

def avoid_roads(n, m, banned_set):
    n += 1
    m += 1

    matrix = [[0 for _ in range(m)] for _ in range(n)]
    matrix[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue

            matrix[i][j] = calc(matrix, i, j, banned_set)

    return matrix[-1][-1]


donations = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def neighbours(arr):
    n = len(arr)
    dp = [-1 for i in range(n+1)]

    for i in range(n):
        if i in [0, 1]:
            dp[i] = arr[i]
            continue

        max_sum = -1
        for j in range(i-1):
            max_sum = max(max_sum, dp[j])

            dp[i] = max_sum + arr[i]

    return max(dp)



arr = [9, 1, 2, 5, 4, 5, 1, 2, 3, 4, 1, 2, 5]

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < (dp[j] + 1):
                dp[i] = dp[j] + 1

    return max(dp)


# This problem is a variation of standard Longest Increasing Subsequence (LIS)
# All we need to change is to use sum as a criteria instead of length of increasing subsequence.
def longest_sum_increasing_subsequence(arr):
    n = len(arr)
    dp = [arr[i] for i in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < (dp[j] + arr[i]):
                dp[i] = dp[j] + arr[i]

    return max(dp)


X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)

dp = [ [0 for j in range(n+1)] for i in range(m+1) ]

def longest_common_subsequence(X, Y, m, n):
    if dp[m][n] != 0:
        return dp[m][n]

    if m == len(X) or n == len(Y):
       return 0

    elif X[m] == Y[n]:
       ans = 1 + longest_common_subsequence(X, Y, m+1, n+1)
    else:
       ans = max(longest_common_subsequence(X, Y, m, n+1), longest_common_subsequence(X, Y, m+1, n))

    dp[m][n] = ans

    return ans


def longest_common_subsequence_1(X, Y):
    m = len(X)
    n = len(Y)

    # Create and initialize DP table
    dp = [[0 for k in range(n+1)] for l in range(m+1)]

    # Fill dp table (similar to LCS loops)
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If characters match and indices are not same
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            # If characters do not match
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[m][n]



# LCS(str, str) where str is the input string with the restriction that when both the characters are same,
# they shouldn’t be on the same index in the two strings

def longest_repeating_sequence(str):
    n = len(str)
    # Create and initialize DP table
    dp = [[0 for k in range(n+1)] for l in range(n+1)]

    # Fill dp table (similar to LCS loops)
    for i in range(1, n+1):
        for j in range(1, n+1):
            # If characters match and indices are not same
            if (str[i-1] == str[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]

            # If characters do not match
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[n][n]

string = "AABEBCDD"
n = len(string)
dp = [ [0 for j in range(n+1)] for i in range(n+1) ]

def longest_repeating_sequence_1(string, m, n):
    if dp[m][n] != 0:
        return dp[m][n]

    if m == len(string) or n == len(string):
       return 0
    elif string[m] == string[n] and m != n:
       return 1 + longest_repeating_sequence_1(string, m+1, n+1)
    else:
       return max(longest_repeating_sequence_1(string, m, n+1), longest_repeating_sequence_1(string, m+1, n))





def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)
