# Estructura de datos: Cola (Queue) en Python

Resolución de dos ejercicios usando una clase `Cola` genérica con principio **FIFO** (First In, First Out).

1. **Suma de colas**: recibe dos colas de enteros y devuelve una nueva cola con la suma elemento a elemento.
2. **Sistema de turnos para una aseguradora**: simula la llegada y atención de clientes en varias colas de servicio.

## Requisitos

- Python **3.10 o superior** (se usan anotaciones como `str | None`)
- No requiere librerías externas (solo la biblioteca estándar)

```bash
python --version
```

## Cómo clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/<nombre-del-repositorio>.git
cd <nombre-del-repositorio>
```

## Estructura del proyecto

```
.
├── cola.py                  # Clase genérica Cola (módulo reutilizable)
├── problema1_suma_colas.py  # Problema 1: suma elemento a elemento
├── problema2_seguros.py     # Problema 2: turnos de una aseguradora
└── README.md
```

| Archivo | Descripción |
|---|---|
| `cola.py` | Clase `Cola` con `encolar`, `desencolar`, `esta_vacia`, `ver_frente` y `obtener_tamaño`. |
| `problema1_suma_colas.py` | Función `sumar_colas` y bloque de prueba con datos de ejemplo. |
| `problema2_seguros.py` | Aplicación interactiva con bucle `while` e `input()`. |

## Ejecución

> Ejecute los scripts desde la carpeta raíz, para que `import cola` funcione.

### Problema 1: Suma de colas

```bash
python problema1_suma_colas.py
```

Salida esperada:

```
  Cola A  Cola B  Resultado
       3       6          9
       4       2          6
       2       9         11
       8      11         19
      12       3         15

Prueba superada: [9, 6, 11, 19, 15] == [9, 6, 11, 19, 15]
```

### Problema 2: Sistema de turnos

```bash
python problema2_seguros.py
```

| Comando | Acción |
|---|---|
| `C <n>` | Llega un cliente al servicio `n`; se le asigna un turno. |
| `A <n>` | Se atiende al próximo cliente del servicio `n`. |
| `S` | Salir del programa. |

Servicios disponibles: `1` Siniestros, `2` Altas de póliza, `3` Pagos y cobranzas, `4` Consultas generales.

Ejemplo de sesión:

```
> C 1
  Turno asignado: S1-001 (Siniestros). Clientes en espera: 1
> C 1
  Turno asignado: S1-002 (Siniestros). Clientes en espera: 2
> A 1
  Llamando a S1-001 (Siniestros). Quedan en espera: 1
> A 3
  No hay clientes en espera en Pagos y cobranzas.
> S
Sistema cerrado.
```

## Complejidad algorítmica

| Operación | Complejidad |
|---|---|
| `encolar`, `desencolar`, `ver_frente`, `esta_vacia`, `obtener_tamaño` | O(1) |
| `sumar_colas` | O(n) tiempo, O(n) espacio |
| Llegada / atención de clientes | O(1) por operación |

La cola se implementa sobre `collections.deque`: `popleft()` es O(1), mientras que `list.pop(0)` sería O(n).

## Decisiones de diseño

- **Genérica**: `Cola[T]` con `typing.Generic` acepta cualquier tipo de dato.
- **Sin efectos secundarios**: `sumar_colas` deja intactas las colas originales.
- **Errores explícitos**: desencolar o ver el frente de una cola vacía lanza `IndexError`.
- **Modular**: la estructura de datos (`cola.py`) está separada de la lógica de cada problema.

## Autor

<Nombre y apellido> - <Materia / Institución>
