import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='killian',
        password='killian2901',
        database='kikiflix'
    )

except mysql.connector.Error as e:
    print("erreur lors de la connexion à Mysql", e)
finally:
    pass






programme = True

while(programme):
    choice = main_menu()
    print(choice)
    choice = int(choice)
    if choice == 1:
       name=input("nom de langage")
       date=input("Date ")
       level=input("level")

       create_langage(name,date,level)

    elif choice == 2:
        id = input("id du langage")
        name = input("nom de langage")
        date = input("Date ")
        level = input("level")

        update_user(id,name, date, level)
    elif choice == 3:
        id = input("id du langage")


        delete_user(id)

    else:
        pass

