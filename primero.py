def name_user(user):

    if (len(user) < 6):
        print("El nombre de usuario debe contener al menos 6 caracteres")
    elif (len(user) > 12):
        print("El nombre de usuario no debe contener al menos 12 caracteres")
    elif (not user.isalnum()):
        print("El nombre de usuario puede contener solo letras y números")
    else:
        return True

    return False

if (__name__ == "__main__"):

    user = input("Introduzca un nombre de usuario: ")

    if (name_user(user)):
        print("Nombre de usuario correcto")