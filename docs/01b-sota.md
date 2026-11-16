# 01b · Estado del arte (SOTA) de mi proyecto

## 1. Problema y preguntas de búsqueda (CE 1c)

**Problema:** una persona que gestiona o desarrolla una web pequeña tiene dificultad para comprobar si es accesible, porque las soluciones de pago que he consultado solo ofrecen pedir una demo (no publican precio) y las gratuitas son herramientas técnicas, que se usan desde la línea de comandos o desde las herramientas de desarrollo del navegador.

| # | Pregunta | Dónde busqué | Fecha |
|---|---|---|---|
| P1 | ¿Qué herramientas existen para analizar la accesibilidad de una web? | Páginas oficiales de cada herramienta y repositorio de axe-core en GitHub | 2026-11-16 |
| P2 | ¿Cuánto cuestan? | Páginas de producto de cada solución | 2026-11-16 |
| P3 | ¿Se pueden usar gratis y desde la línea de comandos? | Páginas de axe-core, Pa11y y Lighthouse | 2026-11-16 |
| P4 | ¿Qué parte se puede automatizar y cuál necesita a una persona? | axe-core, WCAG-EM (W3C) y la oferta de pruebas manuales de Level Access y Siteimprove | 2026-11-16 |
| P5 | ¿Cómo se evalúa la accesibilidad sin herramientas automáticas? | WCAG-EM 2.0 (W3C) | 2026-11-16 |

**Límite:** la lista de soluciones parte de herramientas que ya conocía; no he hecho un barrido sistemático con un buscador de aplicaciones o repositorios. Queda **pendiente** ampliarla antes de H2.

## 2. Soluciones existentes (CE 1a, 1c, 2a)

| Solución | Para quién | Qué hace | Modelo de precio | Enlace y fecha de acceso | Estado (`leído` / `sin leer`) |
|---|---|---|---|---|---|
| axe-core (Deque) | Desarrollo | Motor de pruebas de accesibilidad para webs. Reglas de WCAG 2.0, 2.1 y 2.2 (A, AA, AAA). Dice encontrar de media un 57 % de los problemas de WCAG de forma automática y devuelve como «incomplete» lo que necesita revisión manual | Código abierto (licencia Mozilla Public License 2.0). Precio: no lo dice | https://github.com/dequelabs/axe-core · 2026-11-16 | `leído` |
| Pa11y (CLI, CI y Dashboard) | Diseñadores y desarrolladores; el Dashboard también para personas no desarrolladoras | Herramientas que cargan páginas y señalan problemas de accesibilidad: línea de comandos, integración continua y panel que prueba páginas cada día | Gratuito y de código abierto. No menciona planes de pago | https://pa11y.org/ · 2026-11-16 | `leído` |
| Lighthouse (Google) | Desarrollo web | Auditorías de rendimiento, accesibilidad, SEO y más a partir de una dirección. Se usa desde Chrome DevTools, línea de comandos, módulo de Node o PageSpeed Insights | Código abierto. Precio: no lo dice | https://developer.chrome.com/docs/lighthouse/overview · 2026-11-16 | `leído` |
| Siteimprove (accesibilidad) | Organizaciones de varios sectores (finanzas, sanidad, educación superior, administración, comercio) | Monitoriza de forma continua páginas web, PDF y otros contenidos; prioriza y corrige; ofrece pruebas manuales con personas expertas certificadas | No lo dice: solo ofrece «Request a demo» | https://www.siteimprove.com/platform/accessibility/ · 2026-11-16 | `leído` |
| Axe Monitor (Deque) | Responsables de producto, agencias y equipos de desarrollo y QA | Monitorización y informes automáticos de accesibilidad de webs y PDF, con puntuaciones y evolución en el tiempo | No lo dice: solo ofrece «Schedule a Demo» | https://www.deque.com/axe/monitor/ · 2026-11-16 | `leído` |
| Level Access | Empresas (UE, finanzas, software, educación, comercio) y sector público | Plataforma con tres pilares: pruebas y auditoría, corrección y gobernanza; incluye pruebas manuales y auditorías | No lo dice: solo ofrece una demo de 30 minutos | https://www.levelaccess.com/ · 2026-11-16 | `leído` |
| WCAG-EM 2.0 (W3C), evaluación manual por una persona experta | Quien evalúa la accesibilidad de un producto digital (deducido por el título y los pasos) | Metodología en cinco pasos: definir el alcance, explorar el producto, elegir una muestra, evaluarla e informar. **Alternativa no digital** | No lo dice. Es una Nota de Grupo de Trabajo del 23 de julio de 2026 | https://www.w3.org/TR/WCAG-EM/ · 2026-11-16 | `leído` |

## 3. Modelos de negocio (CE 1d, 1e)

*Qué **patrones** se repiten en las soluciones del apartado 2 (suscripción, *freemium*, comisión por operación, licencia, publicidad, servicio gratuito o público) y por qué. Describe con un **Business Model Canvas** (opcional; el profesor te da el material) **2-3 casos**. Termina con el modelo que seguiría **tu** proyecto, o qué ahorra o mejora si no es un negocio.*

| Patrón | Soluciones que lo usan | Ventaja | Riesgo |
|---|---|---|---|
| [RELLENAR] | | | |

## 4. Herramientas y tecnologías (CE 2a, 2b)

*Para cada decisión técnica importante (lenguaje y *framework*, base de datos, despliegue, autenticación…), compara **2-3 opciones con los mismos criterios**. Marca la que eliges.*

| Decisión | Opción | Madurez | Licencia | Coste | Curva de aprendizaje | Encaje con el ciclo | Elegida |
|---|---|---|---|---|---|---|---|
| [RELLENAR: p. ej. base de datos] | | | | | | | |

*Cada decisión importante se convierte en una decisión registrada en [`decisiones/`](decisiones/0000-plantilla.md).*

## 5. Hueco y diferenciación (CE 1e)

- Las tres soluciones de pago que he leído (Siteimprove, Axe Monitor y Level Access) solo ofrecen pedir una demo y no muestran precios, así que quien tiene poco presupuesto no puede saber de antemano si le sirven.
- Las gratuitas (axe-core, Pa11y y Lighthouse) cubren la parte automática, pero son herramientas técnicas. axe-core devuelve como «incomplete» lo que exige revisión manual, y WCAG-EM propone un proceso de cinco pasos (alcance, exploración, muestra, evaluación e informe) que va más allá de lanzar una herramienta.
- **Propuesta de AriaScope (hipótesis por contrastar):** una herramienta de línea de comandos de código abierto que dé, en un solo informe legible, lo detectado y lo que hay que revisar a mano, pensada para quien no es especialista, sin cuenta ni demo.
- **Honestidad:** Pa11y y axe-core ya cubren la detección automática y son mejores para quien necesite un panel o monitorización continua. Si AriaScope no aporta ese informe claro, no se justifica.

## 6. Decisiones derivadas (CE 1e, 1f, 2b)

*Qué consecuencias tiene este estudio en tu proyecto.*

- **Tipo de proyecto elegido** (enlaza con el apartado 3 de [`01-analisis.md`](01-analisis.md)): [RELLENAR]
- **Requisitos que salen del estudio** (con su ID del apartado 4 de `01-analisis.md`): [RELLENAR]
- **Decisiones técnicas** (enlace a cada archivo de `decisiones/`): [RELLENAR]

## 7. Fuentes y calidad (CE 2a)

*Al menos **2 fuentes independientes** (no dos páginas de la misma empresa). Datos oficiales o primarios antes que blogs.*

| # | Fuente (enlace) | Tipo | Fecha de acceso | Fiabilidad (alta / media / baja) y por qué |
|---|---|---|---|---|
| F1 | [RELLENAR] | | | |

## 8. Límites

*Qué **no pudiste comprobar** y qué datos son estimaciones. Una lista corta y honesta es mejor que fingir certeza.*

- [RELLENAR]

---

## Criterios de evaluación que alimenta este documento (texto literal)

- **1a)** Se han clasificado las empresas del sector por sus características organizativas y el tipo de producto o servicio que ofrecen.
- **1c)** Se han identificado las necesidades más demandadas a las empresas.
- **1d)** Se han valorado las oportunidades de negocio previsibles en el sector.
- **1e)** Se ha identificado el tipo de proyecto requerido para dar respuesta a las demandas previstas.
- **1f)** Se han determinado las características específicas requeridas al proyecto.
- **2a)** Se ha recopilado información relativa a los aspectos que van a ser tratados en el proyecto.
- **2b)** Se ha realizado el estudio de viabilidad técnica del mismo.

> El SOTA **no añade criterios de evaluación**: reúne en un solo sitio lo que 1a-1f y 2a-2b ya piden. La evaluación sigue las listas de cotejo de H1 y H2.
