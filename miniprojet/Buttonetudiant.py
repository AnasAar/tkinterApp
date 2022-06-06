from tkinter import *
from tkinter import messagebox
import mysql.connector
import Accueilpage




db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="anasaar123",
    database="miniprjtdb"

)

#création des classes nécessaires pour la gestion des étudiants

class ajouteretudWindow:

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
        self.window8.title("Ajouter un(e) étudiant(e)")
        self.window8.iconbitmap('insea.ico')
        self.ajtn = Label(self.window8, text="Entrer le nom de l'étudiant", font=('Italic', 10), bg='green', fg='white')
        self.ajtn.place(x=150, y=30)
        self.ajtp = Label(self.window8, text="Entrer le prénom de l'étudiant", font=('Italic', 10), bg='green',fg='white')
        self.ajtp.place(x=150, y=130)
        self.ajta = Label(self.window8, text="Entrer l'âge de l'étudiant", font=('Italic', 10), bg='green',fg='white')
        self.ajta.place(x=150, y=230)
        self.ajtf = Label(self.window8, text="Entrer le nom de filiére d'étudiant", font=('Italic', 10), bg='green', fg='white')
        self.ajtf.place(x=150, y=330)

        self.ajtn = Entry()
        self.ajtn.place(x=50, y=80, width=500, height=40)
        self.ajtp = Entry()
        self.ajtp.place(x=50, y=180, width=500, height=40)
        self.ajta = Entry()
        self.ajta.place(x=50, y=280, width=500, height=40)
        self.ajtf = Entry()
        self.ajtf.place(x=50, y=380, width=500, height=40)

        self.button = Button(self.window8, text="enregistrer l'étudiant", font=('Arial Bold', 15), command=self.enregistrer)
        self.button.place(x=150, y=420)


        self.window8.mainloop()

    def enregistrer(self):
        ajtn=self.ajtn.get()
        ajtp = self.ajtp.get()
        ajta = self.ajta.get()
        ajtf = self.ajtf.get()
        L=[]
        T=[]
        F=[]
        T.append(ajtn)
        T.append(ajtp)
        T.append(ajta)
        L.append(ajtn)
        L.append(ajtp)
        L.append(ajta)
        F.append(ajtf)

        if L[0]== "" or L[1]== "" or L[2]== "" or F[0] == "":
            messagebox.showinfo("Alert!", "Entrer les données complétent de l'étudiant")
        else:
            mycon = db.cursor()
            mycon.execute(""" SELECT idfiliere FROM filiere WHERE namefiliere= %s """, F)
            query = mycon.fetchall()
            for a in query:
                 L.append(a[0])
            mycon.close()
            cur=db.cursor()
            cur.execute(""" SELECT idetud FROM etudiant WHERE nometud= %s AND prenom= %s AND age= %s """, T)
            result=cur.fetchall()
            for i in result:
                print(i)
                return messagebox.showinfo("Echec!", "Ce étudiant(e) existe déja, veuillez vérifier vos données!")
            cur.close()
            mycursor=db.cursor()
            mycursor.execute(""" INSERT INTO etudiant ( idetud, nometud, prenom, age, filiereid ) VALUES(NULL, (%s), (%s), (%s), (%s)) """, L)
            db.commit()
            messagebox.showinfo("Succés!", "Succées d'enregistrement d'étudiant(e)")
        self.window8.destroy()
        return Accueilpage.login()

if __name__ == "__main__":
    x = ajouteretudWindow()



class modifieretudWindow:

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
        self.window9.title("Modifier un(e) étudiant(e)")
        self.window9.iconbitmap('insea.ico')
        self.anc = Label(self.window9, text="Entrer l'id de l'étudiant(e) ", font=('Italic', 10), bg='green', fg='white')
        self.anc.place(x=150, y=10)
        self.nvn = Label(self.window9, text="Entrer le nouveau nom de l'étudiant(e)", font=('Italic', 10), bg='green', fg='white')
        self.nvn.place(x=150, y=100)
        self.nvp = Label(self.window9, text="Entrer le nouveau prénom de l'étudiant(e)", font=('Italic', 10), bg='green', fg='white')
        self.nvp.place(x=150, y=190)
        self.nva = Label(self.window9, text="Entrer l'âge de l'étudiant(e)", font=('Italic', 10), bg='green', fg='white')
        self.nva.place(x=150, y=280)
        self.nvf = Label(self.window9, text="Entrer la nouvelle filiére d'étudiant(e)", font=('Italic', 10), bg='green',fg='white')
        self.nvf.place(x=150, y=380)

        self.anc = Entry()
        self.anc.place(x=50, y=60, width=500, height=40)
        self.nvn = Entry()
        self.nvn.place(x=50, y=150, width=500, height=40)
        self.nvp = Entry()
        self.nvp.place(x=50, y=230, width=500, height=40)
        self.nva = Entry()
        self.nva.place(x=50, y=320, width=500, height=40)
        self.nvf = Entry()
        self.nvf.place(x=50, y=420, width=500, height=40)

        self.button = Button(self.window9, text="Modifier l'étudiant(e) ", font=('Arial Bold', 10), command=self.modiff)
        self.button.place(x=150, y=470)


        self.window9.mainloop()

    def modiff(self):
        anc=self.anc.get()
        nvn=self.nvn.get()
        nvp=self.nvp.get()
        nva=self.nva.get()
        nvf=self.nvf.get()
        L=[]
        T=[]
        F=[]
        T.append(anc)
        L.append(nvn)
        L.append(nvp)
        L.append(nva)
        F.append(nvf)
        if T[0] == "" or L[0] == "" or L[1] == "" or L[2] == "" or F[0] == "" :
            messagebox.showinfo("Alert!", "Entrer un(e) étudiant valide")
        else:
            mycon=db.cursor()
            mycon.execute(""" SELECT * FROM etudiant WHERE idetud= %s """, T)
            result=mycon.fetchall()
            mycon.close()
            if result != []:
                conn = db.cursor()
                conn.execute(""" SELECT idfiliere FROM filiere WHERE namefiliere= %s """, F)
                query = conn.fetchall()
                for a in query:
                    L.append(a[0])
                    L.append(anc)
                conn.close()
                mycursor=db.cursor()
                mycursor.execute(""" UPDATE etudiant SET nometud= %s, prenom= %s, age= %s, filiereid= %s  WHERE idetud= %s """, L)
                db.commit()
                messagebox.showinfo("Succés!", "l'étudiant(e) a été modifier avec succées")
                self.window9.destroy()
                return Accueilpage.login()
            return messagebox.showinfo("Echec!", "L'étudiant(e) n'existe pas, veuillez vérifier vos données!")


if __name__ == "__main__":
    x = modifieretudWindow()

class suppetudWindow:

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
        self.window10.title("Supprimer un(e) étudiant")
        self.window10.iconbitmap('insea.ico')
        self.supp = Label(self.window10, text="Entrer le id d'étudiant(e) ", font=('Arial Bold', 20), bg='green', fg='white')
        self.supp.place(x=150, y=30)

        self.supp = Entry()
        self.supp.place(x=50, y=140, width=500, height=50)

        self.button = Button(self.window10, text="Supprimer l'étudiant(e) mentionner", font=('Arial Bold', 15), command=self.confirmer)
        self.button.place(x=150, y=300)


        self.window10.mainloop()

    def confirmer(self):
        messagebox.showinfo("Alert!", "Vous voulez vraiment supprimer l'étudiant(e) mentionner!!")
        self.button = Button(self.window10, text="confirmation de la suppréssion d'étudiant(e) mentionner", font=('Arial Bold', 15), command=self.supprimer)
        self.button.place(x=70, y=400)


    def supprimer(self):
        supp=self.supp.get()
        L=[]
        L.append(supp)
        if L[0] == "":
            messagebox.showinfo("Alert!", "Entrer un étudiant(e) valide")
        else:
            mycursor=db.cursor()
            mycursor.execute(""" SELECT * FROM etudiant WHERE idetud= %s """, L)
            result=mycursor.fetchall()
            for i in result:
                print(i)
                mycursor = db.cursor()
                mycursor.execute(""" DELETE FROM etudiant  WHERE idetud= %s """, L)
                db.commit()
                messagebox.showinfo("Succés!", "l'étudiant(e) a été supprimer")
                self.window10.destroy()
                return Accueilpage.login()
            return messagebox.showinfo("Echec!", "L'étudiant(e) n'existe pas, veuillez vérifier vos données!")

if __name__ == "__main__":
    x = suppetudWindow()
