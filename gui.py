
import tkinter as tk
import output

def printSomething():
    y = output.function()
    label = tk.Label(root, text= "5 potential hits await you in the terminal...")
    label.pack()

root = tk.Tk()
root.geometry('500x200')
root.configure(bg='pink')
root.title('FeralBlogger')

button = tk.Button(root, text="Make my next viral text post", command=printSomething)
button.pack()
button.configure(bg='white')

root.mainloop()
