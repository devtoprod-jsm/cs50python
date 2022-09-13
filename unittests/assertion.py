from square import square


def square_test():
    try:
        assert square(2) == 4
    except AssertionError:
        print("square of 2 is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Square of 3 is not 9")


def main():
    square_test()


if __name__ == "__main__":
    main()