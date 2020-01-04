from tkinter import *
from backend import Database

database = Database()


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(0, selected_tuple[1])
        e3.delete(0, END)
        e3.insert(0, selected_tuple[2])
        e2.delete(0, END)
        e2.insert(0, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(0, selected_tuple[4])
    except IndexError:
        pass


def search_command():
    list1.delete(0, END)
    for rows in database.search(title_var.get(), author_var.get(), year_var.get(), isbn_var.get()):
        list1.insert(END, rows)


def view_command():
    list1.delete(0, END)
    for rows in database.view():
        list1.insert(END, rows)


def add_command():
    list1.delete(0, END)
    database.insert(title_var.get(), author_var.get(), year_var.get(), isbn_var.get())
    list1.delete(0,END)
    list1.insert(END, (title_var.get(), author_var.get(), year_var.get(), isbn_var.get()))


def update_command():
    database.update(selected_tuple[0], title_var.get(), author_var.get(), year_var.get(), isbn_var.get())


def delete_command():
    database.delete(selected_tuple[0])


def close_command():
    windows.destroy()


windows = Tk()
windows.title("Books")

# creating a label and entry for title,author,year,isbn
l1 = Label(windows, text="Title")
l1.grid(row=0, column=0)
title_var = StringVar()
e1 = Entry(windows, textvariable=title_var)
e1.grid(row=0, column=1)

l2 = Label(windows, text="Year")
l2.grid(row=1, column=0)
year_var = StringVar()
e2 = Entry(windows, textvariable=year_var)
e2.grid(row=1, column=1)

l3 = Label(windows, text="Author")
l3.grid(row=0, column=2)
author_var = StringVar()
e3 = Entry(windows, textvariable=author_var)
e3.grid(row=0, column=3)

l4 = Label(windows, text="isbn")
l4.grid(row=1, column=2)
isbn_var = StringVar()
e4 = Entry(windows, textvariable=isbn_var)
e4.grid(row=1, column=3)

# create a listbox  and scroll bar
list1 = Listbox(windows, width=40, height=10)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(windows)
scroll.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)


list1.bind("<<ListboxSelect>>", get_selected_row)

# create a button for Function
b1 = Button(windows, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b1 = Button(windows, text="Add Enrty", width=12, command=add_command)
b1.grid(row=3, column=3)

b1 = Button(windows, text="Update Entry", width=12, command=update_command)
b1.grid(row=4, column=3)

b1 = Button(windows, text="Search Entry", width=12, command=search_command)
b1.grid(row=5, column=3)

b1 = Button(windows, text="Delete Entry", width=12, command=delete_command)
b1.grid(row=6, column=3)

b1 = Button(windows, text="Close", width=12, command=close_command)
b1.grid(row=7, column=3)

windows.mainloop()
