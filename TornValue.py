from tkinter import *

root = Tk()
root.title("TornValue by DeadShot556[2637964]")
root.geometry("500x300")
icon = PhotoImage(file='tvico.png')
root.iconphoto(False, icon)


def return_entry():
    """Gets and prints the content of the entry"""
    entry = int(raw.get())
    new_value.config(text=entry)


def clear_entry():
    """removes all values"""
    raw.delete(0, END)
    new_value.config(text="")
    new_discount.config(text="")
    new_profit.config(text="")


def Eighty():
    entry = int(raw.get())
    eighty = entry * 0.8
    new_discount.config(text=int(eighty))
    profit = entry - eighty
    new_profit.config(text=int(profit))


def Ninety():
    entry = int(raw.get())
    ninety = entry * 0.9
    new_discount.config(text=int(ninety))
    profit = entry - ninety
    new_profit.config(text=int(profit))


def Ninety2():
    entry = int(raw.get())
    ninety_two = entry * 0.92
    new_discount.config(text=int(ninety_two))
    profit = entry - ninety_two
    new_profit.config(text=int(profit))


def Ninety5():
    entry = int(raw.get())
    ninety_five = entry * 0.95
    new_discount.config(text=int(ninety_five))
    profit = entry - ninety_five
    new_profit.config(text=int(profit))


def Ninety8():
    entry = int(raw.get())
    ninety_eight = entry * 0.98
    new_discount.config(text=int(ninety_eight))
    profit = entry - ninety_eight
    new_profit.config(text=int(profit))


canvas = Canvas(root, bg="#75a3a3")
canvas.place(relwidth=1, relheight=1)

raw = Entry(canvas, bd=2, bg="#b3cccc", fg="black", justify="center")
raw.place(y=15, x=150, width=200)
content = raw.get()

info = Label(canvas, text="Designed to be used with TornTools live trade values.", bg="#75a3a3")
info.place(width=300, y=277, x=100)

raw_label = Label(canvas, text="^^^ Insert the Raw Trade Value ^^^", fg="black", bg="#75a3a3")
raw_label.place(y=35, x=150, width=200)

raw_label2 = Label(canvas, text="Without ( $ ) or( , ) symbols", fg="black", bg="#75a3a3")
raw_label2.place(y=50, x=150, width=200)

raw_value = Label(canvas, text="Total Market Value:", fg="black", bg="#75a3a3")
raw_value.place(y=95, x=15)

raw_discount = Label(canvas, text="Discounted Value:", fg="black", bg="#75a3a3")
raw_discount.place(y=125, x=15)

raw_profit = Label(canvas, text="Total Profit:", fg="black", bg="#75a3a3")
raw_profit.place(y=155, x=15)

new_value = Label(canvas, text="", bg="#b3cccc", relief="raised")
new_value.place(y=95, x=150, width=200)

new_discount = Label(canvas, text="", bg="#b3cccc", relief="raised")
new_discount.place(y=125, x=150, width=200)

new_profit = Label(canvas, text="", bg="#b3cccc", relief="raised")
new_profit.place(y=155, x=150, width=200)

perc = Label(canvas, font=("arial", 10, "bold"), text="What percentage of the sale will you profit?", bg="#75a3a3")
perc.place(y=210, x=100, width=300)

submit = Button(canvas, text="Submit", justify="center", command=return_entry)
submit.place(width=60, y=13, x=360)

clear = Button(canvas, text="Clear", justify="center", command=clear_entry)
clear.place(width=60, y=13, x=430)

perc_2 = Button(canvas, text="2%", justify="center", command=Ninety8)
perc_2.place(width=75, y=250, x=20)

perc_5 = Button(canvas, text="5%", justify="center", command=Ninety5)
perc_5.place(width=75, y=250, x=115)

perc_9 = Button(canvas, text="8%", justify="center", command=Ninety2)
perc_9.place(width=75, y=250, x=212.5)

perc_10 = Button(canvas, text="10%", justify="center", command=Ninety)
perc_10.place(width=75, y=250, x=310)

perc_20 = Button(canvas, text="20%", justify="center", command=Eighty)
perc_20.place(width=75, y=250, x=405)


root.mainloop()