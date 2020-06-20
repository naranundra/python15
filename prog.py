from tkinter import *
import tkinter.messagebox as msgbox
import tkinter

window = Tk()
window.title('Бүртгэлийн программ')
window.geometry('350x250')
window.resizable(0,0)

# reg_no, owog, ner, utas
reg_no = StringVar()
owog = StringVar()
ner = StringVar()
utas = StringVar()

Label(window,text='Регистр:').grid(row=0, column=0)
Entry(window, textvariable=reg_no).grid(row=0, column=1)

Label(window,text='Овог:').grid(row=1, column=0)
Entry(window, textvariable=owog).grid(row=1, column=1)

Label(window,text='Нэр:').grid(row=2, column=0)
Entry(window, textvariable=ner).grid(row=2, column=1)

Label(window,text='Утас:').grid(row=3, column=0)
Entry(window, textvariable=utas).grid(row=3, column=1)

def user_save():
    if reg_no.get() == '' or owog.get() == '' or ner.get == '' or utas.get == '':
        msgbox.showwarning('Анхаар, Mэдээллийг бүрэн оруулна уу')
    else:
        list_data.insert(END, reg_no.get()+ ','+ owog.get()+ ',' +ner.get() + ','+ utas.get())
        clear_entries()
      
def user_update():
    print('update...')

def user_delete():
    list_data.delete(list_data.curselection()[0])
    clear_entries()
    print('deleted...')
    
def clear_entries():
    reg_no.set('')
    owog.set('')
    ner.set('') 
    utas.set('')

Button(window, text='Хадгалах', command=user_save).grid(row=0, column=3)
Button(window, text='Засварлах', command=user_update).grid(row=1, column=3)
Button(window, text='Устгах', command = user_delete).grid(row = 2, column = 3)
Button(window, text='Арилгах', command = clear_entries).grid(row = 3, column = 3)

def user_select(event):
    selected_user = list_data.get(list_data.curselection()[0])
    data = selected_user.split(',')
    reg_no.set(data[0])
    owog.set(data[1])
    ner.set(data[2])
    utas.set(data[3])

list_data = Listbox(window, width=50, height=10)
list_data.grid(row=4, rowspan=1, column=0, columnspan=4 )
list_data.bind('<<ListboxSelect>>', user_select)

scroll = Scrollbar(window)
scroll.grid(row=4, column=4)
list_data.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_data.yview)

window.mainloop()