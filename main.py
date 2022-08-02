from tkinter import *

def main():
    global root
    root = Tk()

    root.geometry('300x300')
    root.title("My App")
    root.configure(bg='#fff')
    
    Label(root, text="Hello World").pack()
    Button(root, text="Exit ❌", command=root.destroy).pack()
    root.mainloop()

# Run App
main()