from CRUD_F import print_info

print("Crud")
#sukuriame 3 aktoriu

aktoriai= [
    {"id":1,"name": "Leonardo", "surname": "Dicaprio"},
    {"id":2, "name": "Meg", "surname": "Ryan"},
    {"id":3, "name": "Jamie", "surname": "Foxxas"}
]
id_counter =3
while True:
    print("rinkis 1. print, 2. add, 3. edit, 4. delete, 5 exit")
    # print_info()
    opt = input()
    match opt:
        case '1':
            print("Rodyti")
            for aktorius in aktoriai:
                print(f"ID: {aktorius['id']}), Vardas: {aktorius["name"]}:Pavarde: {aktorius['surname']}")
        case '2':
            print("prideti nauja aktoriu")

            vardas = input("autoriaus vardas: ")
            pavarde = input("aktoriaus pavarde: ")
            id_counter += 1
            naujas = {"id": id_counter, "name": vardas,"surname": pavarde}
            aktoriai.append(naujas)
            print(f"prideti aktoriu: {vardas} {pavarde} (ID: {id_counter})")


        case '3':
            print("redaguoti")
        case '4':
            print("trinti")
        case '5':
            print('iseiti is programos')
            break

from CRUD import *
# aktoriai = load_default_data()
# id_counter = 3
#
# while True:
#     print_info()
#     choise = input()
# match choise:
#     case '1':
#      Aktoriu_sarasas(aktoriai)
#     case '2':
#           id_counter += 1
#           aktoriai.append(create_aktoriai(id_counter))
#     case '3':
#           edit_aktoriai(id_counter, aktoriai)









