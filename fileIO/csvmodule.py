import csv
students=[]
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for line in reader:
        students.append({"name" : line[0],"house" : line[1]})

for student in sorted(students,key=lambda student : student["name"]):
    print(student["name"],student["house"])

newstudents = []
with open("students.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        newstudents.append({"name":row["name"],"house":row["house"]})

for student in sorted(newstudents,key=lambda student : student["name"]):
    print(student["name"],student["house"])

with open("csvwrite.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","house"])
    for line in newstudents:
        writer.writerow({"house":line["house"],"name":line["name"]})