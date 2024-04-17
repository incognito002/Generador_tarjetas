import random
import time
import os
import binlist
from colorama import init, Fore, Style

def solicitar_credenciales(intentos):
    for intento in range(intentos):
        # Solicitar las credenciales al usuario
        print(Fore.YELLOW + "+" + "-" * 60 + "+")
        print("|" + Fore.MAGENTA + "||||| Bienvenido al Validador de BIN |||||".center(60) + Fore.YELLOW + "|")
        print("+" + "-" * 60 + "+" + Style.RESET_ALL)
        usuario = input(Fore.CYAN + "Usuario: " + Style.RESET_ALL)
        contraseña = input(Fore.CYAN + "Contraseña: " + Style.RESET_ALL)
        if verificar_credenciales(usuario, contraseña):
            return usuario
        else:
            print(Fore.RED + "Credenciales incorrectas. Intento {} de {}".format(intento + 1, intentos) + Style.RESET_ALL)
    return None

def verificar_credenciales(usuario, contraseña):
    # Verificar si las credenciales son correctas
    return usuario == "ck4" and contraseña == "ck4"

def limpiar_terminal():
    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

def personalizar_terminal():
    # Mostrar el nombre de la herramienta en un cuadro grande
    print(Fore.YELLOW + "+" + "-" * 60 + "+")
    print("|" + Fore.MAGENTA + "Validador de BIN".center(60) + Fore.YELLOW + "|")
    print("+" + "-" * 60 + "+" + Style.RESET_ALL)
    print()

    # Animación de bienvenida con borde de colores
    mensaje_bienvenida = [
        "=== Validador de BIN ===",
        "Bienvenido al Validador de BIN",
        "Por favor, ingrese sus credenciales a continuación:"
    ]
    color_borde = Fore.YELLOW
    color_texto = Fore.MAGENTA
    longitud_maxima = max(len(linea) for linea in mensaje_bienvenida)
    print(color_borde + "+" + "-" * (longitud_maxima + 2) + "+" + Style.RESET_ALL)
    for linea in mensaje_bienvenida:
        print(color_borde + "| " + color_texto + linea.ljust(longitud_maxima) + " " * (longitud_maxima - len(linea)) + " " + color_borde + "|" + Style.RESET_ALL)
    print(color_borde + "+" + "-" * (longitud_maxima + 2) + "+" + Style.RESET_ALL)

def validar_bin(bin):
    # Verificar si el BIN es válido utilizando la biblioteca binlist
    result = binlist.find(bin)
    if result:
        return True
    else:
        return False

def main():
    # Solicitar las credenciales con 5 intentos
    usuario = solicitar_credenciales(5)
    if usuario is None:
        print(Fore.RED + "Has excedido el número máximo de intentos. ¡Adiós!")
        return

    # Limpiar la terminal después de ingresar las credenciales correctas
    limpiar_terminal()

    # Personalizar la terminal
    personalizar_terminal()

    # Solicitar el BIN a validar
    bin = input(Fore.MAGENTA + "Ingrese el BIN a validar: ")

    # Validar el BIN ingresado
    if validar_bin(bin):
        print(Fore.GREEN + "El BIN {} es válido.".format(bin))
    else:
        print(Fore.RED + "El BIN {} es inválido.".format(bin))

if __name__ == "__main__":
    main()
