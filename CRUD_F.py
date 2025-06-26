def print_info():
     print("1 - Rodyti")
     print("2 - prideti nauja")
     print("3 - atnaujinti aktoriu")
def aktoriu_sarasas(sarasas):
    for aktorius in sarasas:
        print(f"ID: {aktorius['id']}, Vardas:{aktorius['name']}, Pavarde:{aktorius['surname']}")


