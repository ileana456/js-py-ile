# 🔍 Verificador de Par o Impar en Python
import random

def verificar_paridad(numero: int) -> str:
    """Retorna 'par' o 'impar' según la paridad del número dado."""
    return "par" if numero % 2 == 0 else "impar"

def main():
    numero = random.randint(1, 100)
    resultado = verificar_paridad(numero)

    print("🎲 Número generado aleatoriamente:")
    print(f"👉 {numero}")
    print(f"📌 El número es {'PAR' if resultado == 'par' else 'IMPAR'}.\n")

if __name__ == "__main__":
    main()