from tkinter import *
window = Tk()
window.title("Tkiner first window")
window.minsize(width=500, height=300)
i = 0
# Label 
my_label = Label(text="I am a label", font=("Arial", 12, "normal"))
my_label.pack()
# def clicked():
#     # my_label["text"] = f"Button Clicked"
#     my_label.config(text="Button Clicked")
#     my_label.pack()

# Entry
my_input = Entry(width=10)
my_input.pack()

def clicked():
    my_label.config(text=my_input.get())
    my_label.pack()

# Button
my_btn = Button(text="Click me", command=clicked)
my_btn.pack()


window.mainloop()