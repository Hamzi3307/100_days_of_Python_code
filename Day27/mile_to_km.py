from tkinter import *

window = Tk()
window.title("Mile to Km")
window.minsize(width=200, height=100)

# Mile Label
mile = Label(text="Miles")
mile.grid(column=3, row=1)

# is equal to
eql = Label(text="is equal to")
eql.grid(column=1, row=2)

# km label
km = Label(text="km")
km.grid(column=3, row=2)

# Entry
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="enter")
# Gets text in entry
# print(entry.get())
entry.grid(column=2, row=1)

# kilemeters
cal = Label(text="1 mile = 1.6 km")
cal.grid(column=2, row=2)
def clicked():
    if entry.get().title() == "Exit":
        # code to stop the loop 
        pass 
    try:
        m = int(entry.get())
    except:
        cal.config(text="Try to enter digits plzz")
    km = m * 1.6
    cal.config(text=km)    

# button (calculate)
my_btn = Button(text="calculate", command=clicked)
my_btn.grid(column=2, row=3)

window.mainloop()