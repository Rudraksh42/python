from tkinter import *
root  = Tk()
root.title("AsCII Coverter")
root.geometry("700x700")
root.configure(background = "light cyan")


input1 = Entry(root)
input1.place(relx=0.5 , rely = 0.4 , anchor = CENTER)
label = Label(root, text = "Name IN AsCII  " , bg= "snow" , fg = "black")
def anciiConvert():
    input_word = input1.get()
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        
btn= Button(root , text = "Convert TO AsCII" , bg = "Cyan" , fg = "black" , command=anciiConvert)
btn.place(relx = 0.5 ,rely = 0.5 , anchor = CENTER)
label.place(relx = 0.5 , rely = 0.6 , anchor = CENTER) 
        

root.mainloop()