from tkinter import *
import tkinter as tk
from tkinter import messagebox
import Admin
import mysql.connector

#Connection au base de données mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="anasaar123",
    database="miniprjtdb"

)

#création de classe login pour l'authentification d'admin

class login:

    def __init__(self):
        self.window= Tk()

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+" + str(x) + "+" + str(y)
        self.window.geometry(str1)
        self.window.resizable(width=False, height=False)

        self.window.title("Mini projet Aaraba")
        self.window.iconbitmap('insea.ico')
        self.label = tk.Label(self.window, text="Bienvenue au gestion des filiéres et étudiants INSEA", font=("Arial Bold", 15),
                         fg="Green")
        self.txt = Label(self.window, text="Espace Admins :", font=('Arial Bold', 12))
        self.txt.place(x=250, y=60)
        self.label.pack()

        self.id = Label(self.window, text="*Id :", font=('bold', 10))
        self.id.place(x=150, y=100)

        self.passwrd = Label(self.window, text="*Password :", font=('bold', 10))
        self.passwrd.place(x=150, y=130)

        self.id = Entry()
        self.id.place(x=250, y=100)

        self.passwrd = Entry(show="*" )
        self.passwrd.place(x=250, y=130)

        self.button= Button(self.window, text="Login", font=("Italic", 12 ), bg="green" , fg="White" ,command=self.login)
        self.button.place(x=270, y=160)

        self.window.mainloop()

    def login(self):
        id=self.id.get()
        passwd=self.passwrd.get()
        info=[]
        info.append(id)
        info.append(passwd)

        if info[0] == "":
            messagebox.showinfo("Alert!", "Entrer votre id")
        elif info[1] == "":
            messagebox.showinfo("Alert!", "Entrer votre password")
        else:
            mycursor=db.cursor()
            mycursor.execute(""" SELECT ID , passwrd FROM admins WHERE ID= %s AND passwrd= %s """, info)
            result=mycursor.fetchall()
            for i in result:
                print(i)
                self.window.destroy()
                return Admin.AdminWindow()
            messagebox.showinfo("ALert!", "Wrong id/password")




if __name__=="__main__":
    x = login()

