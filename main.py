import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Labels
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "italic"))
my_label.pack(side="left")
# ^ this is required for label to show up


# Required to keep the window open until manually closed by the user.
window.mainloop()
