# Understand for loop in python

# For example if array a is a = [1,2,3,6,5]
# 1. len(a) will be 5, which is the length of the array
# 2. To get the first value it will be a[0] which is 1
# 3. To get the last value it will be a[len(a)-1]
# 4. To find the index values of the array, you will have to iterate (for loop) through the array


a = [3, 2, 3, 6, 5]

print(len(a))  # 5
print(a[0])  # 3
print(len(a)-1)  # 4
print(a[len(a)-1])  # 5

for i in range(1, len(a)):
    print(i)
# output = 1 2 3 4 (Start from index 1 to last index of the array)
