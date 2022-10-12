from tkinter import *
import random 

root = Tk()
root.geometry("500x500")
root.configure(bg = "snow")

item = ["mobile" , "food" , "camera" , "water bottle", "medicine"]
lb = Label(root)
lb["text"] = "Listed Item Are" + str(item)
label_item = Label(root)

def random_list():
    random_name = random.sample(range(0,4),1)
    label_item["text"] = "pick the " + str(random_name)
  
    
btn = Button(root , text = "press" , command=random_list)
btn.place(relx = 0.5 , rely =0.6 , anchor=CENTER)
lb.place(relx = 0.5 , rely =0.5, anchor=CENTER)
label_item.place(relx = 0.5 , rely =0.7 , anchor=CENTER)
    
root.mainloop()