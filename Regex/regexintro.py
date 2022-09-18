import re

email = input("Please enter your email: ")
es="\n"
if re.search(r"^\w+@\w+(\.\w+)?\.com$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

#print("\\\\\n\\\\\n")