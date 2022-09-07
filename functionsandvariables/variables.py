fname = input("What is your first name? ").strip().lower().capitalize()
lname = input("What is your last name? ").strip().lower().capitalize()

print(f"Hello, {fname}. {lname}")
print(fname)
print(lname)
print(fname,lname,sep="+++")
print(fname,end="!!!")
print(lname)
print(type(fname))

fullname = input("Fullname please: ")
fname,lname = fullname.split(" ")
print(fname)
print(lname)

print(int(input("number1: ")) + int(input("number2: ")))
print(round(39/7,2))
x=1000.1000
print(f"{x:,}")
print(f"{x:.2f}")

