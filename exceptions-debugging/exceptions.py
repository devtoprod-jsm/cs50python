def get_int():
    while True:
        try:
          x = int(input("Give me a number: "))
        except ValueError:
          print(f"Your input is not a integer")
        else:
          return x

def main():
    print(get_int())

if __name__ == "__main__":
    main()