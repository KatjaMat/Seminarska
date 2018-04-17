from  tkinter import *
from math import *
from time import *
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
        self.stevec = 0
        self.stanje = ''


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

        #stevec
        self.canvas.create_text((655, 53), text=str(self.stevec), font=(16), tag='stevec')
        self.canvas.create_text((354, 100), text='ZAČNI IGRO S PRITISKOM NA GUMB START.',
                                font=(500), tag='dober')


        self.premik()   # NA KONCU

        menu = Menu(root)
        root.config(menu = menu)


    def narisiKaca(self, xKaca, yKaca):
        '''narise kaco na zacetku igre'''
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



        #print(self.IDkaca)
        #print(self.seznamGlavaRep)
        #print(self.IDkrogec)

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
        '''ce je gumb pritisnjen, se kaca zacne premikati'''
        self.pritisnjen = True
        self.canvas.delete(self.gumbStart_window) #skrije gumb
        if self.stanje == 'slab':
            self.canvas.delete('slab')
        else:
            self.canvas.delete('dober')


    def preveriRob(self): #konec igre
        if self.xKaca == 3 or self.xKaca == 708 or self.yKaca == 3 or self.yKaca == 708:
            self.stanje = 'slab'
            self.reset()


    def reset(self):
        '''klicemo jo 2krat, ce se zaletimo v rob ali sam vase'''
        self.xKaca = 153
        self.yKaca = 153
        for el in self.seznamGlavaRep:
            self.canvas.delete(el)
        self.seznamGlavaRep = []
        self.narisiKaca(self.xKaca, self.yKaca)
        self.smer = 0


        if self.stanje == 'slab':
            self.canvas.create_text((354,100), text = 'ZELO SI BIL SLAB. DOSEGEL SI: '+ str(self.stevec)+ ' TOČK', font = (500), tag = 'slab')
        elif self.stanje == 'dober':
            self.canvas.create_text((354, 100), text='NAJ TI BO. ZMAGAL SI IGRO S ' + str(self.stevec) + ' TOČKAMI',
                                    font=(500), tag='dober')


        self.pritisnjen = False
        self.gumbStart_window = self.canvas.create_window(350, 350, window=self.gumbStart)
        self.stevec = 0
        self.canvas.delete('stevec')
        self.canvas.create_text((655, 53), text=str(self.stevec), font=(16), tag='stevec')



    def pojejBonboncek(self):        
        self.canvas.delete(self.IDkrogec)
        self.narisiKrogec()
        self.podaljsaj = True
        self.canvas.delete('stevec')
        self.canvas.create_text((655, 53), text=str(self.stevec), font=(16), tag = 'stevec')

        
    # kačo in krogec definiramo z seznamom koordinat

    #def rastiKacaRep(self):

    def preveriZaletiSeNekam(self):
        '''preveri, ce se je kaca zaletela sama vase'''
        stej = 0
        preveri = self.canvas.coords(self.IDkaca) #preverjamo ce bodo koordinate glave kdaj iste kot koordinate drugega dela telesa, to bi pomenilo, da smo se zaleteli
        for el in self.seznamGlavaRep:
            if preveri == self.canvas.coords(el):
                stej +=1
        if stej >= 2:
            self.stanje = 'slab'
            self.reset()




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

        d = sqrt((self.xKrogec-self.xKaca)**2+(self.yKrogec-self.yKaca)**2)
        if d <= 12:
            self.stevec += 1
            self.pojejBonboncek()
        if self.stevec == 25:
            self.stanje = 'dober'
            self.reset()



        self.canvas.after(100, self.premik)
        self.preveriRob()
        self.preveriZaletiSeNekam()
        

    




root = Tk()

aplikacija = Kaca(root)

root.title('Boriz - The Snake')

root.mainloop()
