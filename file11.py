OutFile = open('UpdatedFile.txt', "w")
InpFile = open('Repeated.txt', "r")

LSNF = set()
print("Eliminating duplicate lines")
for line in InpFile:
    if line not in LSNF:
        OutFile.write(line)
        LSNF.add(line)

OutFile.close()
InpFile.close()