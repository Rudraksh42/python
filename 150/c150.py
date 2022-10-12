from tkinter import *
import random 

root = Tk()
root.title("Lucky Friend")
root.geometry("500x500")
root.configure(bg = "light blue")


list1 = []

enput_frnd = Entry(root)

friend_list = Label(root)
random_no = Label(root)
lucky_frnd = Label(root)

def add_frnd():
    frnd = enput_frnd.get()
    list1.append(frnd)
    friend_list["text"] = "Your Friend List:" + str(list1)
    
def random_frnd():
    lenght = len(list1)
    ran_frnd = random.randint(0 , lenght-1)
    random_no["text"] = str(ran_frnd)
    lucky_frnd_no = list1[ran_frnd]
    lucky_frnd["text"] = "Your Luckky Friend Is " + lucky_frnd_no
    print(lucky_frnd_no)
    
    
btn1 = Button(root , text = "Add Friend" , command=add_frnd)
btn2 = Button(root , text = "Who Is Your Lucky Friend?" , command=random_frnd)
enput_frnd.place(relx = 0.5 , rely = 0.3 , anchor = CENTER)
friend_list.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
random_no.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)
lucky_frnd.place(relx = 0.5 , rely = 0.8 , anchor = CENTER)
btn1.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)
btn2.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)

root.mainloop()