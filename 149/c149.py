from tkinter import *
import random
root = Tk()
root.title("Lucky Friend")
root.geometry("400x400")

label_frnd = Label(root)

list1= ["Rohan" , "Aaradhay" , "Swayam" , "Abhinav" , "Vraj"]
print(list1)

def lucky():
    ran = random.randint(0,4) 
    print(ran)
    luckyperson =list1[ran]
    label_frnd["text"] = luckyperson
 
btn = Button(root ,text = "choose your lucky frnd", command=lucky)
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
label_frnd.place(relx = 0.5 , rely = 0.6, anchor = CENTER)
root.mainloop()