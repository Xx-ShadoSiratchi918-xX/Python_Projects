from tkinter import *

root = Tk()
root.title("Calculator")


def show_preview():
    show = display.get()
    label.config(text=show)


def clean_display():
    display.delete(0, END)


def remove_number():
    current_display = display.get()
    if len(current_display) > 0:
        new_display = current_display[:-1]
        display.delete(0, END)
        display.insert(0, new_display)
    else:
        clean_display()
        display.insert(0, '#ERROR')


def calculate():
    result = display.get()
    length = len(result)
    if length != 0:
        try:
            calc = str(eval(result))
            display.delete(0, END)
            display.insert(0, calc)
            show_preview()

        except:
            calc = "#ERROR"
            display.delete(0, END)
            display.insert(0, calc)
            show_preview()
    else:
        pass

label = Label(root, text='', font='THIN 13')
label.grid(row=1, column=2, sticky=W)
Label(root, text='=', font='THIN 10').grid(row=1, column=3, sticky=NSEW, columnspan=2)
Label(root, text='', font='THIN 10').grid(row=1, column=4, sticky=E)

display = Entry(root, font='THIN 20', borderwidth=5)
display.grid(row=2, columnspan=7, sticky=W + E)

# Botones Numericos

Button(root, text='1', borderwidth=5, command=lambda: display.insert(END, '1')).grid(row=3, column=1, pady=5, padx=5, sticky=W + E)
Button(root, text=' 2 ', borderwidth=5, command=lambda: display.insert(END, '2')).grid(row=3, column=2, pady=5, padx=5, sticky=W + E)
Button(root, text=' 3 ', borderwidth=5, command=lambda: display.insert(END, '3')).grid(row=3, column=3, pady=5, padx=5, sticky=W + E)

Button(root, text='4', borderwidth=5, command=lambda: display.insert(END, '4')).grid(row=4, column=1, pady=5, padx=5, sticky=W + E)
Button(root, text=' 5 ', borderwidth=5, command=lambda: display.insert(END, '5')).grid(row=4, column=2, pady=5, padx=5, sticky=W + E)
Button(root, text=' 6 ', borderwidth=5, command=lambda: display.insert(END, '6')).grid(row=4, column=3, pady=5, padx=5, sticky=W + E)

Button(root, text='7', borderwidth=5, command=lambda: display.insert(END, '7')).grid(row=5, column=1, pady=5, padx=5, sticky=W + E)
Button(root, text=' 8 ', borderwidth=5, command=lambda: display.insert(END, '8')).grid(row=5, column=2, pady=5, padx=5, sticky=W + E)
Button(root, text=' 9 ', borderwidth=5, command=lambda: display.insert(END, '9')).grid(row=5, column=3, pady=5, padx=5, sticky=W + E)

# Botones de operadores

Button(root, text='AC', borderwidth=5, command=lambda: clean_display()).grid(row=6, column=1, pady=5, padx=5, sticky=W + E)
Button(root, text=' 0 ', borderwidth=5, command=lambda: display.insert(END, '0')).grid(row=6, column=2, pady=5, padx=5, sticky=W + E)
Button(root, text=' % ', borderwidth=5, command=lambda: display.insert(END, '%')).grid(row=6, column=3, pady=5, padx=5, sticky=W + E)

Button(root, text=' + ', borderwidth=5, command=lambda: display.insert(END, '+')).grid(row=3, column=4, pady=5, padx=5, sticky=W + E)
Button(root, text=' - ', borderwidth=5, command=lambda: display.insert(END, '-')).grid(row=4, column=4, pady=5, padx=5, sticky=W + E)
Button(root, text=' * ', borderwidth=5, command=lambda: display.insert(END, '*')).grid(row=5, column=4, pady=5, padx=5, sticky=W + E)
Button(root, text=' / ', borderwidth=5, command=lambda: display.insert(END, '/')).grid(row=6, column=4, pady=5, padx=5, sticky=W + E)

Button(root, text='↩', borderwidth=5, command=lambda: remove_number()).grid(row=3, column=5, pady=5, padx=5, sticky=W + E, columnspan=2)
Button(root, text='Exp', borderwidth=5, command=lambda: display.insert(END, '**')).grid(row=4, column=5, pady=5, padx=5, sticky=W + E)
Button(root, text='^2', borderwidth=5, command=lambda: display.insert(END, '**2')).grid(row=4, column=6, pady=5, padx=5, sticky=W + E)
Button(root, text=' ( ', borderwidth=5, command=lambda: display.insert(END, '(')).grid(row=5, column=5, pady=5, padx=5, sticky=W + E)
Button(root, text=' ) ', borderwidth=5, command=lambda: display.insert(END, ')')).grid(row=5, column=6, pady=5, padx=5, sticky=W + E)
Button(root, text='=', borderwidth=5, command=lambda: calculate()).grid(row=6, column=5, pady=5, padx=5, sticky=W + E, columnspan=2)

root.mainloop()
