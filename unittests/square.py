def square(num):
    return num*num


def main():
    num = int(input("What's the number? "))
    print(f"{num} squared is {square(num)}")


if __name__ == "__main__":
    main()