from tkinter import *
root = Tk()
root.title("AScii & encryption")
root.geometry("500x500")
root.configure(background = "#f0a5a5")


word_value = Entry(root)
word_value.place(relx = 0.5, rely = 0.4, anchor = CENTER)
ascii_value = Label(root)
ascii_encrypted = Label(root)

def value_ascii():
    ascii_value["text"] =  " "
    value = word_value.get()
    for letter in value:
        ascii_value["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted_name = ascii + 2
        ascii_name = str(chr(encrypted_name))
        ascii_encrypted["text"] += ascii_name
        
        
btn = Button(root , text = "convert the value " , command=value_ascii)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
ascii_value.place(relx = 0.5, rely = 0.6, anchor = CENTER)        
ascii_encrypted.place(relx = 0.5, rely = 0.7, anchor = CENTER)    

root.mainloop()