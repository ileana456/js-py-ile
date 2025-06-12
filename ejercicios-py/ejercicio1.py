from tabulate import tabulate
from typing import List, Dict, Any, Union
import sys

# ----------------------- FUNCIONES PRINCIPALES -----------------------

def calcular(num1: float, num2: float, operacion: str) -> Union[float, str]:
    """Realiza una operación matemática básica entre dos números."""
    try:
        match operacion:
            case '+': return num1 + num2
            case '-': return num1 - num2
            case '*': return num1 * num2
            case '/': return "Error: división por cero" if num2 == 0 else round(num1 / num2, 2)
            case _:  return "Operación no válida"
    except Exception as e:
        return f"Error: {e}"

def mostrar_resultados(resultados: List[Dict[str, Any]], titulo: str) -> None:
    """Muestra resultados tabulados con título y formato."""
    print(f"\n🔷 {titulo}")
    print(tabulate(resultados, headers="keys", tablefmt="fancy_grid"))
    sys.stdout.flush()

def ejecutar_operaciones(numeros: List[float], operaciones: List[str]) -> List[Dict[str, Any]]:
    """Ejecuta operaciones entre pares de números en una lista."""
    resultados = []
    for i in range(0, len(numeros) - 1, 2):
        n1, n2 = numeros[i], numeros[i + 1]
        for op in operaciones:
            resultado = calcular(n1, n2, op)
            resultados.append({
                "Número 1": n1,
                "Número 2": n2,
                "Operación": op,
                "Resultado": resultado
            })
    return resultados

# ----------------------- DATOS Y FLUJO PRINCIPAL -----------------------

def main():
    print("🧮 Calculadora Avanzada en Python")
    sys.stdout.flush()

    numeros = [5, 3, 10, 0, 2, 4, 10, 2]
    operaciones = ['+', '-', '*', '/']

    print("\n🚀 Iniciando sección 1: Operaciones básicas con for tradicional...")
    resultados = ejecutar_operaciones(numeros, operaciones)
    mostrar_resultados(resultados, "1️⃣ Resultados de operaciones")

    print("\n✅ Ejecución completada correctamente.\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()

