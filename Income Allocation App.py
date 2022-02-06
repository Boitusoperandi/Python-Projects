import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


root_var = tk.Tk()
#ADDS TITLE 
root_var.title("Income Allocator")

#-----------------Textvariables for entries----------------------
amount1 = StringVar()
amount2 = StringVar()
amount3 = StringVar()
amount4 = StringVar()

#-----------------------------ENTRIES---------------------------------------------
#Salary Entry Placing 
a = Entry(root_var,textvariable= amount1, width = 35, borderwidth=5)
a.grid(row=0, column=1, columnspan= 3, padx=10, pady=10)

#Saving Entry and Placing
b = Entry(root_var,textvariable=amount2, width = 35, borderwidth=5)
b.grid(row=1, column=1, columnspan= 3, padx=10, pady=10)


#Spending Entry and Placing
c = Entry(root_var,textvariable=amount3, width = 35, borderwidth=5)
c.grid(row=2, column=1, columnspan= 3, padx=10, pady=10)


#Investments Entry and Placing
d = Entry(root_var,textvariable=amount4, width = 35, borderwidth=5)
d.grid(row=3, column=1, columnspan= 3, padx=10, pady=10)

#-------------------------------LABELS Before Entries-----------------------------------------
#Labels and placing
IncomeLabel = Label(root_var,text = "Enter your INCOME Amount:" + "                        $")
IncomeLabel.grid(row=0,column=0)

SavingsLabel = Label(root_var,text = "Enter Percentage allocated to SAVINGS:         ")
SavingsLabel.grid(row=1,column=0)

SpendingLabel = Label(root_var, text = "Enter Percentage allocated to SPENDING:      ")
SpendingLabel.grid(row=2,column=0)

InvestmentsLabel = Label(root_var, text = "Enter Percentage allocated to INVESTMENTS:")
InvestmentsLabel.grid(row=3,column=0)

Percetagelabelone= Label(root_var,text = "%")
Percetagelabelone.grid(row=1,column=3)

Percetagelabel2= Label(root_var,text = "%")
Percetagelabel2.grid(row=2,column=3)

Percetagelabel3= Label(root_var,text = "%")
Percetagelabel3.grid(row=3,column=3)

#------------------------------Functions----------------------------------------

def press():
    
    #to get the float of the numbers in Entry boxes
    a1 = float(a.get())
    b1 = float(b.get())
    c1 = float(c.get())
    d1 = float(d.get())

    #Savings Calculation
    calc1 = round((a1 * b1)*.01,2)
    
    #Spendings Calculation
    calc2 = round((a1 * c1)*.01,2)
    
    #Investments Calculation
    calc3 = round((a1 * d1)*.01,2)
  
    amount5.set("Money allocated to SAVINGS: ${}".format(calc1))
    amount6.set("Money allocated to SPENDING: ${}".format(calc2))
    amount7.set("Money allocated to INVESTMENTS: ${}".format(calc3))
        
def reset():
    #deletes all numbers that were calculated or entered
    amount1.set("")
    amount2.set("")
    amount3.set("")
    amount4.set("")
    amount5.set("")
    amount6.set("")
    amount7.set("")
   
    
         

def Exit():
    #leaving the application
    root_var.destroy()

#----------------------Labels to be Created when Calcation executed--------------------
#TEXTVARIABLES for calc 
amount5 = tk.StringVar()
amount6 = tk.StringVar()
amount7 = tk.StringVar()

#LABELS FOR CALCS
L_amount1 = ttk.Label(root_var, textvariable = amount5)
L_amount2 = ttk.Label(root_var, textvariable = amount6)
L_amount3 = ttk.Label(root_var, textvariable = amount7)

#placing for labels
L_amount1.grid(row=6, column=0, columnspan = 8)
L_amount2.grid(row=7, column=0, columnspan = 8)
L_amount3.grid(row=8, column=0, columnspan = 8)


#-----------------------------------Buttons--------------------------------------------
#DEFINE BUTTONS
calculatebtn = Button(root_var,text= "CALCULATE",padx=82,pady=13,command=press) 
resetbtn = Button(root_var, text="Reset",padx=60,pady=13, command=reset)
exitbtn = Button(root_var, text="Exit",padx=75,pady=13, command=Exit)


#PLACE BUTTONS ON SCREEN
calculatebtn.grid(row=4, column=0)

resetbtn.grid(row=4,column=1)

exitbtn.grid(row=4 , column=2)


root_var.mainloop()
