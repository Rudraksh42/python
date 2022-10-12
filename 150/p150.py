

from tkinter import *
import random 

root = Tk()
root.title("Lucky Friend")
root.geometry("500x500")
root.configure(bg = "light blue")


list_co = []
list_ci = []


enput_co = Entry(root)
enput_ci = Entry(root)

l1 = Label(root , text = "Enter Country And City " )
list_country = Label(root)
list_city = Label(root)
list_random_co = Label(root)
list_random_ci = Label(root)


def country_capital():
    country = enput_co.get()
    list_co.append(country)
    list_country["text"] = "Country Are :" + str(list_co)
    
    capital = enput_ci.get()
    list_ci.append(capital)
    list_city["text"] = "City Are :" + str(list_ci)

def random_ci_co():
    lenght = len(list_co)
    ran_country = random.randint(0 , lenght-1)

    country_name = list_co[ran_country]
    list_random_co["text"] = "Random Country: " + country_name
    
    lenght2 = len(list_ci)
    ran_city = random.randint(0 , lenght2-1)

    city_name = list_ci[ran_city]
    list_random_ci["text"] = "Random City: " + city_name

    
    
    
btn1 = Button(root , text = "Add Country & City" , command=country_capital)
btn2 = Button(root , text = "Random Country & City" , command=random_ci_co)

l1.place(relx = 0.5 , rely = 0.2 , anchor = CENTER)

enput_co.place(relx = 0.5 , rely = 0.3 , anchor = CENTER)

enput_ci.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)

btn1.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

list_country.place(relx = 0.3 , rely = 0.6 , anchor = CENTER)

list_city.place(relx = 0.7 , rely = 0.6 , anchor = CENTER)

btn2.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)

list_random_co.place(relx = 0.5 , rely = 0.8 , anchor = CENTER)

list_random_ci.place(relx = 0.5 , rely = 0.9 , anchor = CENTER)

root.mainloop()