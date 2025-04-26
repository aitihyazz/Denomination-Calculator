from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x500")
root.configure(bg="light blue")
root.title("Domination Counter")

up = Image.open("image.png")
up = up.resize((300, 300))
image = ImageTk.PhotoImage(up)
label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

label1 = Label(root, text="Domination Calculator", bg="light blue", font=("Arial", 14))
label1.place(relx=0.5, y=340, anchor=CENTER)

def topwin():
    top = Toplevel()
    top.geometry("600x350+50+50")
    top.configure(bg="light grey")
    top.title("Calculator")

    label = Label(top, text="Enter the amount", bg="light grey", font=("Arial", 12))
    label.place(x=230, y=50)

    enter = Entry(top)
    enter.place(x=200, y=80)

    l1 = Label(top, text="2000", bg="light grey")
    l1.place(x=180, y=200)
    l2 = Label(top, text="500", bg="light grey")
    l2.place(x=180, y=230)
    l3 = Label(top, text="100", bg="light grey")
    l3.place(x=180, y=260)

    t1 = Entry(top)
    t1.place(x=270, y=200)
    t2 = Entry(top)
    t2.place(x=270, y=230)
    t3 = Entry(top)
    t3.place(x=270, y=260)

    def calculator():
        try:
            amount = int(enter.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")
    btn.place(x=240, y=120)

def msg():
    messagebox.showinfo("Alert!", "Get ready to continue!")
    topwin()

b1 = Button(root, bg="brown", fg="white", command=msg, text="Let's Get Started")
b1.place(x=260, y=360)

root.mainloop()
