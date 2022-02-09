import random
name = "prashuchaudhary"

# generate random number in range 0-size(s)
    # take chanacter at this position and append into new string
    # also keep track of what positions are already taken   

def randomize(s):
    rand = ""
    seen = []

    while len(seen) < len(s):
        pos = random.randint(0, len(s)-1)
        if pos not in seen:
            rand += s[pos]
            seen.append(pos)

    return rand


# pair 

# 10, 22, 28, 29, 30, 40

# 30
# 34
# 54

def closestSum(arr, n):
    left = 0
    right = len(arr)-1
    current_diff =  10 * 10
    items = []

    while left <= right:
        diff = arr[left] + arr[right] - n
        
        if abs(diff) < current_diff:
            current_diff = abs(diff)
            items = [arr[left], arr[right]]

        if diff < 0:
            left += 1
        elif diff == 0:
            break
        else:
            right -= 1

    return items


O(n) time complexity



table student_marks
    - id
    - student_id
    - test_id
    - marks


select * from student_marks where marks < (select max(marks) from student_marks) order by marks desc limit 1

select * from student_marks where marks > (select avg(marks) from student_marks)



