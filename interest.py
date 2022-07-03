from tkinter import *
window=Tk()

window.title('SI Calculator')
window.geometry("500x400")
window.configure(bg='black')
   
def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    
    result.destroy()
    message=Label(result_f,text="Interest on Rs"+str(p)+"at rate of interest "+str(r)+"% for "+str(t)+" years is Rs."+str(interest), bg = "grey", font=("Calibri", 10), width=45)
    message.place(x=19,y=38)
    message.pack()

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "blue", font=("Calibri", 20),bd=5)
app_label.place(x=18, y=20)

principle_label=Label(window, text="Principle in Rs", fg = "black", bg = "yellow", font=("Calibri", 12),bd=1)
principle_label.place(x=18, y=92)

principle=Entry(window, text="", bd=2, width=22)
principle.place(x=200, y=92)

rate_label=Label(window, text="Rate of Interest in %", fg = "black", bg = "red", font=("Calibri", 12))
rate_label.place(x=20, y=140)

rate=Entry(window, text="", bd=2, width=15)
rate.place(x=200, y=142)

time_label=Label(window, text="Time in Yrs", fg = "black", bg = "green", font=("Calibri", 12))
time_label.place(x=18, y=185)

time=Entry(window, text="", bd=2, width=15)
time.place(x=200, y=187)

calculate_b=Button(window,text="CALCULATE",fg = "black", bg = "grey",bd=4,command=calculate_interest)
calculate_b.place(x=18,y=250)

result_f = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_f.pack(padx=20, pady=20)
result_f.place(x=18,y=300)

result=Label(result_f,text="Your result will be displayed here", bg = "brown", font=("Calibri", 15), width=55)
result.place(x=18,y=20)
result.pack()

window.mainloop()