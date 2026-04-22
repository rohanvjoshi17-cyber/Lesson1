tuple = ()
print(tuple)

tuple = (1, 2, 3)
print(tuple)

tuple = (1, "Hello", 3.4)
print(tuple)

tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(tuple)

tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(tuple[0])
print(tuple[5])

n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])

print("Sliced :", tuple[1:4])

for letter in (tuple):
    print("Hello", letter)