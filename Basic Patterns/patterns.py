# Question1:
class Solution:
    def printSquare(self, N):
        # Code here

        for i in range(0, N, 1):
            for j in range(0, N, 1):
                print("* ", end="")
            print()

# Expected Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# Question2:


class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(0, N, 1):
            for j in range(0, i+1):
                print("*", end=" ")
            print()

# Expected Output:
# *
# * *
# * * *
# * * * *
# * * * * *

# Question3:


class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()

# Expected Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Question4:


class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(i, end=" ")
            print()
# Expected Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Question5:


class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N, 0, -1):
            for j in range(i+1, 1, -1):
                print("*", end=" ")
            print()

# Expected Output:
# * * * * *
# * * * *
# * * *
# * *
# *
