import time
from colorama import init, Fore, Style

# Inicializar colorama
init()

def luhn_algorithm(number):
    """
    Verifica la validez de un número utilizando el algoritmo de Luhn.
    """
    num_list = [int(x) for x in str(number)]
    check_digit = num_list.pop()
    num_list.reverse()
    processed_digits = []
    for index, digit in enumerate(num_list):
        if index % 2 == 0:
            doubled_digit = digit * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            processed_digits.append(doubled_digit)
        else:
            processed_digits.append(digit)
    total = sum(processed_digits)
    return (total + check_digit) % 10 == 0

def validate_bin(bin_number):
    """
    Verifica si un número de BIN es válido.
    """
    return luhn_algorithm(bin_number)

def animacion_verificacion():
    """
    Simula una animación de verificación.
    """
    for _ in range(5):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    print(Fore.MAGENTA + "Verificador de BIN" + Style.RESET_ALL)
    bin_number = input(Fore.CYAN + "Ingrese el número de BIN: " + Style.RESET_ALL)
    print("Verificando el BIN...", end="", flush=True)
    animacion_verificacion()
    if validate_bin(bin_number):
        print(Fore.GREEN + "El número de BIN es válido." + Style.RESET_ALL)
    else:
        print(Fore.RED + "El número de BIN no es válido." + Style.RESET_ALL)
()