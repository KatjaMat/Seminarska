from  tkinter import *
import random

class Kaca:
    def __init__(self,master):
        self.canvas = Canvas(master, width = 700, height = 700, background = "light sky blue") #faking nebesno plava
        self.canvas.pack()
        self.IDkrogec = None
        self.IDkaca = None
        self.xKaca = random.randint(60, 640)
        self.yKaca = random.randint(60, 640)
        self.dKaca = 10
        self.dKrogec = 8
        self.narisiKrogec()
        self.narisiKaca(self.xKaca, self.yKaca)
        self.smer = 0
        self.canvas.bind_all('<Left>', self.levo)
        self.canvas.bind_all('<Right>', self.desno)
        self.premik()

        menu = Menu(root)
        root.config(menu = menu)

        #FRAME

        self.gumbStart = Button(self.canvas, text = 'START')
        self.gumbStart.configure(width = 10, height = 5)
        self.gumbStart_window = self.canvas.create_window(350, 350, window = self.gumbStart)





    def narisiKaca(self, xKaca, yKaca):
        self.IDkaca = self.canvas.create_oval(xKaca-self.dKaca,yKaca-self.dKaca,xKaca+self.dKaca,yKaca+self.dKaca,fill='black')


    def narisiKrogec(self):
        '''na random mesto na platnu narišemo krogec'''
        x = random.randint(10,690)
        y = random.randint(10,690)
        self.IDkrogec=self.canvas.create_oval(x-self.dKrogec,y-self.dKrogec,x+self.dKrogec,y+self.dKrogec, fill='red', outline='black')

    def levo(self,event):
        self.smer = (self.smer + 1) % 4

    def desno(self,event):
        self.smer = (self.smer - 1) % 4


    def premik(self):

        sez = [ (1,0), (0,-1), (-1,0), (0,1)]

        self.xKaca += sez[self.smer][0]
        self.yKaca += sez[self.smer][1]

        #xpremik = self.xKaca
        #ypremik = self.yKaca
        self.canvas.coords(self.IDkaca, self.xKaca-self.dKaca,self.yKaca-self.dKaca,self.xKaca+self.dKaca,self.yKaca+self.dKaca)
        self.canvas.after(30, self.premik)





















root = Tk()

aplikacija = Kaca(root)

root.mainloop()