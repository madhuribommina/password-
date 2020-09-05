from tkinter import *
import random

r=Tk()
r.title("pwd generator")
r.geometry("200x200")

#creating pswd generator
def generate():
    global ad
    #t=Toplevel()
    
    maxlen=12
    alp_l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    smy_l=['#','@','!','$','*','&']
    num_l=['1','2','3','4','5','6','7','8','9']
    full_l=alp_l+smy_l+num_l
    alp=random.choice(alp_l)
    smy=random.choice(smy_l)
    num=random.choice(num_l)
    ran=alp+smy+num
    
    for i in range(maxlen-3):
        ran=ran+random.choice(full_l)
    print(ran)
    ran=list(ran)
    #ran_l=array.array(&# 039;u&# 039;,ran)
    for i in range(3):
        random.shuffle(ran)
        
    pswd=''
    for i in ran:
        pswd=pswd+i
    
    l=Label(r,text=pswd.get())
    l.grid(row=3,column=1)
    
    
    
l=Label(r,text="click here to generate a pswd",)
l.grid(row=1,column=0)
#create a pswd generate button
geb=Button(r,text="click",command=generate)
geb.grid(row=2,column=1)
r.mainloop()
