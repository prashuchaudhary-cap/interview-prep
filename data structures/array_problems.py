
# Minimum number of operation required to convert number x into y
# Operations
# 1. Multiply number by 2.
# 2. Subtract 1 from the number.

def min_operations(x, y):
    # If both are equal then return 0
    if x == y:
        return 0
 
    # Check if conversion is possible or not
    if x <= 0 and y > 0:
        return -1
 
    # If x > y then we can just increase y by 1
    # Therefore return the number of increments required
    if x > y:
        return a-b
 
    # If last bit is odd
    # then increment y so that we can make it even
    if y & 1 == 1:
        return 1+min_operations(x, y+1)
 
    # If y is even then divide it by 2 to make it closer to x
    else:
        return 1+min_operations(x, y//2)
 
 
# Driver code
print(min_operations(4, 7))




# Function to return max sum such that
# no two elements are adjacent

def find_max_sum(arr):
    incl = 0
    excl = 0
    
    for i in arr:         
        # Current max excluding i
        new_excl = max(excl, incl)
        
        # Current max including i
        incl = excl + i

        excl = new_excl
     
    # return max of incl and excl
    return max(excl, incl)
 
# Driver program to test above function
arr = [5, 5, 10, 100, 10, 5]


def binarySearch(arr, x):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present

    return -1


def ternarySearch(key, ar):
    l = 0
    r = len(arr)-1

    while r >= l:

        # Find mid1 and mid2
        mid1 = l + (r-l) // 3
        mid2 = r - (r-l) // 3

        # Check if key is at any mid
        if key == ar[mid1]:
            return mid1
        if key == mid2:
            return mid2

        # Since key is not present at mid,
        # Check in which region it is present
        # Then repeat the search operation in that region
        if key < ar[mid1]:
            # key lies between l and mid1
            r = mid1 - 1
        elif key > ar[mid2]:
            # key lies between mid2 and r
            l = mid2 + 1
        else:
            # key lies between mid1 and mid2
            l = mid1 + 1
            r = mid2 - 1

    return -1


# Python 3 implementation to find the
# index of first 1 in an infinite
# sorted array of 0's and 1's

# function to find the index of first
# '1' binary search technique is applied
def indexOfFirstOne(arr, low, high) :

    while (low <= high) :

        mid = low + (high - low) // 2

        # if true, then 'mid' is the index
        # of first '1'
        if (arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0)):
            break

        # first '1' lies to the left of 'mid'
        elif (arr[mid] == 1):
            high = mid - 1

        # first '1' lies to the right of 'mid'
        else:
            low = mid + 1

    # required index
    return mid

# function to find the index of first
# 1 in an infinite sorted array of 0's
# and 1's
def posOfFirstOne(arr) :

    # find the upper and lower bounds between which the first '1' would be present
    l = 0
    h = 1

    # as the array is being considered infinite therefore 'h' index will always exist in the array
    while (arr[h] == 0) :
        # lower bound
        l = h

        # upper bound
        h = 2 * h

    # required index of first '1'
    return indexOfFirstOne(arr, l, h)


def isPrime(n) :
    # we can check till sqrt(n) because a larger factor of n must be a multiple of smaller factor that has been already checked
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True



# Function to find length of longest sublist with alternating
# positive and negative elements
def findLongestSubList(A):

    # stores length of longest alternating sublist found so far
    maxLen = 1

    # stores ending index of longest alternating sublist found so far
    endIndex = 0

    # stores length of longest alternating sublist ending at current position
    currLen = 1

    # traverse the given list starting from the second index
    for i in range(1, len(A)):

        # if current element has opposite sign than the previous element
        if A[i] * A[i - 1] < 0:

            # include current element in longest alternating sublist ending at
            # previous index
            currLen = currLen + 1

            # update result if current sublist length is found to be greater
            if currLen > maxLen:
                maxLen = currLen
                endIndex = i

        # reset length if current element has same sign as previous element
        else:
            currLen = 1

    sublist = A[endIndex - maxLen + 1: endIndex + 1]


def kadane(A):
    # find maximum element present in given list
    maximum = max(A)

    # if list contains all negative values, return maximum element
    if maximum < 0:
        return maximum

    # stores maximum sum sublist found so far
    maxSoFar = 0

    # stores maximum sum of sublist ending at current position
    maxEndingHere = 0

    # do for each element of the given list
    for i in A:
        # update maximum sum of sublist "ending" at index i (by adding
        # current element to maximum sum ending at previous index i-1)
        maxEndingHere = maxEndingHere + i

        # if maximum sum is negative, set it to 0 (which represents
        # an empty sublist)
        maxEndingHere = max(maxEndingHere, 0)

        # update result if current sublist sum is found to be greater
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar


# Function to count the number of strictly increasing sublists in a list
def getCount(A):

    # stores the count of strictly increasing sublists
    count = 0

    # stores the length of current strictly increasing sublist
    length = 1

    # traverse the list from left to right starting from the 1st index
    for i in range(1, len(A)):

        # if previous element is less than the current element
        if A[i - 1] < A[i]:
            # add the length of current strictly increasing sublist
            # to the answer and increment it
            count += length
            length = length + 1
        else:
            # reset the length to 1
            length = 1

    # return the count of strictly increasing sublists
    return count


# Find minimum number of moves required for converting a given list
# to a list of zeroes using only decrement and reduce operation.
def countMoves(A):

    # stores the count of minimum moves required
    min_moves = 0

    # loop till all elements of the list are not 0
    while True:

        # stores count of 0's in current list
        no_of_zeroes = 0

        # traverse the list
        for i in range(len(A)):
            # convert all odd numbers to even by reducing their value by 1
            # for each odd value, increment number of moves required
            if A[i] % 2 == 1:
                A[i] = A[i] - 1
                min_moves = min_moves + 1

            # increment zeroes count if current element becomes 0
            if A[i] == 0:
                no_of_zeroes = no_of_zeroes + 1

        # break the loop if elements in the list becomes 0
        if no_of_zeroes == len(A):
            break

        # Since each element in the list is even at this point,
        # divide each element by 2
        for j in range(len(A)):
            A[j] = A[j] // 2

        # increment number of moves by 1 for above divide operation
        min_moves = min_moves + 1

    # return count of minimum moves required
    return min_moves


# find maximum contiguous subarray
def maximumContiguousSubArray(arr):
    size = len(arr)
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far



def maximumContiguousSubArray2(arr):
    size = len(arr)
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1,size):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


# sort array with binary values
def sortBinaryArray(arr):
    n = len(arr)
    j = -1
    for i in range(n):
        # if number is smaller
        # than 1 then swap it
        # with j-th number
        if arr[i] < 1:
            j = j + 1
            arr[i], arr[j] = arr[j], arr[i]


# Python program to sort an array with
# 0, 1 and 2 in a single pass

# Function to sort array
def sort012(arr):
    size = len(arr)
    lo = mid = 0
    hi = size - 1

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi = hi - 1

    return arr


# Flatten a list of nested lists

from collections import deque


arr = [1, 2, [3, [4, 5, 6, [7]], 8, 9, [1, 2, [3, 4]]], 4, 5, [6, [7]]]

def flatten(l):
    if isinstance(l, collections.Iterable):
        return [a for i in l for a in flatten(i)]
    else:
        return [l]

def iterative_flatten(li):
    nested = deque(li)
    res = []
    dq = deque()

    while nested or dq:
        x = dq.pop() if dq else nested.popleft()
        dq.extend(reversed(x)) if isinstance(x, list) else res.append(x)

    return res


