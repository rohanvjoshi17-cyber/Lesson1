f1 = open('Codingle.txt', 'a+')
f2 = open('Codingal.txt', 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('content of f1 after append - \n', f1.read())
print('content of f2 after append - \n', f2.read())

f1.close
f2.close