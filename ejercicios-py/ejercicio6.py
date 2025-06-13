import random

def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n: Un número entero no negativo.

    Returns:
        El factorial de n, o None si n es negativo.
    """
    if n < 0:
        return None  # El factorial no está definido para números negativos
    elif n == 0:
        return 1  # El factorial de 0 es 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

# Genera un número aleatorio entre 1 y 10
n = random.randint(1, 10)

# Calcula el factorial
resultado = calcular_factorial(n)

# Imprime el resultado
if resultado is not None:
    print(f"{n}! = {resultado}")
else:
    print("El factorial no está definido para números negativos.")