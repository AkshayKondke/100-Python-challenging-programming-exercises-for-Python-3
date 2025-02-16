import math


print("----------------------||||||||||||||||||--------------------------")
print("\n")

print("\t \tWelcome to the challenge no 06.")

C = 50
H = 30

D_value = input("Enter the value of the D variable for comma separated value: ").split(",")

Q_value = [round(math.sqrt((2 * C * int(D)) / H)) for D in D_value]

print(",".join(map(str, Q_value)))

# print(Q_value)