def main():
    try:
        num1 = input("Enter the first number")
        numb2 = input("Enter the second number")

        num1 = int(num1)
        numb2 = int(numb2)

        sum = num1 + numb2
        print(f"sum: {sum}")

        div = num1 / numb2
        print(f"Division: {div}")
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Cannot divide by zero")
if __name__ == "__main__":
    main()