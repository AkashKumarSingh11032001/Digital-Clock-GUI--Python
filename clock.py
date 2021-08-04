#---> Required package's
import sys
from  tkinter import *
import time 

#---> Defining time function
def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time)
	clock.after(200,times)

#---> Tkinter Window creation
root=Tk()
root.geometry("500x250")

#---> Digital Clock text
tex =Label(root,text="Digital clock",font="times 24 bold")
tex.grid(row=0,column=2)

#---> Digital Clock main
clock=Label(root,font=("times",50,"bold"),bg="white")
clock.grid(row=2,column=2,pady=25,padx=100)
times()

#---> Hour // Minute // Second
way =Label(root,text="hours     minutes     seconds   ",font="times 15 bold")
way.grid(row=3,column=2)

#---> Main loop run
root.mainloop()