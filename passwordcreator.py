import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_digitos=True, incluir_especiales=True):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_digitos:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    if not caracteres:
        print("Error: Debes incluir al menos un tipo de caracteres.")
        return None

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_multiples_contraseñas(cantidad, longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_digitos=True, incluir_especiales=True):
    contraseñas = [generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_digitos, incluir_especiales) for _ in range(cantidad)]
    return contraseñas

def guardar_contraseñas_en_archivo(contraseñas, nombre_archivo="contraseñas.txt"):
    with open(nombre_archivo, "w") as archivo:
        for contraseña in contraseñas:
            archivo.write(contraseña + "\n")

def main():
    longitud = int(input("Ingresa la longitud de la contraseña: "))
    cantidad = int(input("Ingresa la cantidad de contraseñas a generar: "))

    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
    incluir_digitos = input("¿Incluir dígitos? (s/n): ").lower() == 's'
    incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    contraseñas = generar_multiples_contraseñas(cantidad, longitud, incluir_mayusculas, incluir_minusculas, incluir_digitos, incluir_especiales)

    print("\nContraseñas generadas:")
    for i, contraseña in enumerate(contraseñas, start=1):
        print(f"{i}. {contraseña}")

    guardar_archivo = input("¿Quieres guardar las contraseñas en un archivo? (s/n): ").lower() == 's'
    if guardar_archivo:
        nombre_archivo = input("Ingresa el nombre del archivo (por defecto: contraseñas.txt): ") or "contraseñas.txt"
        guardar_contraseñas_en_archivo(contraseñas, nombre_archivo)
        print(f"Contraseñas guardadas en {nombre_archivo}")

if __name__ == "__main__":
    main()
