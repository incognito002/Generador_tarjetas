import random
import os
from colorama import Fore, Style

def solicitar_credenciales():
    # Solicitar las credenciales al usuario
    print(Fore.YELLOW + "+" + "-" * 60 + "+")
    print("|" + Fore.MAGENTA + "||||| Bienvenido al Generador de BINs |||||".center(60) + Fore.YELLOW + "|")
    print("+" + "-" * 60 + "+" + Style.RESET_ALL)
    usuario = input(Fore.CYAN + "Usuario: " + Style.RESET_ALL)
    contraseña = input(Fore.CYAN + "Contraseña: " + Style.RESET_ALL)
    return usuario, contraseña

def iniciar_sesion():
    intentos = 3
    while intentos > 0:
        usuario, contraseña = solicitar_credenciales()
        if usuario == "ck4" and contraseña == "ck4":
            print(Fore.GREEN + "Inicio de sesión exitoso." + Style.RESET_ALL)
            return True
        else:
            intentos -= 1
            print(Fore.RED + "Credenciales incorrectas. Intentos restantes:", intentos, Style.RESET_ALL)
    print(Fore.RED + "Se agotaron los intentos. Saliendo del programa." + Style.RESET_ALL)
    return False

def generate_valid_bin():
    # Generar un número aleatorio de 6 dígitos
    bin_number = ''.join(str(random.randint(0, 9)) for _ in range(5))
    
    # Completar el número generado con un dígito de verificación válido
    bin_number += calculate_check_digit(bin_number)
    
    return bin_number

def calculate_check_digit(bin_number):
    # Calcular el dígito de verificación utilizando el algoritmo de Luhn
    digits = [int(d) for d in bin_number]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit)

def limpiar_terminal():
    # Limpiar la terminal
    os.system('clear' if os.name == 'posix' else 'cls')

# Función principal
def generar_bins():
    limpiar_terminal()
    if not iniciar_sesion():
        return

    # Solicitar cantidad de BINs a generar
    cantidad = int(input(Fore.MAGENTA + "Número de BINs a generar: " + Style.RESET_ALL))
    print(Style.RESET_ALL)
    print("\nGenerando BINs:")
    
    # Generar y mostrar los BINs
    for _ in range(cantidad):
        print(generate_valid_bin())

# Ejecutar la función principal
generar_bins()
