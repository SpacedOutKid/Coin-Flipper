from tkinter import *
import random

#Function for heads button
def headsFunc():
    C=['heads','tails']
    flip=random.choice(C)
    if flip=='heads':
        result=('You Win It Was Heads')
        results.set(result)
    else:
        result=('You Lose It Was Tails')
        results.set(result)

#Function for tails button
def tailsFunc():
    C=['heads','tails']
    flip=random.choice(C)
    if flip=='tails':
        result=('You Win It Was Tails')
        results.set(result)
    else:
        result=('You Lose It Was Heads')
        results.set(result)


master=Tk()
master.title('Coin Flipper')
title=Label(master,text='Heads or Tails?',font=('Agency FB',18,'bold italic'),borderwidth=4, relief='raised')
title.config(width=15)
title.grid(row=0,column=0,columnspan=2,padx=30,pady=10)
    #Creates a label for the game with a border and the window
master.geometry('200x200')



#creates the heads and tails buttons 
headsButton=Button(master,text='HEADS',command=headsFunc,font=('Colonna MT',12,))
headsButton.grid(row=1,column=0,columnspan=3,padx=15,pady=25,sticky=W)
headsButton.config(bd=3,relief='raised')
tailsButton=Button(master,text='TAILS',command=tailsFunc,font=('Colonna MT',12))
tailsButton.grid(row=1,column=1,columnspan=3,padx=15,pady=25,sticky=E)
tailsButton.config(bd=3, relief='raised')
    #Configures the buttons borders 

#creates the entry box that displays the result
results=StringVar()
resultEnt=Entry(state='readonly',textvariable=results,font=('impact',12))
resultEnt.grid(column=0,columnspan=3,row=3,pady=13,padx=8,sticky=SW)
