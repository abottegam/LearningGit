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
    messagebox.showinfo("Answer", "Yes :)")
    #comments
    print("Bryon Gyattlin III 323232323232")


    print("HOLYYYYYY GYATTT WHAT THE SIGMA!!!")
    print("Yes :)")