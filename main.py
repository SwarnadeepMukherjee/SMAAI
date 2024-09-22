import os

print('''
Tasks to perform:
    1. List chapters
    2. Show Status
''')

t = "a"

while (True):
        try:
            t = int(input("What do you want to perform?: "))
            break
        except Exception as e:
            print()
            print("Invalid Input")
            print()
            print("Retrying.......")
            print()
    



if (t == 1):
    s = input("Subject: ")
    with open(f", "r") as file:
        content = file.read()
        print(content)
        
elif (t == 2):
    s = input("Subject: ")