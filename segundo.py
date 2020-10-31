def password_vali(passw):

    long = False
    mayus = False
    minus = False
    nums = False
    especial = False
    espacio = False

    if (len(passw) >= 8):
        long = True

        for letra in passw:
            if (letra.isupper()):
                mayus = True
            elif (letra.islower()):
                minus = True
            elif (letra.isdigit()):
                nums = True
            elif (not letra.isalnum()):
                especial = True
            elif (not letra.isspace()):
                espacio = True

    if (long and mayus and minus and nums and especial and espacio):
        return True
    else:
        return False

if (__name__ == "__main__"):

    passw = input("Introduzca una contraseña: ")

    if (password_vali(passw)):
        print("Contraseña segura")
    else:
        print("La contraseña elegida no es segura")