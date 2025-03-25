def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    n = input("Enter a number for calculating factorial, or press 'q' to exit: ")

    if n.lower() == 'q':
        print("Exiting...")
        break

    try:
        n = int(n)

        if n == 0:
            print("Factorial of 0 is 1")
            continue
        elif n < 0:
            print("Factorial of negative number is not possible.")
            continue

        print("Factorial of", n, "is", factorial(n))

    except ValueError:
        print("Invalid input. Please enter a valid whole number.")