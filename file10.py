new_file = open('Coding.txt', 'x')
new_file.close()

import os
print("Checking if my_file exists or not....")
if os.path.exists("Coding3.txt"):
    os.remove("Coding3.txt")
else:
    print("The file does not exist")

my_file = open("my_file.txt","w")
my_file.write("Hi!, I am Rohan and i am 14 yr old.")
my_file.close()
os.remove('Coding.txt')
os.rmdir('Folder')