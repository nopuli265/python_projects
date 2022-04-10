"""
A program that stores this book information:
Title, Author
Year, ISBN 

User can:
View all records 
Search an entry
Add entry 
Update entry
Delete
Close
"""
from tkinter import *
import backend 

def view_command():
    listBook.delete(0,END)
    for row in backend.view():
        listBook.insert(END,row)

def search_command():
    listBook.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        listBook.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    listBook.delete(0,END)
    listBook.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
   
def get_selected_row(event):
    try:
        global selected_tuple
        index=listBook.curselection()[0]
        selected_tuple=listBook.get(index)
        eTitle.delete(0,END)
        eTitle.insert(END,selected_tuple[1])
        eAuthor.delete(0,END)
        eAuthor.insert(END,selected_tuple[2])
        eYear.delete(0,END)
        eYear.insert(END,selected_tuple[3])
        eISBN.delete(0,END) 
        eISBN.insert(END,selected_tuple[4])
    except IndexError:
        pass
def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

# def close_command():
    
window=Tk()
window.wm_title("Books Store")
labtitle=Label(window, text='Title')
labtitle.grid(row=0,column=0)
title_text=StringVar()
eTitle=Entry(window, textvariable=title_text)
eTitle.grid(row=0,column=1)

labAuthor=Label(window, text='Author')
labAuthor.grid(row=0,column=2)
author_text=StringVar()
eAuthor=Entry(window,textvariable=author_text)
eAuthor.grid(row=0,column=3)

labYear=Label(window, text='Year')
labYear.grid(row=1,column=0)
year_text=StringVar()
eYear=Entry(window,textvariable=year_text)
eYear.grid(row=1,column=1)

labISBN=Label(window, text='ISBN')
labISBN.grid(row=1,column=2)
isbn_text=StringVar()
eISBN=Entry(window,textvariable=isbn_text)
eISBN.grid(row=1,column=3)

listBook=Listbox(window, height=6, width=35)
listBook.grid(row=2,column=0,rowspan=6, columnspan=2)
listBook.bind('<<ListboxSelect>>',get_selected_row)

sb=Scrollbar(window)
sb.grid(row=2,column=2, rowspan=6)

listBook.configure(yscrollcommand=sb.set)
sb.configure(command=listBook.yview)

bView=Button(window, text='View All', width=12, command=view_command)
bView.grid(row=2,column=3)

bSearch=Button(window, text='Search entry', width=12, command=search_command)
bSearch.grid(row=3,column=3)

bAdd=Button(window, text='Add entry', width=12, command=add_command)
bAdd.grid(row=4,column=3)

bUpdate=Button(window, text='Update', width=12, command=update_command)
bUpdate.grid(row=5,column=3)

bDelete=Button(window, text='Delete', width=12,command=delete_command)
bDelete.grid(row=6,column=3)

bClose=Button(window, text='Close', width=12,command=window.destroy)
bClose.grid(row=7,column=3)

window.mainloop()
