import random
import string

def generar_contrasena(longitud, incluir_especiales=False):
    """Genera una contraseña aleatoria.

    Args:
        longitud: La longitud de la contraseña.
        incluir_especiales:  Si se deben incluir caracteres especiales.

    Returns:
        Una cadena de texto que representa la contraseña generada.
    """
    caracteres = string.ascii_letters + string.digits
    if incluir_especiales:
        caracteres += string.punctuation  # Agrega caracteres especiales
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def obtener_longitud():
    """Obtiene la longitud de la contraseña del usuario."""
    while True:
        try:
            longitud = int(input("🔢 Ingresa la longitud deseada para la contraseña (16-40): "))
            if 16 <= longitud <= 40:
                return longitud
            else:
                print("⚠️ La longitud debe estar entre 16 y 40.")
        except ValueError:
            print("❌ Por favor, ingresa un número entero válido.")

def main():
    """Función principal que genera y muestra la contraseña."""
    longitud = obtener_longitud()
    incluir_especiales = input("¿Quieres incluir caracteres especiales? (s/n): ").strip().lower() == 's'
    contrasena = generar_contrasena(longitud, incluir_especiales)
    print("\n🔐 Contraseña generada:")
    print(f"📏 Longitud: {longitud}")
    print(f"🔑 Valor   : {contrasena}")

if __name__ == "__main__":
    main()