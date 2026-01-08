def number_pattern(n):
    # Check if n is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."

    # Check if n is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."

    # Generate pattern
    result = ""
    for i in range(1, n + 1):
        result += str(i) + " "

    return result.strip()


def main():
    print("=== Number Pattern Generator ===")

    user_input = input("Enter a positive integer: ")

    # Validate input before calling function
    try:
        n = int(user_input)
    except ValueError:
        print("Argument must be an integer value.")
        return

    output = number_pattern(n)
    print("Result:")
    print(output)


# Program entry point
if __name__ == "__main__":
    main()
