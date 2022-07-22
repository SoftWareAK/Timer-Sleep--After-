import time
from tkinter import*

#for i in range(30,0,-1):
   # print(i)
   # time.sleep(1) # 1 sn aralıklarla 30dan geriye 1 er azalarak say

   #time komutu py2 de varken 3 te kaldırılmıştır
   #sleep komutu py 3 te after komutu ile çalışır


pencere=Tk()
i=0
def yaz():
   global i
   i=i+1
   l.configure(text=str(i))
   pencere.after(1000,yaz)


l=Label(text=0,font="Verdana 16 bold" )
l.place(x=10,y=10)

yaz()

pencere.mainloop()