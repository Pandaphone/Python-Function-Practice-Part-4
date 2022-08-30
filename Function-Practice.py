# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    numList = [a, b, c]
    max = 0
    for i in numList:
        if max < i:
            max = i
    print(max)


max_num(10, 5, 7)

# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(list):
    start = 1

    for i in list:
        start = start * i
    print(start)


lists = [1, 2, 7]
mult_list(lists)

# Write a Python function called rev_string() to reverse a string.


def rev_string(a_Str):
    return a_Str[::-1]


print(rev_string("HERE IS A GOOD ONE!"))


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.


def num_within(a, b, c):
    return a in range(b, c+1)


print(num_within(3, 1, 3))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first-
# -imagined by Blaise Pascal. Each number is the two numbers above it added together.

# def pascal(n):
# for i in n:
