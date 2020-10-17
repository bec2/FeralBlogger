import tkinter as tk
import output

def printSomething():
    y = output.function()
    label = tk.Label(root, text= str(y))
    label.pack()

root = tk.Tk()
root.geometry('500x200')
root.configure(bg='pink')
root.title('FeralBlogger')

button = tk.Button(root, text="Make my next viral text post", command=printSomething)
button.pack()
button.configure(bg='white')

y():
    sys.stdout = StdRedirector(text_box)


root.mainloop()


