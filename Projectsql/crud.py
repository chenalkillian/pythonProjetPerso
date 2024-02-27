import  mysql.connector
from datetime import datetime


from mysql.connector import  Error

def connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='informatique'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"erreur{e}")
        return None




def create_langage(nom, date, level):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO language (nom,datecreation,levels) VALUES (%s,%s,%s)"
            cursor.execute(query, (nom,date,level))
            conn.commit()
            print(f"User '{nom} added successfully")
        except Error as e:
            print((f"Erreur lors de l'ajout de l'utilisateur: {e}"))
        finally:
            cursor.close()
            conn.close()


def create_message(nom):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO message (historique) VALUES (%s)"
            cursor.execute(query, (nom,))
            conn.commit()
            print(f"le message à été ajoouter")
        except Error as e:
            print((f"Erreur lors de l'ajout de l'utilisateur: {e}"))
        finally:
            cursor.close()
            conn.close()

def delete_user(language_id):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM language WHERE id = %s"
            cursor.execute(query, (language_id,))
            conn.commit()
            print(f"User ID'{language_id} has been deleted")
        except Error as e:
            print((f"Erreur lors de la suppresion de l'utilisateur: {e}"))
        finally:
            cursor.close()
            conn.close()



def update_user(language_id,name,date_creation,level):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            if name != None and date_creation != None and level != None:
                query = "UPDATE language SET nom = %s, datecreation = %s, levels = %s WHERE id = %s"
                cursor.execute(query, (name, date_creation,level,language_id,))
                conn.commit()
                print(f"User ID'{language_id} has been updated to '{name}'.")
            elif name != None and date_creation != None and level == None:
                query = "UPDATE language SET nom = %s, date_creation = %s WHERE id = %s"
                cursor.execute(query, (name, date_creation,language_id,))
                conn.commit()
                print(f"User ID'{language_id} has been updated to '{name}'.")
            elif name != None and date_creation == None and level == None:
                query = "UPDATE language SET nom = %s WHERE id = %s"
                cursor.execute(query, (name, language_id,))
                conn.commit()
                print(f"User ID'{language_id} has been updated to '{name}'.")
        except Error as e:
            print((f"Erreur lors de la mise Ã  jour de l'utilisateur: {e}"))
        finally:
            cursor.close()
            conn.close()





def reade_user():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute( "SELECT nom FROM user")
            return cursor.fetchall()

        except Error as e:
            print((f"Erreur lors de la lecture de l'utilisateur: {e}"))
        finally:
            cursor.close()
            conn.close()


def all_languages():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nom,datecreation FROM language   ")
            return cursor.fetchall()  # Fetch all rows from the cursor
        except Error as e:
            print(f"Erreur lors de la lecture des utilisateurs: {e}")
            return None
        finally:
            conn.close()  # Close the connection when done with it






def verificator_user(name):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT nom FROM user WHERE nom = %s"
            cursor.execute(query, (name,))

            # Utilisez fetchone() pour récupérer une seule ligne
            user = cursor.fetchone()

            if user:
                return user
            else:
                return None

        except Error as e:
            print(f"Erreur lors de la mise à jour de l'utilisateur: {e}")
        finally:
            cursor.close()
            conn.close()








def main_menu(name):

    result = verificator_user(name)

    if result:
        print("Utilisateur trouvé:", result)
        print("Faite votre choix")
        print("[1] Ajouter un langage")
        print("[2] Modifier un langage")
        print("[3] Supprimer un langage")
        print("[4] liste tous les langage")
        print("[5] exit")

        return input("faites votre choix")
    else:
        print("Utilisateur non trouvé.")
        exit()




programme = True

while(programme):
    print("Bienvenue dans votre crud de langage")
    nom = input("entrer votre prénom\n")
    choice = main_menu(nom)
    print(choice)
    choice = int(choice)
    if choice == 1:
       name=input("nom de langage")
       date=input("Date ")
       level=input("level")

       create_langage(nom,date,level)
       create_message(f"l'utilisateur {nom} a ajouté {name} le {str(datetime.now())}")

    elif choice == 2:
        id = input("id du langage")
        name = input("nom de langage")
        date = input("Date ")
        level = input("level")

        update_user(id,name, date, level)
        create_message(f"l'utilsateur: {nom} a modifier {name} le {str(datetime.now())}")

    elif choice == 3:
        id = input("id du langage")


        delete_user(id)
        create_message(f"l'utilsateur: {nom} a supprimer l'id : {id} le {str(datetime.now())}")

    elif choice == 4:
        data = all_languages()
        if data is not None:
            for (nom, date_creation) in data:
                print(f"nom: {nom}, date_creation: {str(datetime.now())}")
        else:
            print("Aucune donnée disponible.")

    elif choice == 5:
        programme=False
    else:
        pass


