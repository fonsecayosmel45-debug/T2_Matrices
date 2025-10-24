import random

Palabra = str
Matriz = list[list[Palabra]]

VOCALES = set("aeiou")

def palabra_aleatoria(longitud: int = 4) -> Palabra:
    return "".join(chr(97 + random.randint(0, 25)) for _ in range(longitud))

def generar_matriz(tamaño: int, longitud_palabra: int = 4) -> Matriz:
    return [[palabra_aleatoria(longitud_palabra) for _ in range(tamaño)] for _ in range(tamaño)]

def tiene_vocal(palabra: Palabra) -> bool:
    return any(letra in VOCALES for letra in palabra)

def contar_vocales_dividir(mat: Matriz, fila_i: int, fila_f: int, col_i: int, col_f: int) -> int:
    alto = fila_f - fila_i
    ancho = col_f - col_i
    if alto == 1 and ancho == 1:
        return 1 if tiene_vocal(mat[fila_i][col_i]) else 0
    if alto == 1 and ancho > 1:
        mitad = col_i + ancho // 2
        return contar_vocales_dividir(mat, fila_i, fila_f, col_i, mitad) + \
               contar_vocales_dividir(mat, fila_i, fila_f, mitad, col_f)
    if ancho == 1 and alto > 1:
        mitad = fila_i + alto // 2
        return contar_vocales_dividir(mat, fila_i, mitad, col_i, col_f) + \
               contar_vocales_dividir(mat, mitad, fila_f, col_i, col_f)
    mitad_f = fila_i + alto // 2
    mitad_c = col_i + ancho // 2
    return (
        contar_vocales_dividir(mat, fila_i, mitad_f, col_i, mitad_c) +
        contar_vocales_dividir(mat, fila_i, mitad_f, mitad_c, col_f) +
        contar_vocales_dividir(mat, mitad_f, fila_f, col_i, mitad_c) +
        contar_vocales_dividir(mat, mitad_f, fila_f, mitad_c, col_f)
    )

def mostrar_matriz(mat: Matriz) -> None:
    for fila in mat:
        print(" ".join(fila))

def main() -> None:
    try:
        n_str = input("Ingrese el tamaño N de la matriz cuadrada (N×N): ").strip()
        n = int(n_str)
        if n <= 0:
            raise ValueError
    except Exception:
        print("Entrada inválida. Por favor, use un número entero positivo.")
        return
    random.seed()
    matriz = generar_matriz(n, longitud_palabra=4)
    print("\nMatriz generada:\n")
    mostrar_matriz(matriz)
    total = contar_vocales_dividir(matriz, 0, n, 0, n)
    print(f"\nTotal de palabras con al menos una vocal: {total}")

if __name__ == "__main__":
    main()
