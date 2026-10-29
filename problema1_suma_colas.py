"""
problema1_suma_colas.py - Suma elemento a elemento de dos colas (interactivo).

El usuario puede ingresar sus propias colas o ejecutar el ejemplo de la
actividad (A=[3,4,2,8,12], B=[6,2,9,11,3] -> [9,6,11,19,15]).

Uso:  python problema1_suma_colas.py
"""
from cola import Cola


def crear_cola(valores: list[int]) -> Cola[int]:
    """Construye una Cola a partir de una lista. Complejidad: O(n)."""
    cola: Cola[int] = Cola()
    for valor in valores:
        cola.encolar(valor)
    return cola


def cola_a_lista(cola: Cola[int]) -> list[int]:
    """Convierte una cola en lista SIN alterarla (rota n veces).
    Complejidad: O(n) tiempo, O(n) espacio."""
    resultado = []
    for _ in range(cola.obtener_tamaño()):
        elemento = cola.desencolar()
        resultado.append(elemento)
        cola.encolar(elemento)  # se reinserta: la cola queda igual
    return resultado


def sumar_colas(cola_a: Cola[int], cola_b: Cola[int]) -> Cola[int]:
    """Devuelve una nueva Cola con la suma uno a uno de cola_a y cola_b.

    Las colas originales quedan intactas (cada elemento se desencola,
    se usa y se vuelve a encolar, preservando el orden).

    Complejidad: O(n) en tiempo y O(n) en espacio (cola resultado),
    con n = tamaño de las colas.
    Lanza ValueError si las colas tienen distinto tamaño.
    """
    if cola_a.obtener_tamaño() != cola_b.obtener_tamaño():
        raise ValueError("Las colas deben tener la misma cantidad de elementos")

    resultado: Cola[int] = Cola()
    for _ in range(cola_a.obtener_tamaño()):
        a = cola_a.desencolar()
        b = cola_b.desencolar()
        resultado.encolar(a + b)
        cola_a.encolar(a)  # restaurar
        cola_b.encolar(b)
    return resultado


def pedir_cola(nombre: str) -> Cola[int]:
    """Pide por consola números separados por espacios y arma la cola.
    Repite hasta recibir datos válidos. Complejidad: O(n) por intento."""
    while True:
        texto = input(f"Ingrese los números de la Cola {nombre} (separados por espacio): ")
        try:
            valores = [int(x) for x in texto.split()]
        except ValueError:
            print("  Error: ingrese solo números enteros (ej: 3 4 2 8 12).")
            continue
        if not valores:
            print("  Error: la cola no puede estar vacía.")
            continue
        return crear_cola(valores)


def mostrar_resultado(cola_a: Cola[int], cola_b: Cola[int], resultado: Cola[int]) -> None:
    """Imprime las tres colas en formato tabla. Complejidad: O(n)."""
    print(f"\n{'Cola A':>8}{'Cola B':>8}{'Resultado':>11}")
    for a, b, r in zip(cola_a_lista(cola_a), cola_a_lista(cola_b), cola_a_lista(resultado)):
        print(f"{a:>8}{b:>8}{r:>11}")


def ejecutar_ejemplo() -> None:
    """Prueba automática con los datos de la actividad."""
    cola_a = crear_cola([3, 4, 2, 8, 12])
    cola_b = crear_cola([6, 2, 9, 11, 3])
    esperado = [9, 6, 11, 19, 15]

    resultado = sumar_colas(cola_a, cola_b)
    mostrar_resultado(cola_a, cola_b, resultado)

    obtenido = cola_a_lista(resultado)
    assert obtenido == esperado, f"Se esperaba {esperado} y se obtuvo {obtenido}"
    print(f"\nPrueba superada: {obtenido} == {esperado}")


def ejecutar_manual() -> None:
    """El usuario ingresa sus colas y se muestra la suma."""
    cola_a = pedir_cola("A")
    cola_b = pedir_cola("B")
    try:
        resultado = sumar_colas(cola_a, cola_b)
    except ValueError as error:
        print(f"\n  {error} (A tiene {cola_a.obtener_tamaño()}, B tiene {cola_b.obtener_tamaño()}).")
        return
    mostrar_resultado(cola_a, cola_b, resultado)
    print(f"\nResultado: {cola_a_lista(resultado)}")


def main() -> None:
    while True:
        print("\n" + "=" * 40)
        print("   SUMA DE COLAS")
        print("=" * 40)
        print("  1. Ingresar mis propias colas")
        print("  2. Ejecutar ejemplo de la actividad")
        print("  3. Salir")
        opcion = input("\nElija una opción: ").strip()

        if opcion == "1":
            ejecutar_manual()
        elif opcion == "2":
            ejecutar_ejemplo()
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("  Opción inválida. Elija 1, 2 o 3.")


if __name__ == "__main__":
    main()
