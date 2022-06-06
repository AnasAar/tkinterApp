from tkinter import *
from tkinter import messagebox
import mysql.connector
import Admin





db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="anasaar123",
    database="miniprjtdb"

)
#création des classes nécessaires pour la gestion des filiéres


class ajouterWindow:

    def __init__(self):
        self.window8 = Tk()
        self.canvas = Canvas(self.window8, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        width = self.window8.winfo_screenwidth()
        height = self.window8.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.window8.geometry(str1)
        self.window8.resizable(width=False, height=False)
        self.window8.title("Ajouter une filiére")
        self.window8.iconbitmap('insea.ico')
        self.ajt = Label(self.window8, text="Entrer le nom de filiere", font=('Arial Bold', 20), bg='green', fg='white')
        self.ajt.place(x=150, y=30)

        self.ajt = Entry()
        self.ajt.place(x=50, y=130, width=500, height=40)

        self.button = Button(self.window8, text="enregistrer la filiére", font=('Arial Bold', 15), command=self.enregistrer)
        self.button.place(x=150, y=250)


        self.window8.mainloop()

    def enregistrer(self):
        ajt=self.ajt.get()
        L=[]
        L.append(ajt)
        if L[0] == "":
            messagebox.showinfo("Alert!", "Entrer une filiére valide")
        else:
            mycursor=db.cursor()
            mycursor.execute(""" SELECT idfiliere FROM filiere WHERE namefiliere= %s """, L)
            result=mycursor.fetchall()
            for i in result:
                print(i)
                return messagebox.showinfo("Echec!", "Cette filiére existe déja, veuillez vérifier vos données!")
            mycursor=db.cursor()
            mycursor.execute(""" INSERT INTO filiere (idfiliere, namefiliere) VALUES(NULL, (%s)) """, L)
            db.commit()
            messagebox.showinfo("Succés!", "d'enregistrement du filiére")
            self.window8.destroy()
            return Admin.AdminWindow()

if __name__ == "__main__":
    x = ajouterWindow()



class modifierWindow:

    def __init__(self):
        self.window9 = Tk()
        self.canvas = Canvas(self.window9, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        width = self.window9.winfo_screenwidth()
        height = self.window9.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.window9.geometry(str1)
        self.window9.resizable(width=False, height=False)
        self.window9.title("Modifier une filiére")
        self.window9.iconbitmap('insea.ico')
        self.anc = Label(self.window9, text="Entrer l'ancienne nom du filiére", font=('Arial Bold', 15), bg='green', fg='white')
        self.anc.place(x=150, y=30)
        self.mdf = Label(self.window9, text="Entrer le nouveau nom du filiére", font=('Arial Bold', 15), bg='green', fg='white')
        self.mdf.place(x=150, y=200)
        self.anc = Entry()
        self.anc.place(x=50, y=100, width=500, height=30)
        self.mdf = Entry()
        self.mdf.place(x=50, y=270, width=500, height=30)


        self.button = Button(self.window9, text="Modifier la filiére", font=('Arial Bold', 15), command=self.modiff)
        self.button.place(x=150, y=350)


        self.window9.mainloop()

    def modiff(self):
        ajt=self.mdf.get()
        anc=self.anc.get()
        L=[]
        T=[]
        T.append(anc)
        L.append(ajt)
        L.append(anc)
        if L[0] == "":
            messagebox.showinfo("Alert!", "Entrer une filiére valide")
        else:
            mycursor=db.cursor()
            mycursor.execute(""" SELECT idfiliere FROM filiere WHERE namefiliere= %s """, T)
            result=mycursor.fetchall()
            for i in result:
                print(i)
                mycursor=db.cursor()
                mycursor.execute(""" UPDATE filiere SET namefiliere= %s  WHERE namefiliere= %s """, L)
                db.commit()
                messagebox.showinfo("Succés!", "la filiére a été modifier")
                self.window9.destroy()
                return Admin.AdminWindow()
            return messagebox.showinfo("Echec!", "Cette filiére n'existe pas, veuillez vérifier vos données!")

if __name__ == "__main__":
    x = modifierWindow()

class suppWindow:

    def __init__(self):
        self.window10 = Tk()
        self.canvas = Canvas(self.window10, width=600, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        width = self.window10.winfo_screenwidth()
        height = self.window10.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 500 / 2)
        str1 = "600x500+" + str(x) + "+" + str(y)
        self.window10.geometry(str1)
        self.window10.resizable(width=False, height=False)
        self.window10.title("Ajouter une filiére")
        self.window10.iconbitmap('insea.ico')
        self.supp = Label(self.window10, text="Entrer le nom du filiere", font=('Arial Bold', 20), bg='green', fg='white')
        self.supp.place(x=150, y=30)

        self.supp = Entry()
        self.supp.place(x=50, y=140, width=500, height=50)

        self.button = Button(self.window10, text="Supprimer la filiére mentionner", font=('Arial Bold', 15), command=self.confirmer)
        self.button.place(x=150, y=300)


        self.window10.mainloop()

    def confirmer(self):
        messagebox.showinfo("Alert!", "Vous voulez vraiment supprimer cette filiére de l'école")
        self.button = Button(self.window10, text="confirmation de la suppréssion du filiére mentionner", font=('Arial Bold', 15), command=self.supprimer)
        self.button.place(x=70, y=400)


    def supprimer(self):
        supp=self.supp.get()
        L=[]
        L.append(supp)
        if L[0] == "":
            messagebox.showinfo("Alert!", "Entrer une filiére valide")
        else:
            mycursor=db.cursor()
            mycursor.execute(""" SELECT idfiliere FROM filiere WHERE namefiliere= %s """, L)
            result=mycursor.fetchall()
            for i in result:
                print(i)
                mycursor = db.cursor()
                mycursor.execute(""" DELETE FROM filiere  WHERE namefiliere= %s """, L)
                db.commit()
                messagebox.showinfo("Succés!", "la filiére a été supprimer")
                self.window10.destroy()
                return Admin.AdminWindow()
            return messagebox.showinfo("Echec!", "Cette filiére n'existe pas, veuillez vérifier vos données!")

if __name__ == "__main__":
    x = suppWindow()
