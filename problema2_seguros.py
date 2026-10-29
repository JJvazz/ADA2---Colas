"""
problema2_seguros.py - Gestión de colas de servicios de una aseguradora.

Comandos:
    C <servicio>   Llega un cliente: se encola y recibe su número de turno.
    A <servicio>   Se atiende: se desencola y se muestra el turno llamado.
    S              Salir.

Uso:  python problema2_seguros.py
"""
from cola import Cola

# Catálogo de servicios (número -> nombre). Fácil de ampliar.
SERVICIOS = {
    1: "Siniestros",
    2: "Altas de póliza",
    3: "Pagos y cobranzas",
    4: "Consultas generales",
}


class SistemaTurnos:
    """Mantiene una Cola por servicio y un contador de turnos por servicio."""

    def __init__(self, servicios: dict[int, str]) -> None:
        self.servicios = servicios
        self.colas: dict[int, Cola[str]] = {s: Cola() for s in servicios}
        self.contadores: dict[int, int] = {s: 0 for s in servicios}

    def llegada_cliente(self, servicio: int) -> str:
        """Genera el turno (ej. 'S1-003') y lo encola.
        Complejidad: O(1) (acceso a dict + encolar)."""
        self.contadores[servicio] += 1
        turno = f"S{servicio}-{self.contadores[servicio]:03d}"
        self.colas[servicio].encolar(turno)
        return turno

    def atender_cliente(self, servicio: int) -> str | None:
        """Desencola y devuelve el próximo turno, o None si no hay espera.
        Complejidad: O(1)."""
        cola = self.colas[servicio]
        if cola.esta_vacia():
            return None
        return cola.desencolar()

    def en_espera(self, servicio: int) -> int:
        """Cantidad de clientes esperando en un servicio. O(1)."""
        return self.colas[servicio].obtener_tamaño()


def interpretar_comando(texto: str) -> tuple[str, int | None]:
    """Separa la letra de comando y el número de servicio.
    Complejidad: O(1). Lanza ValueError si el formato es inválido."""
    partes = texto.strip().upper().split()
    if len(partes) == 1 and partes[0] == "S":
        return "S", None
    if len(partes) == 2 and partes[0] in ("C", "A") and partes[1].isdigit():
        return partes[0], int(partes[1])
    raise ValueError("Formato inválido. Use 'C <n>', 'A <n>' o 'S'.")


def mostrar_menu(servicios: dict[int, str]) -> None:
    print("=" * 46)
    print("   COMPAÑÍA DE SEGUROS - SISTEMA DE TURNOS")
    print("=" * 46)
    for numero, nombre in servicios.items():
        print(f"  {numero}. {nombre}")
    print("-" * 46)
    print("  C <n>: llega cliente | A <n>: atender | S: salir")
    print("=" * 46)


def main() -> None:
    sistema = SistemaTurnos(SERVICIOS)
    mostrar_menu(SERVICIOS)

    while True:  # Cada iteración es O(1): el costo lo marcan las operaciones de cola
        entrada = input("\n> ")
        try:
            comando, servicio = interpretar_comando(entrada)
        except ValueError as error:
            print(f"  {error}")
            continue

        if comando == "S":
            print("Sistema cerrado.")
            break

        if servicio not in SERVICIOS:
            print(f"  El servicio {servicio} no existe. Opciones: {list(SERVICIOS)}")
            continue

        nombre = SERVICIOS[servicio]
        if comando == "C":
            turno = sistema.llegada_cliente(servicio)
            print(f"  Turno asignado: {turno} ({nombre}). "
                  f"Clientes en espera: {sistema.en_espera(servicio)}")
        else:  # comando == "A"
            turno = sistema.atender_cliente(servicio)
            if turno is None:
                print(f"  No hay clientes en espera en {nombre}.")
            else:
                print(f"  Llamando a {turno} ({nombre}). "
                      f"Quedan en espera: {sistema.en_espera(servicio)}")


if __name__ == "__main__":
    main()
