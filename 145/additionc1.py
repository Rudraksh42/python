from tkinter import *
root = Tk()

root.title("addition ")
root.geometry("300x400")
labelANS = Label(root)
  
def add():
    result = 69+1
    labelANS["text"]=result
    
labelANS.pack()
btn = Button(root,text="add",command=add)
btn.pack()
    
    

root.mainloop()