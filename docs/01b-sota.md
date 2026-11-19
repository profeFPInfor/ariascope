# 01b · Estado del arte (SOTA) de mi proyecto

> **Estado:** borrador (2026-11-19). Todavía no lo ha revisado el tutor.
>
> **Para qué sirve:** el **SOTA** (*state of the art*, estado del arte) es lo que ya existe hoy para resolver mi problema. Sirve para decidir qué aporta AriaScope y qué herramientas usar. Cada apartado responde a un **CE** (criterio de evaluación, 1a a 1i y 2a a 2b; el texto está al final).
>
> **Qué se entrega en H1:** los apartados **1, 2 y 5**. Los apartados 3, 4, 6, 7 y 8 se completan en H2.
>
> **Cómo leerlo (5 minutos):** en las tablas, lo que dice la fuente va **sin marca** (es lo que ella *declara*, no lo he probado). Lo que pienso yo va marcado como **«opinión mía»** o **«deducción mía»**. `leído` = abrí la fuente; `sin leer` = no la abrí. Si no entiendes una sigla, mira el apartado 9.

## 1. Problema y preguntas de búsqueda (CE 1c)

**Problema:** una persona que gestiona o desarrolla una web pequeña tiene dificultad para comprobar si es accesible. Las soluciones de pago que he consultado solo ofrecen pedir una demo y no publican el precio. Las gratuitas de línea de comandos exigen manejar una terminal, y las extensiones de navegador (WAVE, Accessibility Insights) tienen interfaz visual pero se usan página a página (apartado 2).

| # | Pregunta | Dónde busqué | Fecha |
|---|---|---|---|
| P1 | ¿Qué herramientas existen para analizar la accesibilidad de una web? | Páginas oficiales de cada herramienta y repositorio de axe-core en GitHub | 2026-11-16 |
| P2 | ¿Cuánto cuestan? | Páginas de producto de cada solución | 2026-11-16 |
| P3 | ¿Se pueden usar gratis y desde la línea de comandos? | Páginas de axe-core, Pa11y y Lighthouse | 2026-11-16 |
| P4 | ¿Qué parte se puede automatizar y cuál necesita a una persona? | axe-core, WCAG-EM (W3C) y la oferta de pruebas manuales de Level Access y Siteimprove | 2026-11-16 |
| P5 | ¿Cómo se evalúa la accesibilidad sin herramientas automáticas? | WCAG-EM 2.0 (W3C) | 2026-11-16 |

**Límite:** la lista parte de herramientas que ya conocía. El 2026-11-19 la contrasté con el directorio del W3C WAI y añadí las que faltaban (apartado 2), pero **no he hecho un barrido sistemático** con un buscador de aplicaciones o repositorios (ver apartado 8).

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
| `@axe-core/cli` y `@axe-core/playwright` (Deque) | Desarrollo | Orden `axe <url>` que guarda los resultados en JSON (`--save`) y termina con código 1 si alguna regla falla (`--exit`); y API de Playwright (`new AxeBuilder({ page }).analyze()`). **Es lo más parecido a AriaScope (opinión mía).** El README del CLI necesita un controlador de Chrome (ChromeDriver) y no dice cómo separa lo «incomplete» | Código abierto (MPL-2.0, repositorio `axe-core-npm`). Precio: no lo dice | https://github.com/dequelabs/axe-core-npm · 2026-11-19 | `leído` |

**Otras soluciones revisadas** (no entran en la tabla principal para respetar el máximo de 8 filas; el estado es el de cada enlace):

| Solución | Para quién | Qué hace | Modelo de precio | Enlace y fecha de acceso | Estado (`leído` / `sin leer`) |
|---|---|---|---|---|---|
| IBM Equal Access `accessibility-checker` | Equipos que prueban en Node | Escanea URLs y ficheros con la orden `achecker` e informa en JSON, CSV, HTML y XLSX; sirve para integración continua (Selenium, Puppeteer, Playwright). El README no define «needs review» | Código abierto (Apache-2.0) | https://github.com/IBMa/equal-access · 2026-11-19 | `leído` |
| Lighthouse CI | Desarrollo | Ejecuta Lighthouse en cada Pull Request y evita regresiones de accesibilidad, SEO y rendimiento | Código abierto (Apache-2.0) | https://github.com/GoogleChrome/lighthouse-ci · 2026-11-19 | `leído` |
| WAVE (extensión) | Quien edita contenido web | Evalúa la página renderizada en el navegador (Chrome, Firefox, Edge) y, según su página, no envía información al servidor de WAVE. Su página no menciona línea de comandos | Precio de la extensión: no lo dice. Hay una «subscription API» sin precios | https://wave.webaim.org/extension/ · 2026-11-19 | `leído` |
| Accessibility Insights | Desarrollo y pruebas | Extensión para Chrome y Edge con «FastPass» (revisión rápida), versión para Windows y evaluación contra WCAG 2.1 AA. No menciona línea de comandos | Código abierto. Precio: no lo dice | https://accessibilityinsights.io/ · 2026-11-19 | `leído` |
| Directorio de herramientas del W3C WAI | Quien busca una herramienta | 119 herramientas con filtro «Command-line / CI» | Gratuito (es un directorio) | https://www.w3.org/WAI/test-evaluate/tools/list/ · 2026-11-19 | `leído` solo los primeros 100.000 caracteres |
| TAW (Fundación CTIC) | Quien analiza una web | No pude abrir su web; no afirmo nada | no lo dice | https://www.tawdis.net/ · 2026-11-19 | `sin leer` |


## 3. Modelos de negocio (CE 1d, 1e)

Patrones que se repiten en las soluciones del apartado 2. Lo que sale de la lectura de sus páginas va sin marca; lo que **deduzco** lo digo.

| Patrón | Soluciones que lo usan | Ventaja | Riesgo |
|---|---|---|---|
| Plataforma de pago con demo y sin precio publicado | Siteimprove, Axe Monitor y Level Access (solo ofrecen «demo») | Servicios con personas expertas y monitorización continua (lo ofrecen ellas) | Quien tiene poco presupuesto no puede saber el coste antes de hablar con ventas (es el problema del apartado 1) |
| Código abierto gratuito, sin plan de pago visible | Pa11y (no menciona planes de pago), Lighthouse (código abierto) | Cualquier equipo técnico puede adoptarlo sin pedir permiso | De dónde sale la financiación **no consta** en lo que leí |
| Motor abierto y plataforma de pago del mismo fabricante | Deque: axe-core (MPL-2.0) y Axe Monitor (demo) | **Deducción mía:** el motor abierto acerca usuarios a la plataforma de pago | Dependencia de un fabricante; no he comprobado qué parte es gratuita |
| Extensión gratuita más API de suscripción | WAVE: extensión en Chrome, Firefox y Edge y una «subscription API» sin precios publicados (el precio de la extensión no consta) | Se prueba en el navegador sin instalar nada más | No he comprobado condiciones ni precios de la API |
| Evaluación manual por personas expertas | WCAG-EM 2.0 (W3C), pruebas manuales de Level Access y Siteimprove | Cubre lo que ninguna herramienta automática puede decidir | **Deducción mía:** es caro y no escala |

**Modelo de AriaScope:** no es un negocio. Es una herramienta gratuita de código abierto cuyo beneficio es dejar un informe claro a quien no puede pagar una plataforma, más el aprendizaje y el portfolio de quien la hace. **Pendiente:** elegir la licencia; axe-core es MPL-2.0 y habrá que comprobar qué exige esa licencia a quien lo usa como dependencia.

## 4. Herramientas y tecnologías (CE 2a, 2b)

Madurez, licencia y características salen de las páginas oficiales leídas el 2026-11-19. **Curva de aprendizaje y encaje con el ciclo son opinión mía.** Donde la página no lo decía, pone «no lo dice».

| Decisión | Opción | Madurez | Licencia | Coste | Curva de aprendizaje | Encaje con el ciclo | Elegida |
|---|---|---|---|---|---|---|---|
| Navegador automatizado | [Playwright](https://playwright.dev/docs/intro) | Mantenido por Microsoft (copyright 2026); Chromium, WebKit y Firefox en Windows, Linux y macOS | Apache-2.0 | Gratuito | Media | Alto: TypeScript/JavaScript, ya visto en 0612 | **Sí** |
| Navegador automatizado | [Puppeteer](https://github.com/puppeteer/puppeteer) | Organización propia en GitHub; solo Chrome y Firefox | Apache-2.0 | Gratuito | Media | Alto, igual que Playwright | No: menos navegadores |
| Navegador automatizado | [Selenium](https://www.selenium.dev/documentation/overview/) | Gestionado por Software Freedom Conservancy; muchos lenguajes | Apache-2.0 | Gratuito | Media-alta (WebDriver, drivers) | Medio | No |
| Motor de reglas | [axe-core](https://github.com/dequelabs/axe-core) | Deque; reglas de WCAG 2.0, 2.1 y 2.2; devuelve «incomplete» | MPL-2.0 | Gratuito | Baja | Alto | **Sí** |
| Motor de reglas | HTML_CodeSniffer, motor por defecto de [Pa11y](https://github.com/pa11y/pa11y) | [Repositorio](https://github.com/squizlabs/HTML_CodeSniffer) sin aviso de archivado; fecha del último cambio: no lo dice | BSD-3-Clause | Gratuito | Baja | Medio | No: no he podido confirmar que siga mantenido |
| Motor de reglas | [IBM Equal Access (accessibility-checker)](https://github.com/IBMa/equal-access) | Paquete para Node con orden `achecker` e informes JSON, CSV, HTML y XLSX | Apache-2.0 | Gratuito | Media | Medio | No: es la alternativa más parecida a lo que haría AriaScope; **comparar en H2** |
| Lenguaje | TypeScript sobre Node.js | Playwright lo ofrece de serie; Node 22, 24 o 26 | no aplica | Gratuito | Media | Alto: se usa en 0612 y 0614 | **Sí** |
| Lenguaje | Python | Playwright lo ofrece también para Python | no aplica | Gratuito | Baja | Medio: no es el de los módulos de 2.º | No |

*Cada decisión importante se convierte en una decisión registrada en `decisiones/` (la plantilla llega con el bloque de H2).*

## 5. Hueco y diferenciación (CE 1e)

- Las tres soluciones de pago que he leído (Siteimprove, Axe Monitor y Level Access) solo ofrecen pedir una demo y no muestran precios, así que quien tiene poco presupuesto no puede saber de antemano si le sirven.
- Las gratuitas de línea de comandos o de integración continua (`@axe-core/cli`, Pa11y, Lighthouse CI e IBM `accessibility-checker`) cubren la detección automática y pueden hacer fallar un proceso, pero se manejan desde la terminal o desde Node. WAVE y Accessibility Insights tienen interfaz visual y se usan desde el navegador; sus páginas no mencionan línea de comandos. axe-core devuelve como «incomplete» lo que exige revisión manual, y WCAG-EM propone un proceso de cinco pasos (alcance, exploración, muestra, evaluación e informe) que va más allá de lanzar una herramienta.
- **Propuesta de AriaScope (hipótesis por contrastar):** una herramienta de línea de comandos de código abierto que dé, en un solo informe legible, lo detectado y lo que hay que revisar a mano, pensada para quien no es especialista, sin cuenta ni demo.
- **Honestidad:** el hueco más débil es el informe. `@axe-core/cli` ya guarda resultados en JSON y falla con `--exit`, e IBM `accessibility-checker` ya genera informes HTML y XLSX; **no he comprobado** cómo presenta cada uno lo «a revisar a mano». Pa11y y axe-core cubren la detección y son mejores para quien necesite monitorización continua. Si el informe de AriaScope no es claramente más claro para un no especialista, no se justifica.

## 6. Decisiones derivadas (CE 1e, 1f, 2b)

- **Tipo de proyecto elegido** (enlaza con el apartado 3 de [`01-analisis.md`](01-analisis.md)): herramienta de línea de comandos de código abierto. Alternativas descartadas allí: aplicación web con cuentas y extensión de navegador. El estudio añade una razón en contra de la extensión: WAVE y Accessibility Insights ya son extensiones de navegador.
- **Requisitos que salen del estudio** (IDs del apartado 4 de `01-analisis.md`): RF-03 (separar «fallo detectado» de «a revisar a mano»), RNF-01 (informe legible para no especialistas), RNF-04 (aviso de que lo automático no cubre todo) y REST-02 (solo tecnologías de código abierto).
- **Decisiones técnicas** (se registrarán en `decisiones/` en H2): Playwright, axe-core y TypeScript sobre Node.js, con las alternativas del apartado 4. **Pendiente de H2:** probar `@axe-core/cli` e IBM `accessibility-checker` sobre una página de prueba y comparar su informe con el que haría AriaScope.

## 7. Fuentes y calidad (CE 2a)

Una fuente es **independiente** cuando no es la página de la solución que describe. Las páginas y repositorios de cada herramienta son primarias, pero hablan bien de sí mismas.

| # | Fuente (enlace) | Tipo | Fecha de acceso | Fiabilidad (alta / media / baja) y por qué |
|---|---|---|---|---|
| F1 | [Lista de herramientas de evaluación del W3C WAI](https://www.w3.org/WAI/test-evaluate/tools/list/) | Directorio de un organismo de estándares | 2026-11-19 | Alta como directorio (119 herramientas, con filtro «línea de comandos / CI»); media como evaluación: no valora la calidad de cada herramienta |
| F2 | [WCAG-EM 2.0 (W3C)](https://www.w3.org/TR/WCAG-EM/) | Metodología oficial | 2026-11-16 | Alta: es la fuente del proceso de evaluación manual |
| F3 | Repositorios y páginas oficiales de axe-core, `@axe-core/cli`, Pa11y, Lighthouse CI, IBM Equal Access, Playwright, Puppeteer y Selenium | Fuente primaria de cada fabricante | 2026-11-19 | Alta para licencia y funciones declaradas; media para ventajas: **declarado**, no probado por mí |
| F4 | Páginas de producto de Siteimprove, Axe Monitor y Level Access | Fuente comercial | 2026-11-16 | Baja para precios y beneficios: solo ofrecen demo |

Qué respalda cada fuente: **F1** respalda los apartados 1, 2 y 8; **F2**, los apartados 1, 2 y 5; **F3**, los apartados 2, 3, 4 y 5; **F4**, los apartados 2, 3 y 5.

## 8. Límites

- **Barrido incompleto.** El directorio del W3C lista 119 herramientas y solo leí sus primeros 100.000 caracteres, con 8 herramientas de línea de comandos o CI visibles; **no he revisado el resto**. Un barrido sistemático en GitHub y npm sigue pendiente.
- **TAW** (herramienta gratuita de la Fundación CTIC, en Gijón): no pude abrir su web oficial (error de certificado), así que **no la incluyo en la tabla principal ni afirmo nada de ella** (solo aparece en «otras soluciones revisadas», como `sin leer`). Estado: `sin leer`; enlace: https://www.tawdis.net/ · 2026-11-19.
- **Nada probado.** Todo lo de este documento sale de páginas y README, **no de ejecutar las herramientas**. En particular, no sé qué muestran `@axe-core/cli` ni `accessibility-checker` en la categoría «a revisar a mano»: el README de `@axe-core/cli` no lo especifica y el de `accessibility-checker` no define «needs review».
- **Precios.** No consta el precio de la extensión WAVE ni el de la «subscription API»; las plataformas de pago no publican precio.
- **Mantenimiento.** No he comprobado la fecha del último cambio de HTML_CodeSniffer ni de otras herramientas.
- **Licencia de AriaScope.** Sin elegir; falta comprobar qué exige la MPL-2.0 de axe-core.
- **Necesidad real.** No he hablado con nadie del sector (ver `01-analisis.md`).

## 9. Siglas y términos

| Término | Qué significa |
|---|---|
| CE | Criterio de evaluación: cada punto que se evalúa (1a a 1i y 2a a 2b) |
| H1, H2 | Hitos de entrega del curso: 26-nov-2026 y 21-ene-2027 |
| W3C | World Wide Web Consortium: organismo que publica los estándares de la web |
| WCAG | Pautas de accesibilidad del contenido web que publica el W3C |
| WCAG-EM | Método del W3C para evaluar la accesibilidad de una web en cinco pasos |
| CLI | Interfaz de línea de comandos: se usa escribiendo órdenes en una terminal |
| API | Forma de usar un programa desde otro programa o desde código |
| Integración continua (CI) | Proceso automático que ejecuta comprobaciones cada vez que se sube código al repositorio |
| Regresión | Que algo que ya funcionaba deje de funcionar tras un cambio |
| Pull Request | Propuesta de cambio en GitHub que se revisa antes de integrarla |
| MPL-2.0, Apache-2.0, BSD-3-Clause, LGPL-3.0 | Licencias de código abierto: dicen en qué condiciones se puede usar y copiar el código |
| ChromeDriver | Programa que permite a otro programa controlar el navegador Chrome de forma automática |
| 0612 y 0614 | Módulos de 2.º DAW: desarrollo web en entorno cliente y despliegue de aplicaciones web |

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
