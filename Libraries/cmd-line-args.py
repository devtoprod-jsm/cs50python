import sys
print(sys.argv[0])
if len(sys.argv) < 2:
    sys.exit("Not enough args")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")
#for i in range (int(sys.argv[1])):
#    print(i+1 , "#" * (i+1))
for i in sys.argv[::-1]:
    print(i)

print(f"{1.56789:.2f}")