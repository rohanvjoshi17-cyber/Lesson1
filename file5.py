file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(9))
file.close()

file = open('Codingal.txt', 'a')
file.write(",I am in 9th Grade")
file.close()