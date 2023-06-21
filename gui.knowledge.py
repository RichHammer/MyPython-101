from tkinter import *
from tkinter import ttk #import theme of tk
from tkinter import messagebox

gui=Tk() #หน้าจอหลัก
gui.title('note program')
gui.geometry('500x400') #ความกว้างและความสูงของหน้าจอโปรแกรม

L1=Label(gui,text='note program',font=('arial',20),fg='red')
L1.place(x=30,y=20)

#B1=Button(gui,text='how much money do you have?')#สร้างปุ่ม
#B1.pack() #pack() เป็นคำสั่งที่ทำให้ปุ่มอยู่กลางหน้าจอ
#B2=ttk.Button(gui,text='how much money do you have?')
#B2.pack() #ปุ่มสวยขึ้น
#B2.pack(ipadx=20,ipady=30)
#B2.place(x=50,y=200) #(0,0) จะอยู่ที่ซ้ายบน

def Button2():
    text='You have 30000 baht'
    messagebox.showinfo('amount of money',text)
    

FB1=Frame(gui) #คล้ายกระดาน,เป็นการใส่กรอบให้ปุ่ม
FB1.place(x=200,y=50)
B2=ttk.Button(FB1,text='how much money do you have?',command=Button2)
B2.pack(ipadx=20,ipady=30)

FB2=LabelFrame(gui,text='money') #ระบุข้อความในพื้นที่กรอบได้
FB2.place(x=100,y=100)
B3=ttk.Button(FB2,text='เงินเงินเงิน')
B3.pack(ipadx=30,ipady=30,padx=35,pady=35) #pad จะมีไว้กำหนดขนาดกรอบ

gui.mainloop()
