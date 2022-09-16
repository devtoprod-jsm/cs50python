students= []
with open("students.csv","r") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        #print(name)
        students.append({"name":name,"house":house})

def get_name(student):
    return student["name"]
#print(sorted(students,key=get_name,reverse=True))

print(sorted(students,key=lambda student:student["name"]))

