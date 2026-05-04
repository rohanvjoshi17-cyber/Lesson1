file = open('Codingle.txt')
c = 0
ct = file.read()
cl = ct.split("\n")

for i in cl:
    if i:
        c += 1

print("This is the number of lines in the file")
print(c)