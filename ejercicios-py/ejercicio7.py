import random

def invertir_palabra(palabra):
    """Invierte una palabra dada."""
    return palabra[::-1]

def obtener_palabra():
    """Obtiene una palabra, ya sea de una lista predefinida o ingresada por el usuario."""
    palabras_predefinidas = ["Hola", "Python", "Javascript", "OpenAI", "Inteligencia"]
    opcion = input("¿Quieres ingresar una palabra (I) o usar una de la lista (L)? (I/L): ").upper()

    if opcion == "I":
        while True:
            palabra = input("Ingresa una palabra: ")
            if palabra.strip():  # Verifica que la palabra no esté vacía
                return palabra
            else:
                print("Por favor, ingresa una palabra válida.")
    elif opcion == "L":
        return random.choice(palabras_predefinidas)
    else:
        print("Opción inválida. Se usará una palabra de la lista por defecto.")
        return random.choice(palabras_predefinidas)

def jugar_invertir_palabras():
    """Permite al usuario invertir palabras y jugar de nuevo."""
    while True:
        palabra = obtener_palabra()
        palabra_invertida = invertir_palabra(palabra)
        print(f"La palabra original es: '{palabra}'")
        print(f"La palabra invertida es: '{palabra_invertida}'")

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (S/N): ").upper()
        if jugar_de_nuevo != "S":
            break

# Inicia el juego
jugar_invertir_palabras()