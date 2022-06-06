from tkinter import *
import tkinter as tk
import dse , ds, af, road, se, sd
import Butt

#Création du class AdminWindow pour l'accés au espace admin
class AdminWindow:

    def __init__(self):
        self.window1 = Tk()
        self.canvas = Canvas(self.window1, width=800, height=700, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        width = self.window1.winfo_screenwidth()
        height = self.window1.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.window1.geometry(str1)
        self.window1.resizable(width=False, height=False)
        self.window1.title("WELCOME ADMINE")
        self.window1.iconbitmap('insea.ico')
        self.label= tk.Label(self.window1, text="Bienvenue au espace admine", font=("Arial Bold", 15), bg='green')
        self.txt= Label(self.window1, text="Filiéres INSEA", font=('Arial Bold', 15), bg='white', fg='green')
        self.txt.place(x=220, y=30)
        self.label.pack()

        self.button1 = Button(self.window1, text="Data & Software Engineering (DSE )", font=("Arial Bold", 14), bg="green", fg="White", command=self.dse)
        self.button1.place(x=140, y=90)

        self.button2 = Button(self.window1, text="Data Science", font=("Arial Bold", 14), bg="green", fg="White", command=self.ds)
        self.button2.place(x=140, y=140)

        self.button3 = Button(self.window1, text="Actuariat- Finance", font=("Arial Bold", 14), bg="green", fg="White", command=self.af)
        self.button3.place(x=140, y=190)

        self.button4 = Button(self.window1, text="Recherche Opérationnelle et Aide à la Décision", font=("Arial Bold", 14),bg="green", fg="White", command=self.road)
        self.button4.place(x=140, y=240)

        self.button5 = Button(self.window1, text="Statistique - Economie appliquée", font=("Arial Bold", 14),bg="green", fg="White", command=self.se)
        self.button5.place(x=140, y=290)

        self.button6 = Button(self.window1, text="Statistique - Démographie", font=("Arial Bold", 14), bg="green", fg="White", command=self.sd)
        self.button6.place(x=140, y=340)

        self.button7 = Button(self.window1, text="Ajouter filiére", font=("Italic", 12), bg="white", fg="black", command=self.ajouter_fil)
        self.button7.place(x=100, y=430)

        self.button8 = Button(self.window1, text="Modifier filiére", font=("Italic", 12), bg="white",fg="black", command=self.modifier_fil)
        self.button8.place(x=220, y=430)

        self.button9 = Button(self.window1, text="Supprimer filiére", font=("Italic", 12), bg="white",fg="black", command=self.supp_fil)
        self.button9.place(x=360, y=430)
        self.window1.mainloop()

    def dse(self):
        self.window1.destroy()
        return dse.dseWindow()
    def ds(self):
        self.window1.destroy()
        return ds.dsWindow()
    def af(self):
        self.window1.destroy()
        return af.afWindow()
    def road(self):
        self.window1.destroy()
        return road.roadWindow()
    def se(self):
        self.window1.destroy()
        return se.seWindow()
    def sd(self):
        self.window1.destroy()
        return sd.sdWindow()

    def ajouter_fil(self):
        self.window1.destroy()
        return Butt.ajouterWindow()

    def modifier_fil(self):
        self.window1.destroy()
        return Butt.modifierWindow()

    def supp_fil(self):
        self.window1.destroy()
        return Butt.suppWindow()






if __name__=="__main__":
    x= AdminWindow()
