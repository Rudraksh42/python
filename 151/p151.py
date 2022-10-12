from tkinter import *
root =Tk()
root.title("Profit And Loss")
root.geometry("700x700")
root.configure(bg = "light blue")

month = ("January" , "Feburary", "March" , "April" , "May" , "June" ,"July" , "August" , "september","October" , "November" , "December")
profit = (140000,30009,13324,89686,34668,97673,43782,16786,323452,85767,24245,65672)

month_l = Label(root)
profit_l = Label(root)
max_l = Label(root)
min_l = Label(root)

month_l["text"] = "Months: " +str(month)
profit_l["text"] = "Profit: " +str(profit)

def month_pro():
    max_profit = max(profit)
    max_pr_index = profit.index(max_profit)
    print(max_pr_index)
    
    max_pr_month = month[max_pr_index]
    max_l["text"] = "Maximum profit of " + str(max_profit) + " was recorded in month of" + str(max_pr_month)

btn1 = Button(root , text= "Press me to know about maximum profit" , command=month_pro)

def month_ls():
    min_profit = min(profit)
    min_pr_index = profit.index(min_profit)
    print(min_pr_index)
    
    min_pr_month = month[min_pr_index]
    min_l["text"] = "Minimum profit of " + str(min_profit) + " was recorded in month of" + str(min_pr_month)
    
btn2 = Button(root , text= "Press me to know about minimum profit" , command=month_ls)

#place
month_l.place(relx = 0.5, rely = 0.3 , anchor= CENTER)
profit_l.place(relx = 0.5, rely = 0.4 , anchor= CENTER)
btn1.place(relx = 0.5, rely = 0.5 , anchor= CENTER)
max_l.place(relx = 0.5, rely = 0.6 , anchor= CENTER)
btn2.place(relx = 0.5, rely = 0.7 , anchor= CENTER)
min_l.place(relx = 0.5, rely = 0.8 , anchor= CENTER)
root.mainloop()