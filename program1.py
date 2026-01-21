def is_armstrong(num):
    if num < 0:
        return False
    original = num
    n = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** n
        num //= 10
    return total == original
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
