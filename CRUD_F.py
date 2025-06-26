def load_default_data ():
    return[
        {"id":1,"name": "Leonardo", "surname": "Dicaprio"},
        {"id":2, "name": "Meg", "surname": "Ryan"},
        {"id":3, "name": "Jamie", "surname": "Foxxas"}
    ]
def print_info():
     print("Pasirinkite:")
     print("1- rodyti visus aktorius")
     print("2 - prideti nauja aktoriu")
     print("3 - redaguoti aktoriu")
     print("4 - istrinti aktoriu")
     print("5 - iseiti")
def rodyti_aktorius(aktoriai):
    for aktorius in aktoriai:
        print(f"ID: {aktorius['id']}, Vardas:{aktorius['name']}, Pavarde:{aktorius['surname']}")
def add_actor(actors,id_counter):
    name=input("Name: ")
    surname=input("Surname: ")
    id_counter+=1
    new_actor = {"id":id_counter,"name":name,"surname":surname}
    actors.append(new_actor)
    print("")
    return id_counter
def edit_actor(actors):
    id_edit = int(input("ID: "))
    for actor in actors:
        if actor['id'] == id_edit:
            actor["name"] = input("Name: ")
            actor["surname"] = input("Surname: ")
            print("")
def delete_actor(actors):
    id_delete = int(input("ID: "))
    for actor in actors:
        if actor['id'] == id_delete:
            actors.remove(actor)
            print(" ")



