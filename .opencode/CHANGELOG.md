# Registro de cambios de `.opencode/`

Una entrada por cambio, la más reciente arriba. Tipos: **Añadido**, **Cambiado**, **Corregido**, **Retirado**.
Cada pieza tiene su propia versión SemVer (`X.Y.Z`):

| Sube | Cuándo |
|---|---|
| **MAYOR** | Cambia de forma que lo que ya hacías deja de valer (nombre, permisos, formato) |
| **MENOR** | Añade una función sin romper lo anterior |
| **PARCHE** | Corrige un fallo o mejora la redacción |

Mientras la versión empiece por `0.`, la pieza está en prueba y puede cambiar más de lo habitual.

## Sin publicar

(vacío)

## 2026-11-16 · primera versión

- **Añadido** agentes `guia` 0.1.0 y `documentador` 0.1.0.
- **Añadido** skills `crear-repositorio` 0.1.0, `documento-inicio` 0.1.0, `soluciones-existentes` 0.1.0, `sector-y-empresas` 0.1.0, `necesidades-y-tipo` 0.1.0, `comprobar-hecho-cuando` 0.1.0 y `auditar-fuentes` 0.1.0.
- **Probado** (2026-11-16, OpenCode 2.2.6, `deepseek-v4.1-flash-free`): `guia` carga la skill `crear-repositorio`, da **un solo paso**, avisa de la privacidad y cierra con las tres cosas que pide su formato. El resto de piezas se cargan, pero no se han ejecutado todavía.
- **Añadido** comandos `paso` 0.1.0, `comprobar` 0.1.0 y `documentar` 0.1.0.
