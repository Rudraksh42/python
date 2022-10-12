from tkinter import*

root = Tk()
root.title("Fibonacci")
root.geometry("500x500")

input_box = Entry(root , bg = "light blue")
label_Series = Label(root , bg ="cyan")
answer_label = Label(root , bg="dark green")

input_box.place(relx=0.5 , rely = 0.3 ,anchor = CENTER)
label_Series.place(relx = 0.5, rely = 0.4 , anchor = CENTER)
answer_label.place(relx=0.5 , rely = 0.5 , anchor = CENTER)

def Fibbonacci():
    for character in input_box.get() :
        label_Series["text"]= " "
        input2 = int(input_box.get())
        first_no = 0
        secound_no = 1
        sum = 0
        counter = 1
        main_sum = 0
        while counter <= input2 :
            label_Series["text"] += str(sum) + " "
            first_no = secound_no
            secound_no = sum
            sum = first_no + secound_no
            counter = counter+1
            main_sum = main_sum + sum
            answer_label['text'] = "Fibbonacci Sum :" +str(main_sum)
        first_no = 0 
        secound_no = 1
        sum = 0
        counter = 1
        main_sum = 0

btn = Button(root , text = "show Fibbonacci Sum" , bg = "blue" , fg = "snow" , command = Fibbonacci)
btn.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)
input_box.pack    
label_Series.pack
answer_label.pack
btn.pack    

            
root.mainloop() 