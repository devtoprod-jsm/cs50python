import re
name = input("What is your name? ")

if matches := re.search("^(.+), *(.+)",name):
    name = f"{matches.group(2)} {matches.group(1)}"

print(name)

url = input("Twitter URL: ")
if matched := re.search("^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
    print(matched.group(1))