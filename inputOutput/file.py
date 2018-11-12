jabber = open("sample.txt", 'r')

for line in jabber:
   if "jabberwock" in line.lower():
        print(line, end="")

jabber.close()

with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")

with open("sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

with open("sample.txt", 'r') as jabber:
    line = jabber.readlines()
print(line)

for lines in line:
    print(lines,end="")

with open("sample.txt", 'r') as jabber:
    line = jabber.readlines()
print(line)

for lines in line[::-1]:
    print(lines,end="")


with open("sample.txt", 'r') as jabber:
    line = jabber.read()

print(line)
for lines in line[::-1]:
    print(lines,end="")