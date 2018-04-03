from  tkinter import *
import random

class Kaca:
    def __init__(self, master):
        self.canvas = Canvas(master, width = 708, height = 708, background = "light sky blue") #faking nebesno plava
        self.canvas.pack()
        self.IDkrogec = None
        self.IDkaca = None
        self.xKaca = 153
        self.yKaca = 153
        self.dKaca = 10 # velikost glave kace
        self.dKrogec = 10 # velikost bonboncka
        self.seznamGlavaRep = []
        self.podaljsaj = False
        self.narisiKrogec()
        self.narisiKaca(self.xKaca, self.yKaca)
        self.smer = 0
        self.canvas.bind_all('<Left>', self.levo)
        self.canvas.bind_all('<Right>', self.desno)


        #FRAME

        #GUMB      

        self.gumbStart = Button(master, text = 'START', command = self.pritisnjenGumb)
        self.gumbStart.configure(width = 10, height = 5)
        self.gumbStart_window = self.canvas.create_window(350, 350, window = self.gumbStart)
        self.pritisnjen = False

        #okvir
        zgornjaCrta = self.canvas.create_line(3,3,708, 3, fill = 'blue', width = 2)
        desnaCrta = self.canvas.create_line(708,3,708, 708, fill = 'blue',width = 2)
        levaCrta = self.canvas.create_line(3,3,3, 708, fill = 'blue',width = 2)
        spodnjaCrta = self.canvas.create_line(3, 708, 708, 708, fill = 'blue',width = 2)




        self.premik()   # NA KONCU

        menu = Menu(root)
        root.config(menu = menu)





    def narisiKaca(self, xKaca, yKaca):
        self.IDkaca = self.canvas.create_oval(self.xKaca - self.dKaca,
                                              self.yKaca - self.dKaca,
                                              self.xKaca + self.dKaca,
                                              self.yKaca + self.dKaca, fill = 'black')
        self.seznamGlavaRep.append(self.IDkaca)
        for i in range(1,5):
            self.seznamGlavaRep.append(self.canvas.create_oval(self.xKaca - self.dKaca - i*15,
                                              self.yKaca - self.dKaca,
                                              self.xKaca + self.dKaca -i*15,
                                              self.yKaca + self.dKaca, fill = 'pink'))

        print(self.IDkaca)
        print(self.seznamGlavaRep)
        print(self.IDkrogec)

    def narisiKrogec(self):
        '''na random mesto na platnu narišemo krogec'''
        self.xKrogec = random.randrange(13, 693, 10)
        self.yKrogec = random.randrange(13, 693, 10)
        self.IDkrogec = self.canvas.create_oval(self.xKrogec - self.dKrogec,
                                              self.yKrogec - self.dKrogec,
                                              self.xKrogec + self.dKrogec,
                                              self.yKrogec + self.dKrogec, fill='red', outline='black')

    def levo(self,event):
        self.smer = (self.smer + 1) % 4

    def desno(self,event):
        self.smer = (self.smer - 1) % 4

    def pritisnjenGumb(self):
        self.pritisnjen = True
        self.canvas.delete(self.gumbStart_window) #skrije gumb


    def preveriRob(self): #konec igre
        if self.xKaca == 3 or self.xKaca == 708 or self.yKaca == 3 or self.yKaca == 708:
            self.pritisnjen = False
            self.reset()


    def reset(self):
        self.xKaca = 153
        self.yKaca = 153
        for el in self.seznamGlavaRep:
            self.canvas.delete(el)
        self.seznamGlavaRep = []
        self.narisiKaca(self.xKaca, self.yKaca)
        self.gumbStart_window = self.canvas.create_window(350, 350, window=self.gumbStart)
        self.smer = 0


    def pojejBonboncek(self):        
        self.canvas.delete(self.IDkrogec)
        self.narisiKrogec()
        self.podaljsaj = True

        
    # kačo in krogec definiramo z seznamom koordinat
    
    def seznamKoordinatKrogca(self):
        '''krogcu priredimo seznam'''
        self.seznamKrogcaX = []
        self.seznamKrogcaY = []
        for i in range(8):
            self.seznamKrogcaX.append(self.xKrogec + i)
            self.seznamKrogcaX.append(self.xKrogec - i)
            self.seznamKrogcaY.append(self.yKrogec + i)
            self.seznamKrogcaY.append(self.yKrogec - i)
        return self.seznamKrogcaX, self.seznamKrogcaY

    def seznamKoordinatKace(self):
        '''kači priredimo seznam'''
        self.seznamKaceX = []
        self.seznamKaceY = []
        for i in range(8):
            self.seznamKaceX.append(self.xKaca + i)
            self.seznamKaceX.append(self.xKaca - i)
            self.seznamKaceY.append(self.yKaca + i)
            self.seznamKaceY.append(self.yKaca - i)
        return self.seznamKaceX, self.seznamKaceY

    #def rastiKacaRep(self):




    def premik(self):
        '''funkcija uravnava gibanje kače'''

        sez = [ (15,0), (0,-15), (-15,0), (0,15)]

        if self.pritisnjen:
            self.xKaca += sez[self.smer][0]
            self.yKaca += sez[self.smer][1]
            self.canvas.coords(self.IDkaca,
                               self.xKaca - self.dKaca,
                               self.yKaca - self.dKaca,
                               self.xKaca + self.dKaca,
                               self.yKaca + self.dKaca)


        seznamKrogca = self.seznamKoordinatKrogca()
        seznamXkrogca = seznamKrogca[0]
        seznamYkrogca = seznamKrogca[1]
        seznamKaca = self.seznamKoordinatKace()
        seznamXkaca = seznamKaca[0]
        seznamYkaca = seznamKaca[1]

        if self.pritisnjen:
            self.canvas.delete(self.seznamGlavaRep[-1])
            if self.podaljsaj == False:
                self.seznamGlavaRep.pop(-1)
            if self.smer == 0:
                self.seznamGlavaRep.insert(1, (self.canvas.create_oval(self.xKaca - self.dKaca - 15,
                                                                       self.yKaca - self.dKaca,
                                                                       self.xKaca + self.dKaca - 15,
                                                                       self.yKaca + self.dKaca, fill='pink')))
            elif self.smer == 1:
                self.seznamGlavaRep.insert(1, (self.canvas.create_oval(self.xKaca - self.dKaca,
                                                                       self.yKaca - self.dKaca + 15,
                                                                       self.xKaca + self.dKaca,
                                                                       self.yKaca + self.dKaca + 15, fill='pink')))
            elif self.smer == 2:
                self.seznamGlavaRep.insert(1, (self.canvas.create_oval(self.xKaca - self.dKaca + 15,
                                                                       self.yKaca - self.dKaca,
                                                                       self.xKaca + self.dKaca + 15,
                                                                       self.yKaca + self.dKaca, fill='pink')))
            elif self.smer == 3:
                self.seznamGlavaRep.insert(1, (self.canvas.create_oval(self.xKaca - self.dKaca,
                                                                       self.yKaca - self.dKaca - 15,
                                                                       self.xKaca + self.dKaca,
                                                                       self.yKaca + self.dKaca - 15, fill='pink')))
            self.podaljsaj = False




        # preverjamo ali je koordinata v seznamu, širši rang je zaradi lažjega ujemanja
        # ko kača poje krogec
        for x in seznamXkaca:
            for y in seznamYkaca:
                if x in seznamXkrogca and y in seznamYkrogca:
                    self.pojejBonboncek()

        self.canvas.after(100, self.premik)
        self.preveriRob()

    




root = Tk()

aplikacija = Kaca(root)

root.mainloop()
