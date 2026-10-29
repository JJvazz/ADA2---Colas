"""
cola.py - Estructura de datos Cola (Queue) genérica.

Principio FIFO (First In, First Out): el primer elemento en entrar
es el primero en salir.

Implementación sobre collections.deque. Una lista de Python NO es buena
opción: list.pop(0) cuesta O(n) porque desplaza todos los elementos,
mientras que deque.popleft() cuesta O(1).
"""
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Cola(Generic[T]):
    """Cola FIFO genérica: admite cualquier tipo de dato (int, str, objetos...)."""

    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def encolar(self, elemento: T) -> None:
        """Agrega un elemento al final de la cola.
        Complejidad: O(1) amortizado."""
        self._items.append(elemento)

    def desencolar(self) -> T:
        """Quita y devuelve el elemento del frente.
        Complejidad: O(1).
        Lanza IndexError si la cola está vacía."""
        if self.esta_vacia():
            raise IndexError("No se puede desencolar: la cola está vacía")
        return self._items.popleft()

    def esta_vacia(self) -> bool:
        """Indica si la cola no tiene elementos. Complejidad: O(1)."""
        return len(self._items) == 0

    def ver_frente(self) -> T:
        """Devuelve el elemento del frente sin quitarlo.
        Complejidad: O(1).
        Lanza IndexError si la cola está vacía."""
        if self.esta_vacia():
            raise IndexError("No hay frente: la cola está vacía")
        return self._items[0]

    def obtener_tamaño(self) -> int:
        """Devuelve la cantidad de elementos. Complejidad: O(1)."""
        return len(self._items)

    def __repr__(self) -> str:
        return f"Cola({list(self._items)})"
