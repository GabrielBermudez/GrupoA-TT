nomUsuario1 = "Leandro"
contra = "contraseña1205"
condicion = True

correo = input("Ingrese su correo electrónico: ")
while (condicion):
    if (("@" in correo) == False or (".com" in correo) == False or correo.islower() == False):
        correo = input("Error, ingrese un correo electrónico válido: ")

    elif ("," in correo or "*" in correo or "/" in correo or "}" in correo or "(" in correo or ")" in correo):
        correo = input("Error, ingrese un correo electrónico válido: ")

    elif ("{" in correo or "|" in correo or "!" in correo or "[" in correo or "=" in correo or " " in correo):
        correo = input("Error, ingrese un correo electrónico válido: ")

    elif ("]" in correo or "#" in correo or "$" in correo or "%" in correo or "&" in correo or "|" in correo):
        correo = input("Error, ingrese un correo electrónico válido: ")

    elif ("¿" in correo or "?" in correo or "'" in correo or ";" in correo or "<" in correo or ">" in correo):
        correo = input("Error, ingrese un correo electrónico válido: ")

    elif ("'" in correo or "+" in correo or "¡" in correo or ":" in correo):
        correo = input("Error, ingrese un correo electrónico válido: ")
    
    else:
        condicion = False
condicion = True    

nomUsuario = input("Ingrese su nombre de usuario: ")
while(condicion):
    if (nomUsuario != nomUsuario1):
        print("Error, el nombre de usuario ingresado no es válido")
        nomUsuario = input("Ingrese su nombre de usuario: ")
    else:
        condicion = False
condicion = True


password = input("Ingrese su contraseña: ")
while(condicion):
    if (password != contra):
        print("Error, la contraseña ingresada no es válida")
        password = input("Ingrese su contraseña nuevamente: ")
    else:
        condicion = False
condicion = True