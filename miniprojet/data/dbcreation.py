import mysql.connector


#connection au base donnée mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="anasaar123",
    database="miniprjtdb"

)
#mycursor = db.cursor()
#Creation du DATABASE "miniprjt"
#mycursor.execute(""" CREATE DATABASE miniprjtdb""")
#Creation des tables( filiere, etudiant et admins)
#mycursor.execute(""" CREATE TABLE filiere ( idfiliere int PRIMARY KEY AUTO_INCREMENT , namefiliere VARCHAR(50))""")
#mycursor.execute("""DROP TABLE admins""")
#mycursor.execute(""" CREATE TABLE etudiant ( idetud int PRIMARY KEY AUTO_INCREMENT , nometud VARCHAR(50), prenom VARCHAR(50), age int,  filiereid int , FOREIGN KEY(filiereid) REFERENCES filiere(idfiliere))""")
#mycursor.execute(" CREATE TABLE admins( ID int PRIMARY KEY , passwrd varchar(255), nomadmin varchar(50), prenomadmin varchar(50))")
#Creation d'un admine pour le login
#mycursor.execute(""" INSERT INTO admins (ID, passwrd, nomadmin, prenomadmin) VALUES( '111', 'aaa', 'Hannad', 'Yaacoub')""")
#mycursor.execute(""" INSERT INTO admins (ID, passwrd, nomadmin, prenomadmin) VALUES( '112', 'ana', 'Aaraba', 'Anass')""")
#insertion des filiere de l' INSEA
#mycursor.execute(""" INSERT INTO filiere (idfiliere, namefiliere) VALUES (NULL , 'Data & Software Engineering (DSE )'),(NULL, 'Data Science'),(NULL , 'Actuariat- Finance'),(NULL, 'Recherche Opérationnelle et Aide à la Décision'),(NULL, 'Statistique - Economie appliquée'),(NULL, 'Statistique - Démographie')""")
#insertion des etudiants
#mycursor.execute(""" INSERT INTO etudiant (idetud, nometud, prenom, age, filiereid ) VALUES (NULL, 'Aaraba', 'Anass', '21', '1'),(NULL, 'kkkk', 'uuuu', '19', '2'),(NULL, 'mmmmm', 'ssss', '27', '3'),(NULL, 'ffff', 'rrrr', '27', '4'),(NULL, 'tttt', 'eeee', '24', '5'),(NULL, 'xxxx', 'aaaa', '20', '6')""")
#db.commit()


