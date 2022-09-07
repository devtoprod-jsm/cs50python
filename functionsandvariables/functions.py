def main():
  name = input("Your name ")
  hello(name)

def hello(to):
  print("Hello", to)

main()

def niam():
  num = int(input("Number please "))
  print(square(num))

def square(num):
  return pow(num,2)

niam()