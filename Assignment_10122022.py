# Pattern #1: Simple Number Triangle Pattern
# Pattern:
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  

n = 5

for digit in range(n):

    for k in range(digit):

        print(digit, end=" ")

    print(" ")

# Pattern #2: Inverted Pyramid of Numbers
# Pattern:
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

n = 5

m = 0

for k in range(n, 0, -1):

    m += 1

    for n in range(1, k + 1):

        print(m, end=' ')

    print('\r')

# Pattern #3: Half Pyramid Pattern of Numbers
# Pattern:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

n = 5

for n in range(1, n+1):

    for m in range(1, n + 1):

        print(m, end=" ")

    print(" ")

# Pattern #4: Inverted Pyramid of Descending Numbers
# Pattern:
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

n = 5

for k in range(n, 0, -1):

    digit = k

    for m in range(0, k):

        print(digit, end=' ')

    print("\r")

# Pattern #5: Inverted Pyramid of the Same Digit
# Pattern:
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5


n = 5

digit = n

for k in range(n, 0, -1):

    for m in range(0, k):

        print(digit, end=' ')

    print("\r")


# Pattern #6: Reverse Pyramid of Numbers
# Pattern:
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

n = 6

for r in range(1, n):

    for m in range(r, 0, -1):

        print(m, end=' ')

    print("")

# Pattern #7: Inverted Half Pyramid Number Pattern
# Pattern:
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1

n = 5

for k in range(n, 0, -1):

    for m in range(0, k + 1):

        print(m, end=' ')

    print("\r")

# Pattern #8: Pyramid of Natural Numbers Less Than 10
# Pattern:
# 1 
# 2 3 4 
# 5 6 7 8 9

curr = 1

end = 2

n = 3

for k in range(n):

    for m in range(1, end):

        print(curr, end=' ')

        curr += 1

    print("")

    end += 2

# Pattern #9: Reverse Pattern of Digits from 10 
# Pattern:
# 1
# 3 2
# 6 5 4
# 10 9 8 7

beg = 1

end = 1

curr = end

for r in range(1, 6):

    for c in range(beg, end):

        curr -= 1

        print(curr, end=' ')

    print("")

    beg = end

    end += r

    curr = end


# Pattern #10: Unique Pyramid Pattern of Digits
# Pattern:
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

n = 6

for k in range(1, n + 1):

    for m in range(1, k-1):

        print(m, end=" ")

    for m in range(k-1, 0, -1):

        print(m, end=" ")

    print()


# Pattern #11: Connected Inverted Pyramid Pattern of Numbers
# Pattern:
# 5 4 3 2 1 1 2 3 4 5 
# 5 4 3 2 2 3 4 5 
# 5 4 3 3 4 5 
# 5 4 4 5 
# 5 5

rows = 6

for i in range(0, rows):

    for j in range(rows - 1, i, -1):

        print(j, end=" ")

    for l in range(i):

        print("", end="")

    for k in range(i + 1, rows):

        print(k, end=" ")

    print('\n')

# Pattern #12: Even Number Pyramid Pattern
# Pattern:
# 10 
# 10 8 
# 10 8 6 
# 10 8 6 4 
# 10 8 6 4 2

n = 5

last_even = 2 * n

even_num = last_even

for k in range(1, n+1):

    even_num = last_even

    for m in range(k):

        print(even_num, end=' ')

        even_num -= 2

    print("\r")

# Pattern #13: Pyramid of Horizontal Tables
# Pattern:
# 0  
# 0 1  
# 0 2 4  
# 0 3 6 9  
# 0 4 8 12 16  
# 0 5 10 15 20 25  
# 0 6 12 18 24 30 36

n = 7

for k in range(0, n):

    for m in range(0, k + 1):

        print(k * m, end=' ')

    print()

# Pattern #14: Pyramid Pattern of Alternate Numbers
# Pattern:
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9

n = 5

k = 1

while k <= n:

    m = 1

    while m <= k:

        print((k*2-1), end=" ")

        m = m + 1

    k = k + 1

    print()



# Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
# Pattern:
#            1 
#          1 2 
#       1 2 3 
#    1 2 3 4 
#  1 2 3 4 5

n = 6

for r in range(1, n):

    digit = 1

    for m in range(n, 0, -1):

        if m > r:

            print(" ", end=' ')

        else:

            print(digit, end=' ')

            digit += 1

    print("")

# Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)
# Pattern:
#             *   
#            * *   
#           * * *   
#          * * * *   
#         * * * * *   
#        * * * * * *   
#       * * * * * * *

s = 7

y = (2 * s)-2

for k in range(0, s):

    for m in range(0, y):

        print(end=" ")

    y = y-1 

    for m in range(0, k + 1):

        print("* ", end=' ')

    print(" ")


# Pattern #17: Downward Triangle Pattern of Stars
# Pattern:
#         * * * * * * 
#          * * * * * 
#           * * * * 
#            * * * 
#             * * 
#              * 


n = 5

s = 2 * n-2

for k in range(n, -1, -1):

    for m in range(s, 0, -1):

        print(end=" ")

    s = s + 1

    for m in range(0, k + 1):

        print("*", end=" ")

    print("")

 
#   Pattern #18: Pyramid Pattern of Stars
# Pattern:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

n = 5

for k in range(0, n):

    for m in range(0, k + 1):

        print("*", end=' ')

    print("\r")
