fileR = open('Codingle.txt','r')
print("------ Reading File ------   ")
print(fileR.read())
fileR.close()

fileW = open('Codingle.txt', 'w')
fileW.write("------ Overwriting File ------   ")
fileW.write("Hi! I am Rohan, I am 14 yrs old!")
fileW.close()

fileA = open('Codingle.txt', 'a')
fileA.write("\n ------ Appending File ------   ")
fileA.write("Hi!,I am Rohan, I am 14 yrs old!")
fileA.close()