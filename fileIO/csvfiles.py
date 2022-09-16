with open("students.csv","r") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(name)
        print(line.split(","))
        print(f"{name} belongs to {house}")