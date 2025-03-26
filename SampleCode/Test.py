from tkinter import messagebox
inp = input("Input: ").lower()
fnd = input("Word to find: ")

start = -1
for letter in fnd:
    start = inp.find(letter, start+1)
    if start == -1:
        print("No!!")
        break
else:
    print(f"{fnd} could not be found")
    print("Sorry!")