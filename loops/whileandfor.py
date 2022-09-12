num = int(input("Number of Jai: "))
print(range(num))
i = 0
while (i < num):
  print("Jai")
  i += 1

for i in range(num):
  print (i)

print("Jai\n"*num,end="")

#validating input
while True:
  n = int(input("Number please "))
  if n >= 0:
    break

for _ in range(n):
  print("Jai")

def main():
  num = getNumber()
  jai(num)
def getNumber():
  while True:
    num = int(input("Give number "))
    if n > 0:
      return num
def jai(num):
  for _ in range(num):
    print("Jai")
main()