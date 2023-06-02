import os 
#------------------------------------------------------1-masala--------------------------------------------------------
"""
def is_power_of_two(n: int):
    if n == 1:
        return True
    elif n == 0 or n % 2 != 0:
        return False
    else:
        return is_power_of_two(n // 2)
print(is_power_of_two(6345))
"""
#--------------------------------------------------------2-masala-------------------------------------------------
"""
def addDigit(n):
    if n <= 9:
        return n
    return addDigit(sum(int(digit) for digit in str(n)))

print(addDigit(38))
"""
