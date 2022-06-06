from tkinter import *
import mysql.connector
import Buttonetudiant
import Admin





db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="anasaar123",
    database="Miniprjtdb"

)

#class roadWindow pour la gestion de la filiere Recherche Opérationnelle et Aide à la Décision
class roadWindow:

    def __init__(self):
        self.window2= Tk()
        self.canvas = Canvas(self.window2, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        width = self.window2.winfo_screenwidth()
        height = self.window2.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)

        self.window2.geometry(str1)
        self.window2.resizable(width=False, height=False)
        self.window2.title("Recherche Opérationnelle et Aide à la Décision")
        self.window2.iconbitmap('insea.ico')
        self.txt = Label(self.window2, text="Filiére Recherche Opérationnelle et Aide à la Décision(ROAD) :", font=('Arial Bold', 13),bg='green', fg='white')
        self.txt.place(x=100, y=60)
        self.txt = Label(self.window2, text="ID :", font=('Italic', 8),bg='green', fg='white')
        self.txt.place(x=100, y=130)
        self.txt = Label(self.window2, text="Nom :", font=('Italic', 8),bg='green', fg='white')
        self.txt.place(x=160, y=130)
        self.txt = Label(self.window2, text="Prenom :", font=('Italic', 8),bg='green', fg='white')
        self.txt.place(x=230, y=130)
        self.txt = Label(self.window2, text="Age :", font=('Italic', 8),bg='green', fg='white')
        self.txt.place(x=320, y=130)
        self.list= Listbox(self.window2)
        self.list.place(x=100, y=150 , width=300)
        self.show()

        self.button1 = Button(self.window2, text="Ajouter étudiant", font=('Italic', 10),command=self.ajouter)
        self.button1.place(x=80, y=350, width=120)

        self.button2 = Button(self.window2, text="Modifier étudiant", font=('Italic', 10), command=self.modifier)
        self.button2.place(x=200, y=350, width=120)

        self.button3 = Button(self.window2, text="Supprimer étudiant", font=('Italic', 10), command=self.supprimer)
        self.button3.place(x=320, y=350, width=120)

        self.window2.mainloop()

    def show(self):
        mycursor = db.cursor()
        mycursor.execute(""" SELECT * FROM etudiant WHERE filiereid= 4""")
        result = mycursor.fetchall()
        for i in result:
            insertData = str(i[0])+'                  '+str(i[1])+'               '+str(i[2])+'                   '+str(i[3])
            self.list.insert(self.list.size()+1, insertData)

    def ajouter(self):
        self.window2.destroy()
        return Buttonetudiant.ajouteretudWindow()
    def modifier(self):
        self.window2.destroy()
        return Buttonetudiant.modifieretudWindow()
    def supprimer(self):
        self.window2.destroy()
        return Buttonetudiant.suppetudWindow()



if __name__=="__main__":
    x= roadWindow()
    Admin.AdminWindow()