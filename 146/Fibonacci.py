from tkinter import*

root = Tk()
root.title("Fibonacci")
root.geometry("500x500")

label_series = Label(root , text="Fibonacci Series:- ")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    first_no = 0
    second_no = 1
    sum = 0
    num = 10
    counter = 1
    while(counter <= num):
        label_series["text"] += str(sum)+" "
        counter += 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    
    label_flower["text"] = "Flower is fully bloomed"
    label_spiral["text"] = "Spiral in left direction are " + str(second_no) + "\n and Spiral in right direction are " + str(first_no) + "\n Total number of spiral are " + str(sum)
        
   
btn = Button(root , text="Show Fibonacci Series " , command=fibonacci)     
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop() 