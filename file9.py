with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am Rohan and I am 14 yr old.")
file.close()

with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are.....")
    for line in data:
        word = line.split()
        print (word)
file.close()