N = 121
rev = 0
dup = N  # Initalizing dup to check if number is palindrome or not

# Reverse a number
while N > 0:
    digit = N % 10
    rev = rev * 10 + digit  # important formula
    N = N//10
print(rev)

# below condition is to check if number is palindrome
if dup == rev:
    print("true")
else:
    print("false")
