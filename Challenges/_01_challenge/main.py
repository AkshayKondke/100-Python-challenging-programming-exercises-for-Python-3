
#  Question
# Write a Python program that finds all numbers divisible by 7 but not a multiple of 5 in the range 2000 to 3200 (both included)

number = []

for num in range(2000, 3201):
    
    if num % 7 == 0 and num % 5 != 0:
        number.append(str(num))

print(", ".join(number))