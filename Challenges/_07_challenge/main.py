

def generate_2d_array():
    x, y = map(int, input("Enter two numbers separated by comma: ").split(","))

    result = [[i * j for j in range(y)] for i in range(x)]

    print("Generating 2D array...")

    for row in result:
        print(" | ".join(map(str, row)))

generate_2d_array()