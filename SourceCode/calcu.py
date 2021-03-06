from tkinter import *
from tkinter import messagebox
import math
####GUI###window###setup
window=Tk()
window.title("Rishabh_calc")
window.maxsize(width=357,height=300)
window.minsize(width=290,height=300)
window.geometry('290x300')
window.configure(bg='powderblue')
window.iconbitmap('Blackvariant-Shadow135-System-Calculator.ico')

###button functions###
def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)
def clear():
    global operator
    operator=''
    tex.set(operator)
def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Error','DONT give first place AS Decimal!! Try again')

def sinf():
    try:
        global operator
        result=math.sin(eval(tex.get()))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Preerror','Give parameters First')


def cosf():
    try:

        global operator
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Preerror', 'Give parameters First')


def tanf():
    try:
         global operator
         result = math.tan(eval(tex.get()))
         operator = str(result)
         tex.set(operator)
    except:
        messagebox.showinfo('Preerror', 'Give parameters First')


def sqrtf():
    try:
         global operator
         result = math.sqrt(eval(tex.get()))
         operator = str(result)
         tex.set(operator)
    except:
        messagebox.showinfo('Preerror', 'Give parameters First')


def logf():
    try:

        global operator
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Preerror', 'Give parameters First')


tex=StringVar()
operator=''
######buttons#####
##################
#entry block
entry1=Entry(window,bg='black',fg='cyan',font=("DS-DIGITAL",20),justify='right',bd=16,textvariable=tex)
entry1.grid(row=0,column=0,columnspan=4)
#buttons 1row

but7=Button(text='7',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(7))
but7.grid(row=1,column=0)

but8=Button(text='8',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(8))
but8.grid(row=1,column=1)

but9=Button(text='9',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(9))
but9.grid(row=1,column=2)

butadd=Button(text='+',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click('+'))
butadd.grid(row=1,column=3)


#button 2 row
but4=Button(text='4',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(4))
but4.grid(row=2,column=0)

but5=Button(text='5',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(5))
but5.grid(row=2,column=1)

but6=Button(text='6',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(6))
but6.grid(row=2,column=2)

butsub=Button(text='-',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click('-'))
butsub.grid(row=2,column=3)



#button row3
but1=Button(text='1',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(1))
but1.grid(row=3,column=0)

but2=Button(text='2',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(2))
but2.grid(row=3,column=1)

but3=Button(text='3',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click(3))
but3.grid(row=3,column=2)

butmul=Button(text='*',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='15',pady='15',command=lambda:click('*'))
butmul.grid(row=3,column=3)

#button 4 row
butclr=Button(text='clr',bg='black',fg='cyan',font=("DS-DIGITAL",11),padx='12',pady='13',command=clear)
butclr.grid(row=4,column=0)

but0=Button(text='0',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='13',pady='12',command=lambda:click(0))
but0.grid(row=4,column=1)

butdiv=Button(text='/',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='13',pady='12',command=lambda:click('/'))
butdiv.grid(row=4,column=2)

butmequal=Button(text='=',bg='black',fg='cyan',font=("DS-DIGITAL",15),padx='13',pady='12',command=equal)
butmequal.grid(row=4,column=3)
##SpecialButtons
butsin=Button(text='sin',bg='black',fg='cyan',font=("DS-DIGITAL",11),padx='17',pady='15',command=sinf)
butsin.grid(row=0,column=4)

butcos=Button(text='cos',bg='black',fg='cyan',font=("DS-DIGITAL",11),padx='17',pady='15',command=cosf)
butcos.grid(row=1,column=4)

buttan=Button(text='tan',bg='black',fg='cyan',font=("DS-DIGITAL",11),padx='17',pady='15',command=tanf)
buttan.grid(row=2,column=4)

butsqrt=Button(text='sqrt',bg='black',fg='cyan',font=("DS-DIGITAL",10),padx='17',pady='15',command=sqrtf)
butsqrt.grid(row=3,column=4)

butlog=Button(text='log',bg='black',fg='cyan',font=("DS-DIGITAL",11),padx='17',pady='15',command=logf)
butlog.grid(row=4,column=4)





window.mainloop()