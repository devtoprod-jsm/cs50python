kids = [{"name":"Jai","age":4,"school":"Shemrock"},{"name":"Jashwin","age":1,"school":None}]

for kid in kids:
  print(kid["name"])
x = len(kids)
for i in range(x):
  for j in range(x):
    print("£",end="")
  print()

for i in range(x):
  print("$"*x)