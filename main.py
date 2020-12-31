import tkinter

root = tkinter.Tk()
root.title("Simple Adder")
tkinter.Label(root, text="First No.").grid(row=0)
tkinter.Label(root, text="Second No.").grid(row=1)
a = tkinter.Entry(root)
b = tkinter.Entry(root)
a.grid(row=0, column=1) 
b.grid(row=1, column=1) 
def add():
    try:
        sum = int(a.get())+int(b.get())
        return tkinter.Label(root, text=f'The sum of no. are {sum}').grid(row=3)
    except:
        a.delete(0, 'end')
        b.delete(0, 'end')
        return tkinter.Label(root, text="Must be a no.").grid(row=3)
addButton = tkinter.Button(root, text="Add", command=add).grid(row=2)
root.mainloop()