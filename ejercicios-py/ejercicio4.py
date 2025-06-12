import random

def jugar_adivinanza():
    """
    Juego de adivinanza donde el usuario intenta adivinar un número secreto.
    """
    secreto = random.randint(1, 100)
    intentos_maximos = 7  # Puedes ajustar la dificultad cambiando este valor
    intentos_restantes = intentos_maximos

    print("¡Bienvenido al juego de adivinanza!")
    print(f"Estoy pensando en un número entre 1 y 100. Tienes {intentos_maximos} intentos.")

    while intentos_restantes > 0:
        try:
            intento = int(input(f"Intento {intentos_maximos - intentos_restantes + 1}: Ingresa tu número: "))
            if not (1 <= intento <= 100):
                print("Por favor, ingresa un número válido entre 1 y 100.")
                continue # Regresa al inicio del bucle para que el usuario intente de nuevo
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue # Regresa al inicio del bucle para que el usuario intente de nuevo

        if intento < secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Correcto! ¡Adivinaste el número {secreto} en {intentos_maximos - intentos_restantes + 1} intentos!")
            return # Termina la función si el usuario gana

        intentos_restantes -= 1

    print(f"¡Agotaste tus intentos! El número era {secreto}.")

# Inicia el juego
jugar_adivinanza()