name = input("What's your name? ")

file = open("names1.txt","a")
file.write(f"{name}\n")
file.close()

with open("names2.txt","a") as file:
    file.write(name)

with open("names1.txt","r") as file:
    for line in sorted(set(file)):
        print(f"{line.rstrip()}")