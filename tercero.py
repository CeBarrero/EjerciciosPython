from primero import *
from segundo import *

user = input("Introduzca un nombre de usuario:")
password = input("Introduzca una contraseña valida:")

if (not name_user(user) or not  password_vali(password)):
    print("El nombre de usuario o la contraseña no son validas")
else:
    print("Usuario y contraseña son validos")
