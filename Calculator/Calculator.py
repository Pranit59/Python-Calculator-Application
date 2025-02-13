from tkinter import * 

def click(event):
    text=event.widget.cget('text')
    #print(text)
    if(text=='='):
        if(svalue.get().isdigit()):
            value=int(svalue.get())
            
        else:
            value=eval(e1.get())
        svalue.set(value)
        e1.update()
         
    elif(text=='AC'):
        svalue.set('')
        e1.update()
    else:
        svalue.set(svalue.get()+text)        
 
root=Tk()
root.title('Calculator')
root.geometry('430x600')
root.resizable(False, False)
root.config(bg='Black')

svalue=StringVar()
svalue.set('')

Label(root,text='Calculator',bg='Black',fg='White',font="Century 20 bold").pack(pady=30)

e1=Entry(root,font='Century 40 bold',fg='white',bg='Black',width=14,relief=GROOVE,textvariable=svalue)     
e1.pack(pady=5)

f=Frame(root)
f.config(bg='Black')

b=Button(f,text='7',font='Century 23 bold',width=3,fg='White',bg='black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='8',font='Century 23 bold',width=3,fg='white',bg='Black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='9',font='Century 23 bold',width=3,fg='white',bg='Black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='*',font='Century 23 bold',width=3,fg='white',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

f.pack()

f=Frame(root)
f.config(bg='Black')

b=Button(f,text='4',font='Century 23 bold',width=3,fg='white',bg='black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='5',font='Century 23 bold',width=3,fg='white',bg='black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='6',font='Century 23 bold',width=3,fg='white',bg='black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='-',font='Century 23 bold',width=3,fg='White',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

f.pack()

f=Frame(root)
f.config(bg='Black')

b=Button(f,text='1',font='Century 23 bold',width=3,fg='White',bg='black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='2',font='Century 23 bold',width=3,fg='White',bg='black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='3',font='Century 23 bold',width=3,fg='White',bg='black',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='+',font='Century 23 bold',width=3,fg='White',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

f.pack()

f=Frame(root)
f.config(bg='Black')

b=Button(f,text='00',font='Century 23 bold',width=3,fg='White',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='0',font='Century 23 bold',width=3,fg='White',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='.',font='Century 23 bold',width=3,fg='White',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='/',font='Century 23 bold',width=3,fg='White',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

f.pack()

f=Frame(root)
f.config(bg='Black')

b=Button(f,text='AC',font='Century 21 bold',width=14,fg='white',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

b=Button(f,text='=',font='Century 23 bold',width=3,fg='White',bg='LightSteelBlue4',relief=GROOVE)
b.bind('<Button-1>',click)
b.pack(side=LEFT,padx=14,pady=10)

f.pack()

root.mainloop() 


