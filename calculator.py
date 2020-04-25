
from tkinter import *
import tkinter.font as tkFont

window = Tk()

window.geometry("295x445")
window.resizable(0,0)
window.title("Sahil's Calculator")
window.configure(padx=6,pady=10,bg="#ffffff", borderwidth=0, relief="flat")
window.iconbitmap("calculator.ico")
window.wm_attributes("-alpha",0.945)

fontStyle = tkFont.Font(family="comic sans ms", size=20, weight="bold")
fontnumber = tkFont.Font(family="comic sans ms", size=12, weight='normal')
fontnumber1 = tkFont.Font(family="comic sans ms", size=10, weight='bold')
fontnumber2 = tkFont.Font(family="comic sans ms", size=10, weight='normal')
fontnumber3 = tkFont.Font(family="comic sans ms", size=9, weight='normal')
fontnumber4 = tkFont.Font(family="comic sans ms", size=7, weight='bold')

title_bar = Label(window,text="Sahil's Calculator", fg ="#ffffff",bg="#ffffff", font=fontnumber1,justify="left")
#close_btn = Button(window,text="X" ,bg="#ff6666",font=fontnumber4,command=window.destroy,bd=0,padx=24,pady=2,fg="white")
title_bar.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
#close_btn.grid(row=0,column=3,padx=1,pady=1)


e = Entry(window,width=17,borderwidth=0,bg="#ffffff", font=fontStyle)
e.grid(row=2, column=0, columnspan=4,padx=0,pady=20)
e.config(justify="right")
e.size()

e1 = Entry(window, width=38, borderwidth=0, bg="#ffffff", font=fontnumber3 )
e1.grid(row=1, column=0, columnspan=4,padx=0,pady=5)
e1.config(justify="right")

def button_click(number):

    current = e.get()
    e.delete(0, END)
    if (number == "-"):
        e.insert(0,  str(number) + str(current))

    else:
        e.insert(0, str(current) + str(number))



def button_clear():
    e.delete(0, END)
    e1.delete(0, END)
    sum1 = 0



def button_del():
    num1 = float(e.get())
    num1 = int(num1/10)
    e.delete(0,END)
    e.insert(0,num1)


def button_add():
    first_number = float(e.get())
    global f_num
    global math
    math = " + "
    f_num = float(first_number)
    e.delete(0, END)
    e1.insert(END,str(first_number) + math)



def button_sub():
    first_number = float(e.get())
    global f_num
    global math
    math = " - "
    f_num = float(first_number)
    e.delete(0, END)
    e1.insert(END,str(first_number) + math)

def button_mul():
    first_number = float(e.get())
    global f_num
    global math
    math = " x "
    f_num = float(first_number)
    e.delete(0, END)
    e1.insert(END,str(first_number) + math)


def button_div():
    first_number = float(e.get())
    global f_num
    global math
    math = " / "
    f_num = float(first_number)
    e.delete(0, END)
    e1.insert(END, str(first_number) + math)

def button_mod():
    first_number = float(e.get())
    global f_num
    global math
    math = " % "
    f_num = float(first_number)
    e.delete(0, END)
    e1.insert(END, str(first_number) + math)

def button_sqr():
    first_number = float(e.get())
    global f_num
    global math
    math = "\u00B2 "
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0,str(f_num**2))

def button_inv():
    first_number = float(e.get())
    global f_num
    global math
    math = " 1/x "
    f_num = float(first_number)
    f_num = 1 / f_num
    e.delete(0, END)
    e.insert(0,f_num)

def button_raise():
    first_number = float(e.get())
    global f_num
    global math
    math = " ^ "
    f_num = float(first_number)
    e.delete(0, END)
    e1.insert(END, str(first_number) + math)

def button_root():
    first_number = float(e.get())
    global f_num
    global math
    math = " \u221A"
    f_num = float(first_number) ** 0.5
    e.delete(0, END)
    e.insert(0, f_num)

def button_equal():
    second_number = float(e.get())
    e.delete(0, END)
    if (math == " + "):
        e.insert(0,f_num + second_number)
        e1.insert(END, str(second_number) + " = ")
    elif (math == " - "):
        e.insert(0, f_num - second_number)
        e1.insert(END, str(second_number) + " = ")
    elif (math == " x "):
        e.insert(0, f_num * second_number)
        e1.insert(END, str(second_number) + " = ")
    elif (math == " / "):
        e.insert(0, f_num / second_number)
        e1.insert(END, str(second_number) + " = ")
    elif (math == " % "):
        e.insert(0, f_num % second_number)
        e1.insert(END, str(second_number) + " = ")
    elif (math == " ^ "):
        e.insert(0, f_num ** second_number)
        e1.insert(END, str(second_number) + " = ")
    elif (math == "\u00B2 "):
        e.delete(0, END)
        e.insert(0, str(f_num ** 2))
        e1.delete(0, END)
        e1.insert(END, str(f_num) + math)
    elif (math == " \u221A"):
        e.insert(0, f_num)
    elif (math == " 1/x "):
        e.insert(0, f_num)



one_button = Button(window,text="1",command=lambda: button_click(1),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
two_button = Button(window,text="2",command=lambda: button_click(2),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
three_button = Button(window,text="3",command=lambda: button_click(3),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
four_button = Button(window,text="4",command=lambda: button_click(4),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
five_button = Button(window,text="5",command=lambda: button_click(5),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
six_button = Button(window,text="6",command=lambda: button_click(6),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
seven_button = Button(window,text="7",command=lambda: button_click(7),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
eight_button = Button(window,text="8",command=lambda: button_click(8),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
nine_button = Button(window,text="9",command=lambda: button_click(9),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
zero_button = Button(window,text="0",command=lambda: button_click(0),padx=28.4998,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
dot_button = Button(window,text=".",command=lambda: button_click("."),padx=28,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)
plusminus_button = Button(window,text="+/-",command=lambda: button_click("-"),padx=20.3,pady=10,borderwidth=0,bg="#fbfbfb", font=fontnumber1)

submit_button = Button(window,text="=",padx=24,pady=6,borderwidth=0,command=lambda: button_equal(),bg="#4d94ff", font=fontnumber)

clear_button = Button(window,text="CE",padx=24,pady=10.5,borderwidth=0,command=lambda: button_clear(),bg="#d8d8d8", font=fontnumber1)

add_button = Button(window,text="+",padx=24,pady=6,borderwidth=0,command=lambda: button_add(),bg="#f2f2f2", font=fontnumber)
sub_button = Button(window,text="-",padx=24,pady=6,borderwidth=0,command=lambda: button_sub(),bg="#f2f2f2", font=fontnumber)
mul_button = Button(window,text="x",padx=24,pady=6,borderwidth=0,command=lambda: button_mul(),bg="#f2f2f2", font=fontnumber)
div_button = Button(window,text="/",padx=24,pady=7,borderwidth=0,command=lambda: button_div(),bg="#f2f2f2", font=fontnumber)
mod_button = Button(window,text="%",padx=24,pady=8,borderwidth=0,command=lambda: button_mod(),bg="#f2f2f2", font=fontnumber)
sqr_button = Button(window,text="X\u00B2",padx=23,pady=11,borderwidth=0,command=lambda: button_sqr(),bg="#f2f2f2", font=fontnumber2)
raise_button = Button(window,text="X\252",padx=24,pady=11,borderwidth=0,command=lambda: button_raise(),bg="#f2f2f2", font=fontnumber2)
inv_button = Button(window,text="1/X",padx=20,pady=11,borderwidth=0,command=lambda: button_inv(),bg="#f2f2f2", font=fontnumber2)
root_button = Button(window,text="\u221AX",padx=23,pady=11,borderwidth=0,command=lambda: button_root(),bg="#f2f2f2", font=fontnumber2)
del_button = Button(window,text="\u232B",padx=18.4,pady=7,borderwidth=0,command=lambda: button_del(),bg="#d8d8d8", font=fontnumber)

seven_button.grid(row=6,column=0, padx=1, pady=1)
eight_button.grid(row=6,column=1, padx=1, pady=1)
nine_button.grid(row=6,column=2, padx=1, pady=1)

four_button.grid(row=7,column=0, padx=1, pady=1)
five_button.grid(row=7,column=1, padx=1, pady=1)
six_button.grid(row=7,column=2, padx=1, pady=1)

one_button.grid(row=8,column=0, padx=1, pady=1)
two_button.grid(row=8,column=1, padx=1, pady=1)
three_button.grid(row=8,column=2, padx=1, pady=1)

zero_button.grid(row=9,column=1, padx=1, pady=1)
plusminus_button.grid(row=9,column=0, padx=1, pady=1)
dot_button.grid(row=9,column=2, padx=1, pady=1)

submit_button.grid(row=9,column=3,columnspan=1, padx=1, pady=1)
clear_button.grid(row=3,column=2, padx=1, pady=1)

add_button.grid(row=8,column=3, padx=1, pady=1)
sub_button.grid(row=7,column=3, padx=1, pady=1)
mul_button.grid(row=6,column=3, padx=1, pady=1)
div_button.grid(row=5,column=3, padx=1, pady=1)
mod_button.grid(row=3,column=0, padx=1, pady=1)
sqr_button.grid(row=5,column=1, padx=1, pady=1)
raise_button.grid(row=3,column=1, padx=1, pady=1)
inv_button.grid(row=5,column=0, padx=1, pady=1)
root_button.grid(row=5,column=2, padx=1, pady=1)
del_button.grid(row=3,column=3, padx=1, pady=1)

window.mainloop()

