from tkinter import *
root = Tk()
root.title("Random Alphabet")
root.geometry("500x500")
root.configure(bg="#3483eb")

import random

alpha1 = ["a" ,"b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z"]
print(alpha1)
alpha2 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(alpha2)

word1L = Label(root)
word1U = Label(root)

def generate_random():
    
    #lowercase
    
    ranL1 = random.randint(0,25) 
    print(ranL1)
    diL1 = alpha1[ranL1]
    
    
    ranL2 = random.randint(0,25) 
    print(ranL2)
    diL2 = alpha1[ranL2]
    
    
    ranL3 = random.randint(0,25) 
    print(ranL3)
    diL3 = alpha1[ranL3]
    
    
    ranL4 = random.randint(0,25) 
    print(ranL4)
    diL4 = alpha1[ranL4]
    
    
    ranL5 = random.randint(0,25) 
    print(ranL5)
    diL5 =alpha1[ranL5]
    
    word1L["text"] = "Random Alphabet in Lowercase Are: "  + diL1 + diL2 + diL3 + diL4 + diL5
    
    #uppercase
    
    ranU1 = random.randint(0,25) 
    print(ranU1)
    diU1 = alpha2[ranU1]
    
    
    ranU2 = random.randint(0,25) 
    print(ranU2)
    diU2 = alpha2[ranU2]
    
    
    ranU3 = random.randint(0,25) 
    print(ranU3)
    diU3 = alpha2[ranU3]
    
    
    ranU4 = random.randint(0,25) 
    print(ranU4)
    diU4 = alpha2[ranU4]
    
    
    ranU5 = random.randint(0,25) 
    print(ranU5)
    diU5 =alpha2[ranU5]
    
    word1U["text"] = "Random Alphabet in Uppercase  Are: "  + diU1 + diU2 + diU3 + diU4 + diU5


btn = Button(root , text = "Show The Random Alphabet" ,bg="aquamarine1", fg ="black" , command=generate_random)
btn.place(relx = 0.5 , rely= 0.3, anchor= CENTER)
word1L.place(relx = 0.5 , rely= 0.4, anchor= CENTER)
word1U.place(relx = 0.5 , rely= 0.5, anchor= CENTER)

root.mainloop()