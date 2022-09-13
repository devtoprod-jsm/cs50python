from square import square


def square_test():
    if square(2) != 4:
        print("Square of 2 is not 4")
    if square(3) != 9:
        print("Square of 3 is not 9")


def main():
    square_test()


if __name__ == "__main__":
    main()