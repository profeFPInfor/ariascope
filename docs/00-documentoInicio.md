# 00 · Documento de inicio del proyecto

## 1. Datos del alumno/a

| | |
|---|---|
| **Nombre** | Tever (profesor del módulo; proyecto de referencia para el alumnado) |
| **Usuario de GitHub** | devTever |
| **Repositorio del proyecto** | https://github.com/devTever/ariascope |
| **Ciclo y curso** | DAW, 2.º · curso 2026-27 |
| **Fecha** | 2026-11-16 |

## 2. Nombre del proyecto

**AriaScope.** Herramienta de línea de comandos de código abierto que analiza la accesibilidad de páginas web.

## 3. Qué quiero hacer

Una herramienta que se ejecuta desde la terminal: le das la dirección de una página web y te devuelve un informe de accesibilidad fácil de leer. Por debajo abre la página con un navegador automatizado (Playwright) y le pasa un motor de reglas de accesibilidad de código abierto (axe-core).

La idea es que el informe separe con claridad **lo que se ha detectado como fallo** de **lo que una persona tiene que revisar a mano**, porque ninguna herramienta automática lo cubre todo. Se podrá usar a mano y, más adelante, en un proceso de integración continua (que falle si hay errores).

Es un proyecto **de referencia**: sigue los mismos pasos y usa las mismas plantillas que el alumnado, para que se vea cómo queda cada documento terminado.

## 4. Qué problema o necesidad resuelve

Quien desarrolla o gestiona una web pequeña tiene dificultad para comprobar si es accesible: las soluciones de pago que he consultado solo ofrecen pedir una demo (no publican precios) y las gratuitas son herramientas técnicas, que se usan desde la línea de comandos o desde las herramientas de desarrollo del navegador. Las fuentes están en `01b-sota.md` y el desarrollo, en `01-analisis.md`.

Lo que **todavía no he comprobado** es si esta necesidad la sienten de verdad pymes o estudiantes (no he hablado con nadie del sector): queda como **pendiente**.

## 5. Para quién

- **Estudiantes y desarrolladores junior** que quieren revisar la accesibilidad de sus propios proyectos.
- **Pequeñas empresas y autónomos** con una web propia y sin presupuesto para herramientas de pago.

Contexto de uso: sobre páginas **propias o de prueba**, desde un equipo personal o un servidor de integración continua.

## 6. Funcionalidades principales

| # | Funcionalidad | ¿Imprescindible? (sí / no) |
|---|---|---|
| 1 | Analizar una dirección web y mostrar los fallos de accesibilidad detectados | sí |
| 2 | Generar un informe legible (texto/Markdown) y otro en JSON | sí |
| 3 | Separar «fallo detectado» de «a revisar a mano» | sí |
| 4 | Analizar una lista de direcciones de un fichero | no |
| 5 | Devolver un código de salida distinto de cero si hay fallos (para integración continua) | no |

## 7. Tecnologías previstas

| Tecnología | Para qué | Nivel actual (nada / algo / bien) |
|---|---|---|
| TypeScript y Node.js | Código de la herramienta | pendiente de concretar |
| Playwright | Abrir y recorrer las páginas | pendiente de concretar |
| axe-core | Reglas de accesibilidad | pendiente de concretar |

## 8. Dónde se integra con los módulos de 2.º

- [x] Desarrollo web en entorno cliente (0612): trabajo con el DOM y con JavaScript/TypeScript
- [ ] Desarrollo web en entorno servidor (0613)
- [x] Despliegue de aplicaciones web (0614): publicación como paquete y ejecución en integración continua
- [x] Diseño de interfaces web (0615): la accesibilidad como criterio de diseño

## 9. Datos y empresas

- ¿El proyecto parte de una **empresa** (por ejemplo, de tus prácticas)? **No.**
- ¿Usará **datos personales reales**? **No.** Solo se analizan páginas propias o de prueba; no se almacenan datos de personas.

## 10. Riesgos y dudas iniciales

- **Alcance:** la comprobación automática no cubre toda la accesibilidad. La propia web de axe-core dice que «se puede encontrar de media un 57 % de los problemas de WCAG de forma automática» (dato **declarado** por ellos, sin contrastar). El informe tiene que explicarlo bien para no dar falsa seguridad.
- **Tiempo:** aprender Playwright y axe-core a la vez.
- **Competencia:** ya existen herramientas gratuitas y consolidadas; habrá que justificar qué aporta esta (ver `01b-sota.md`, apartado 5).

## 11. Qué espero aprender

A conectar un navegador automatizado con un motor de reglas, a escribir un informe claro para personas no expertas y a publicar una herramienta de código abierto con su documentación.

---

## Aprobación del tutor

*Esta parte la rellena el tutor.*

| Criterio mínimo | Cumple |
|---|---|
| Necesidad real y documentada | ☐ |
| Alcance abordable en el tiempo disponible | ☐ |
| Integra contenidos de al menos tres módulos de 2.º | ☐ |
| No usa datos personales reales | ☐ |

**Estado:** ☐ Aprobada · ☐ Aprobada con cambios · ☐ Necesita rehacerse

**Fecha:** 

**Comentarios del tutor:**
