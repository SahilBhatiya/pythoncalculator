
from tkinter import *
import tkinter.font as tkFont

window = Tk()




window.iconbitmap("calculator1.ico")
window.resizable(0,0)
window.title("SB Softwares: Calculator")
window.configure(padx=3,pady=10,bg="#ffffff", borderwidth=0, relief="flat")

window.wm_attributes("-alpha",0.9825)
window.minsize(290,450)
window.maxsize(290,450)





fontStyle = tkFont.Font(family="comic sans ms", size=17, weight="bold")
fontnumber = tkFont.Font(family="comic sans ms", size=12, weight='normal')
fontnumber1 = tkFont.Font(family="comic sans ms", size=10, weight='bold')
fontnumber2 = tkFont.Font(family="comic sans ms", size=10, weight='normal')
fontnumber3 = tkFont.Font(family="comic sans ms", size=9, weight='normal')
fontnumber4 = tkFont.Font(family="comic sans ms", size=7, weight='bold')

title_bar = Label(window,text="Sahil's Calculator", fg ="#ffffff",bg="#ffffff", font=fontnumber1,justify="left")
#close_btn = Button(window,text="X" ,bg="#ff6666",font=fontnumber4,command=window.destroy,bd=0,padx=24,pady=2,fg="white")
title_bar.grid(row=0,column=0,columnspan=3,padx=1,pady=5)
#close_btn.grid(row=0,column=3,padx=1,pady=1)


e = Entry(window,width=20,borderwidth=0,bg="#ffffff", font=fontStyle, state = "disabled", disabledbackground="#ffffff",readonlybackground="#ffffff", cursor="arrow")
e.grid(row=2, column=0, columnspan=4,padx=0,pady=20)
e.config(justify="right")
e.size()

e1 = Entry(window, width=38, borderwidth=0, bg="#ffffff", font=fontnumber3, state = "disabled", disabledbackground="#ffffff", cursor="arrow")
e1.grid(row=1, column=0, columnspan=4,padx=0,pady=5)
e1.config(justify="right")

def button_click(number):
    global m_i
    e.config(state = "normal")
    e1.config(state = "normal")
    current = e.get()
    e.delete(0, END)
    if (number == "-"):
        e.insert(0,  str(number) + str(current))

    else:
        e.insert(0, str(current) + str(number))
    if(m_i >= 1):
        button_equal()
    e.config(state="disabled")
    e1.config(state="disabled")


def button_clear():
    global m_i, f_num, first_number, second_number, math
    first_number = 0
    second_number = 0
    f_num = 0
    math = ""
    m_i = 0
    e.config(state="normal")
    e1.config(state="normal")
    e.delete(0, END)
    e1.delete(0, END)
    sum1 = 0
    e.config(state="disabled")
    e1.config(state="disabled")



def button_del():
    e.config(state="normal")
    e1.config(state="normal")
    num1 = str(e.get())
    if(len(num1) - 1 == 0):
        num1 = 0
    else:
        num1 = num1[0:len(num1) - 1]
    e.delete(0,END)
    e.insert(0,num1)
    button_equal()
    e.config(state="disabled")
    e1.config(state="disabled")


def button_equal():
    global f_num
    global first_number
    global second_number
    e.config(state="normal")
    e1.config(state="normal")
    if(math == ""):
        pass
    elif(math == " + "):
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(second_number))
        f_num = float(first_number + second_number)
        e1.insert(END, " = " + str(f_num))

    elif (math == " - "):
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(second_number))
        f_num = float(first_number - second_number)
        e1.insert(END, " = " + str(f_num))

    elif (math == " x "):
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(second_number))
        f_num = float(first_number * second_number)
        e1.insert(END, " = " + str(f_num))

    elif (math == " / "):
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(second_number))
        f_num = float(first_number / second_number)
        e1.insert(END, " = " + str(f_num))

    elif (math == " % "):
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(second_number))
        f_num = float(first_number % second_number)
        e1.insert(END, " = " + str(f_num))


    elif (math == "\u00B2 "):
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(2))
        f_num = float(second_number ** 2)
        e1.insert(END, " = " + str(f_num))

    elif (math == "^"):
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(second_number))
        f_num = float(first_number ** second_number)
        e1.insert(END, " = " + str(f_num))

    e.config(state="disabled")
    e1.config(state="disabled")

def button_tt():
    global f_num
    e.config(state="normal")
    e.delete(0, END)
    e.insert(0, f_num)
    e.config(state="disabled")

m_i = 0
def button_add():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = " + "
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if(m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number)
        e.delete(0, END)
        e1.insert(0, str(first_number) + math)
    else:
        e.delete(0, END)
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        button_equal()


    e.config(state="disabled")
    e1.config(state="disabled")




def button_sub():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = " - "
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if(m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number)
        e.delete(0, END)
        e1.insert(END,str(first_number) + math)
    else:
        e.delete(0, END)
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        button_equal()

    e.config(state="disabled")
    e1.config(state="disabled")


def button_mul():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = " x "
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if(m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number)
        e.delete(0, END)
        e1.insert(END,str(first_number) + math)

    else:
        e.delete(0, END)
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        button_equal()
    e.config(state="disabled")
    e1.config(state="disabled")


def button_div():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = " / "
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if(m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number)
        e.delete(0, END)
        e1.insert(END, str(first_number) + math)
    else:
        e.delete(0, END)
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        button_equal()
    e.config(state="disabled")
    e1.config(state="disabled")

def button_mod():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = " % "
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if (m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number)
        e.delete(0, END)
        e1.insert(END, str(first_number) + math)
    else:
        e.delete(0, END)
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        button_equal()
    e.config(state="disabled")
    e1.config(state="disabled")

def button_sqr():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = "\u00B2 "
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if (m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number ** 2)
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(2))
        f_num = float(second_number ** 2)
        e1.insert(END, " = " + str(f_num))
        button_tt()
    else:
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(first_number) + math + str(2))
        f_num = float(second_number ** 2)
        e1.insert(END, " = " + str(f_num))
        button_tt()


    e.config(state="disabled")
    e1.config(state="disabled")

def button_inv():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = "/"
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if (m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number ** 2)
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(1) + math + str(first_number))
        f_num = float(1 / second_number)
        e1.insert(END, " = " + str(f_num))
        button_tt()
    else:
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, str(1) + math + str(first_number))
        f_num = float(1 / second_number)
        e1.insert(END, " = " + str(f_num))
        button_tt()

    e.config(state="disabled")
    e1.config(state="disabled")

def button_raise():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = "^"
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if (m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number)
        e.delete(0, END)
        e1.insert(END, str(first_number) + math)
    else:
        e.delete(0, END)
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        button_equal()
    e.config(state="disabled")
    e1.config(state="disabled")


def button_root():
    global m_i
    global f_num
    global math
    global first_number
    global second_number
    math = "\u221A"
    m_i = m_i + 1
    e.config(state="normal")
    e1.config(state="normal")
    if (m_i == 1):
        first_number = float(e.get())
        f_num = float(first_number ** 0.5)
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, math + str(first_number))
        f_num = float(second_number ** 0.5)
        e1.insert(END, " = " + str(f_num))
        button_tt()
    else:
        first_number = f_num
        e1.delete(0, END)
        e1.insert(0, str(first_number) + math)
        second_number = float(e.get())
        e1.delete(0, END)
        e1.insert(END, math + str(first_number))
        f_num = float(second_number ** 0.5)
        e1.insert(END, " = " + str(f_num))
        button_tt()


    e.config(state="disabled")
    e1.config(state="disabled")





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

submit_button = Button(window,text="=",padx=25,pady=6.5,borderwidth=0,command=lambda: button_tt(),bg="#4885ef", fg="#ffffff", font=fontnumber)

clear_button = Button(window,text="CE",padx=24,pady=10.4999,borderwidth=0,command=lambda: button_clear(),bg="#e8e8e8", font=fontnumber1)

add_button = Button(window,text="+",padx=25,pady=6.5,borderwidth=0,command=lambda: button_add(),bg="#f6f6f6", font=fontnumber)
sub_button = Button(window,text="-",padx=24,pady=7,borderwidth=0,command=lambda: button_sub(),bg="#f6f6f6", font=fontnumber)
mul_button = Button(window,text="x",padx=24,pady=7,borderwidth=0,command=lambda: button_mul(),bg="#f6f6f6", font=fontnumber)
div_button = Button(window,text="/",padx=24,pady=7,borderwidth=0,command=lambda: button_div(),bg="#f6f6f6", font=fontnumber)
mod_button = Button(window,text="%",padx=24,pady=7,borderwidth=0,command=lambda: button_mod(),bg="#f6f6f6", font=fontnumber)
sqr_button = Button(window,text="X\u00B2",padx=23,pady=11,borderwidth=0,command=lambda: button_sqr(),bg="#f6f6f6", font=fontnumber2)
raise_button = Button(window,text="X\252",padx=24,pady=11,borderwidth=0,command=lambda: button_raise(),bg="#f6f6f6", font=fontnumber2)
inv_button = Button(window,text="1/X",padx=20,pady=11,borderwidth=0,command=lambda: button_inv(),bg="#f6f6f6", font=fontnumber2)
root_button = Button(window,text="\u221AX",padx=24,pady=11,borderwidth=0,command=lambda: button_root(),bg="#f6f6f6", font=fontnumber2)
del_button = Button(window,text="\u232B",padx=18.4,pady=6.5,borderwidth=0,command=lambda: button_del(),bg="#e8e8e8", font=fontnumber)

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

window.bind_all("9", lambda event:button_click(9))
window.bind_all("8", lambda event:button_click(8))
window.bind_all("7", lambda event:button_click(7))
window.bind_all("6", lambda event:button_click(6))
window.bind_all("5", lambda event:button_click(5))
window.bind_all("4", lambda event:button_click(4))
window.bind_all("3", lambda event:button_click(3))
window.bind_all("2", lambda event:button_click(2))
window.bind_all("1", lambda event:button_click(1))
window.bind_all("0", lambda event:button_click(0))
window.bind_all(".", lambda event:button_click("."))
window.bind_all("<BackSpace>", lambda event:button_del())
window.bind_all("c", lambda event:button_clear())
window.bind_all("C", lambda event:button_clear())
window.bind_all("<Delete>", lambda event:button_clear())
window.bind_all("/", lambda event:button_div())
window.bind_all("*", lambda event:button_mul())
window.bind_all("-", lambda event:button_sub())
window.bind_all("+", lambda event:button_add())
window.bind_all("<Return>", lambda event:button_tt())
window.bind_all("s", lambda event:button_sqr())
window.bind_all("S", lambda event:button_sqr())
window.bind_all("r", lambda event:button_root())
window.bind_all("R", lambda event:button_root())
window.bind_all("a", lambda event:button_raise())
window.bind_all("A", lambda event:button_raise())
window.bind_all("m", lambda event:button_mod())
window.bind_all("M", lambda event:button_mod())
window.bind_all("x", lambda event:button_inv())
window.bind_all("X", lambda event:button_inv())





def add_button_animation_enter(e):
    add_button.configure(bg="#dfdfdf")

def add_button_animation_leave(e):
    add_button.configure(bg="#f6f6f6")

add_button.bind("<Enter>", add_button_animation_enter)
add_button.bind("<Leave>", add_button_animation_leave)


def sub_button_animation_enter(e):
    sub_button.configure(bg="#dfdfdf")

def sub_button_animation_leave(e):
    sub_button.configure(bg="#f6f6f6")

sub_button.bind("<Enter>", sub_button_animation_enter)
sub_button.bind("<Leave>", sub_button_animation_leave)


def mul_button_animation_enter(e):
    mul_button.configure(bg="#dfdfdf")

def mul_button_animation_leave(e):
    mul_button.configure(bg="#f6f6f6")

mul_button.bind("<Enter>", mul_button_animation_enter)
mul_button.bind("<Leave>", mul_button_animation_leave)


def div_button_animation_enter(e):
    div_button.configure(bg="#dfdfdf")

def div_button_animation_leave(e):
    div_button.configure(bg="#f6f6f6")

div_button.bind("<Enter>", div_button_animation_enter)
div_button.bind("<Leave>", div_button_animation_leave)


def mod_button_animation_enter(e):
    mod_button.configure(bg="#dfdfdf")

def mod_button_animation_leave(e):
    mod_button.configure(bg="#f6f6f6")

mod_button.bind("<Enter>", mod_button_animation_enter)
mod_button.bind("<Leave>", mod_button_animation_leave)


def sqr_button_animation_enter(e):
    sqr_button.configure(bg="#dfdfdf")

def sqr_button_animation_leave(e):
    sqr_button.configure(bg="#f6f6f6")

sqr_button.bind("<Enter>", sqr_button_animation_enter)
sqr_button.bind("<Leave>", sqr_button_animation_leave)


def raise_button_animation_enter(e):
    raise_button.configure(bg="#dfdfdf")

def raise_button_animation_leave(e):
    raise_button.configure(bg="#f6f6f6")

raise_button.bind("<Enter>", raise_button_animation_enter)
raise_button.bind("<Leave>", raise_button_animation_leave)


def inv_button_animation_enter(e):
    inv_button.configure(bg="#dfdfdf")

def inv_button_animation_leave(e):
    inv_button.configure(bg="#f6f6f6")

inv_button.bind("<Enter>", inv_button_animation_enter)
inv_button.bind("<Leave>", inv_button_animation_leave)


def root_button_animation_enter(e):
    root_button.configure(bg="#dfdfdf")

def root_button_animation_leave(e):
    root_button.configure(bg="#f6f6f6")

root_button.bind("<Enter>", root_button_animation_enter)
root_button.bind("<Leave>", root_button_animation_leave)


def del_button_animation_enter(e):
    del_button.configure(bg="#b0b0b0")

def del_button_animation_leave(e):
    del_button.configure(bg="#e8e8e8")

del_button.bind("<Enter>", del_button_animation_enter)
del_button.bind("<Leave>", del_button_animation_leave)


def clear_button_animation_enter(e):
    clear_button.configure(bg="#b0b0b0")

def clear_button_animation_leave(e):
    clear_button.configure(bg="#e8e8e8")

clear_button.bind("<Enter>", clear_button_animation_enter)
clear_button.bind("<Leave>", clear_button_animation_leave)


def submit_button_animation_enter(e):
    submit_button.configure(bg="#78b5ff")

def submit_button_animation_leave(e):
    submit_button.configure(bg="#4885ef")

submit_button.bind("<Enter>", submit_button_animation_enter)
submit_button.bind("<Leave>", submit_button_animation_leave)


def zero_button_animation_enter(e):
    zero_button.configure(bg="#ededed")

def zero_button_animation_leave(e):
    zero_button.configure(bg="#fbfbfb")

zero_button.bind("<Enter>", zero_button_animation_enter)
zero_button.bind("<Leave>", zero_button_animation_leave)


def one_button_animation_enter(e):
    one_button.configure(bg="#ededed")

def one_button_animation_leave(e):
    one_button.configure(bg="#fbfbfb")

one_button.bind("<Enter>", one_button_animation_enter)
one_button.bind("<Leave>", one_button_animation_leave)


def two_button_animation_enter(e):
    two_button.configure(bg="#ededed")

def two_button_animation_leave(e):
    two_button.configure(bg="#fbfbfb")

two_button.bind("<Enter>", two_button_animation_enter)
two_button.bind("<Leave>", two_button_animation_leave)


def three_button_animation_enter(e):
    three_button.configure(bg="#ededed")

def three_button_animation_leave(e):
    three_button.configure(bg="#fbfbfb")

three_button.bind("<Enter>", three_button_animation_enter)
three_button.bind("<Leave>", three_button_animation_leave)


def four_button_animation_enter(e):
    four_button.configure(bg="#ededed")

def four_button_animation_leave(e):
    four_button.configure(bg="#fbfbfb")

four_button.bind("<Enter>", four_button_animation_enter)
four_button.bind("<Leave>", four_button_animation_leave)


def five_button_animation_enter(e):
    five_button.configure(bg="#ededed")

def five_button_animation_leave(e):
    five_button.configure(bg="#fbfbfb")

five_button.bind("<Enter>", five_button_animation_enter)
five_button.bind("<Leave>", five_button_animation_leave)


def six_button_animation_enter(e):
    six_button.configure(bg="#ededed")

def six_button_animation_leave(e):
    six_button.configure(bg="#fbfbfb")

six_button.bind("<Enter>", six_button_animation_enter)
six_button.bind("<Leave>", six_button_animation_leave)


def seven_button_animation_enter(e):
    seven_button.configure(bg="#ededed")

def seven_button_animation_leave(e):
    seven_button.configure(bg="#fbfbfb")

seven_button.bind("<Enter>", seven_button_animation_enter)
seven_button.bind("<Leave>", seven_button_animation_leave)


def eight_button_animation_enter(e):
    eight_button.configure(bg="#ededed")

def eight_button_animation_leave(e):
    eight_button.configure(bg="#fbfbfb")

eight_button.bind("<Enter>", eight_button_animation_enter)
eight_button.bind("<Leave>", eight_button_animation_leave)



def nine_button_animation_enter(e):
    nine_button.configure(bg="#ededed")

def nine_button_animation_leave(e):
    nine_button.configure(bg="#fbfbfb")

nine_button.bind("<Enter>", nine_button_animation_enter)
nine_button.bind("<Leave>", nine_button_animation_leave)



def dot_button_animation_enter(e):
    dot_button.configure(bg="#ededed")

def dot_button_animation_leave(e):
    dot_button.configure(bg="#fbfbfb")

dot_button.bind("<Enter>", dot_button_animation_enter)
dot_button.bind("<Leave>", dot_button_animation_leave)



def plusminus_button_animation_enter(e):
    plusminus_button.configure(bg="#ededed")

def plusminus_button_animation_leave(e):
    plusminus_button.configure(bg="#fbfbfb")

plusminus_button.bind("<Enter>", plusminus_button_animation_enter)
plusminus_button.bind("<Leave>", plusminus_button_animation_leave)


window.mainloop()

