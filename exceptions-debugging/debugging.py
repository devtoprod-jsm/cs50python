def get_height():
     return int(input("Give height: "))

def main():
    for i in range(get_height()):
        print("#" * (i+1))

if __name__ == "__main__":
    main()