Gcd question

# Given an array of length n, find the maximum sum of k elements by traversing only via the start and end of the array (k corner elements).
# e.g. array = [1,5,6,78,9,0,9,99,8]
# k=4
# Ans - 8+99+9+1

# Function to return maximum sum
def maxCronerPointCount(arr, K, size):
 
    # Initialize variables
    curr_points = 0
    max_points = 0
 
    # Iterate over first K elements
    # of array and update the value
    # for curr_points
    for i in range(K):
        curr_points += arr[i]
 
    # Update value for max_points
    max_points = curr_points
 
    # j points to the end of the array
    j = size - 1
 
    for i in range(K - 1, -1, -1):
        curr_points = (curr_points +
                       arr[j] - arr[i])
        max_points = max(curr_points,
                         max_points)
        j -= 1
 
    # Return the final result
    return max_points    


# Trapping Rain Water
def findWater(arr, n):
 
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n
 
    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n
 
    # Initialize result
    water = 0
 
    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])
 
    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);
 
    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]
 
    return water
time - O(n)
space - O(n)


def findWater(arr, n):
 
    # initialize output
    result = 0
      
    # maximum element on left and right
    left_max = 0
    right_max = 0
      
    # indices to traverse the array
    lo = 0
    hi = n-1
      
    while(lo <= hi):
     
        if(arr[lo] < arr[hi]):
         
            if(arr[lo] > left_max):
 
                # update max in left
                left_max = arr[lo]
            else:
 
                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo+= 1
         
        else:
         
            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-= 1
         
    return result
time - O(n)
space - O(1)

# Longest Increasing Subsequence

# Longest Common Subsequence
# Dynamic Programming implementation of LCS problem
 
def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs
 
 
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is 4", lcs(X, Y)
O(mn)


# Max level sum in tree

# Fill rows and columns with 0 problem

# Sum of a binary tree.

# Level Order traversal of Binary tree

# Sort binary array, in 1 pass


@ Design Parking Lot

@ Internal working of HashMap aand HashSet

@ Implement - factory, factory method, builder and singleton design pattern, make singleton thread safe.


9. What is synchronization and how it is implemented in java?
10. What is serialization in Java
11. What is a double lock, and why it is used?
12. What is a concurrent hashmap, with internal working?

https://www.interviewbit.com/java-interview-questions/
https://www.interviewbit.com/java-8-interview-questions/
https://www.interviewbit.com/spring-boot-interview-questions/
https://www.interviewbit.com/oops-interview-questions/

@ Explain the flow of a spring boot application

@ How to do unit testing inn spring boot

@ What are spring actuators

@ Different annotations inn spring boot

@ How do cron jobs work
 
@ How do we scale a spring boot application

@ Design Bookmyshow

@ Design a Rate Limiter

@ Twitter design

@ concurrency annd oops principles

