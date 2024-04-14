import random
from colorama import init, Fore, Style

def generar_bin(tipo_tarjeta):
    # Generar un BIN de 6 dígitos
    bin = ''.join(random.choices('0123456789', k=6))
    
    # Determinar el tipo de tarjeta
    if tipo_tarjeta == 1:
        tipo = "Visa"
    elif tipo_tarjeta == 2:
        tipo = "Mastercard"
    elif tipo_tarjeta == 3:
        tipo = "American Express"
    else:
        tipo = "Otro"
    
    # Devolver el BIN generado y el tipo de tarjeta
    return bin, tipo

def main():
    init()  # Inicializar colorama
    print(Fore.YELLOW + "+" + "-" * 60 + "+")
    print("|" + Fore.MAGENTA + "||||| Generador de BINs |||||".center(60) + Fore.YELLOW + "|")
    print("+" + "-" * 60 + "+" + Style.RESET_ALL)
    print()
    
    print(Fore.MAGENTA + "Seleccione el tipo de tarjeta que desea generar:")
    print("1. Visa")
    print("2. Mastercard")
    print("3. American Express")
    print("4. Otro" + Style.RESET_ALL)
    
    opcion = int(input(Fore.CYAN + "Opción: " + Style.RESET_ALL))
    
    if opcion < 1 or opcion > 4:
        print(Fore.RED + "Opción no válida. Saliendo del programa." + Style.RESET_ALL)
        return
    
    bin, tipo = generar_bin(opcion)
    
    print(Fore.GREEN + "\nBIN generado con éxito:" + Style.RESET_ALL)
    print("BIN:", bin)
    print("Tipo de tarjeta:", tipo)

if __name__ == "__main__":
    main()
