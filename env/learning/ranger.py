def read_int(prompt, min, max):
    #
    # Write your code here.
    #

    try:
        num = int(input("Enter a number from -10 to 10: " ))
    except ValueError as ex:
        return f"wrong input, the cause might be `{ex}`"

    min = -10
    max = 10

    try:
        if num < min or num > max:
            return f" {num}, it is not in permitted range (-10, 10)"
        else:
            return num
    except ValueError as ex:
        print(f"{ex} Wrong number {num} enter")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

