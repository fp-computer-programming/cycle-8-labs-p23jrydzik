# author: JHR 12/6/12

# OG Loop
def sum_to(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

# New While Loop
def sum_to2(n):
    total = 0
    i = 1
    while i < (n+1):
        total += i
        i += 1
    return total

# Test Cases
print(sum_to(1))
print(sum_to2(1))
print(sum_to(2))
print(sum_to2(2))
print(sum_to(3))
print(sum_to2(3))
print(sum_to(4))
print(sum_to2(4))
print(sum_to(10))
print(sum_to2(10))
print(sum_to(100))
print(sum_to2(100))