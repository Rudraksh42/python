from tkinter import *
import random 

root = Tk()
root.title("Random Number")
root.geometry("500x500")
root.configure(bg = "chartreuse3")

ran_list = Label(root)
ran_sort = Label(root)

def randomlist() :
    randomlist = random.sample(range(1,100),10)
    ran_list["text"] = "Random Numbers Are: " + str(randomlist)
    randomlist.sort()
    ran_sort["text"]= "Sorted Number Are: " + str(randomlist)
    
btn = Button(root , text = "Show The Random Number's" ,bg="aquamarine1", fg ="black" , command=randomlist)
ran_list.place(relx = 0.5 , rely= 0.6, anchor= CENTER)
ran_sort.place(relx = 0.5 , rely= 0.7, anchor= CENTER)
btn.place(relx = 0.5 , rely= 0.5, anchor= CENTER)

root.mainloop()