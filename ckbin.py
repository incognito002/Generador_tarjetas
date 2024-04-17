import re

def validar_bin(bin):
    # Definir patrones de BIN para diferentes esquemas de tarjetas
    patrones = {
        "Visa": "^4[0-9]{12}(?:[0-9]{3})?$",
        "Mastercard": "^5[1-5][0-9]{14}$",
        "American Express": "^3[47][0-9]{13}$",
        # Agrega más patrones según sea necesario
    }

    # Iterar sobre los patrones y verificar si el BIN coincide con alguno de ellos
    for esquema, patron in patrones.items():
        if re.match(patron, bin):
            return True, esquema
    
    return False, None

def main():
    # Código principal para solicitar el BIN y validar
    print("+------------------------------------------------------------+")
    print("|         ||||| Bienvenido al Validador de BIN |||||         |")
    print("+------------------------------------------------------------+")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == "ck4" and contraseña == "ck4":
        bin = input("Ingrese el BIN a validar: ")
        valido, esquema = validar_bin(bin)
        if valido:
            print("El BIN es válido y pertenece al esquema:", esquema)
        else:
            print("El BIN no es válido.")
    else:
        print("Credenciales incorrectas. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
