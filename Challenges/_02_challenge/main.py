
# question
# Compute Factorial of a Number


# normal method
num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"Factorial calculation form normal method  : {factorial}")



#  Recursive method solution
def fact_cal(num):
    if num == 0 or num == 1:
        return 1   
    return num * fact_cal(num - 1)

print(f"Factorial calculation from Recursive method: {fact_cal(num)}")