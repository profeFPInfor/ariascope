# Manifiesto de `.opencode/`

Agentes, skills y comandos de este proyecto, cada uno con **su** versión ([SemVer](https://semver.org/lang/es/) `X.Y.Z`).
La versión de cada pieza está en la propia pieza (línea «Versión: X.Y.Z»); esta tabla debe coincidir. Qué cambia en cada versión: [CHANGELOG.md](CHANGELOG.md).

**Versión del conjunto:** 0.2.1 · **OpenCode:** 2.x (probado con 2.2.6)

| Tipo | Nombre | Versión | Estado | Para qué |
|---|---|---|---|---|
| agente | guia | 0.3.1 | probado en 2.2.6 (1 prueba, de la versión 0.2.1; 2 simulaciones el 2026-11-19, la 2.ª con esta versión) | Te guía paso a paso en las tareas de H1, pasos 0 a 8 (solo lectura) |
| agente | documentador | 0.2.2 | probado en 2.2.6 (2 simulaciones el 2026-11-19; los arreglos, comprobados en esta versión) | Da forma de documentación a lo que tú aportas; escribe en `docs/`, `README.md` y `asistenciaIA/` solo si lo confirmas |
| skill | crear-repositorio | 0.2.1 | probado en 2.2.6 (1 prueba, de la versión 0.1.0) | Paso 0: repositorio público, README y los tres documentos |
| skill | documento-inicio | 0.1.0 | no probado | Aclarar la idea y rellenar `00-documentoInicio.md` |
| skill | soluciones-existentes | 0.1.0 | no probado | Paso 1: problema y soluciones existentes (`01b-sota.md`) |
| skill | sector-y-empresas | 0.1.0 | no probado | Paso 2: sector, empresas y organigrama (`01-analisis.md`) |
| skill | necesidades-y-tipo | 0.1.1 | no probado | Pasos 3 y 4: necesidades, oportunidad y tipo de proyecto |
| skill | objetivos-y-requisitos | 0.1.0 | no probado | Paso 5: objetivos medibles y requisitos RF, RNF y REST con «Cómo se verifica» |
| skill | obligaciones-y-ayudas | 0.1.1 | probado en 2.2.6 (simulación, de la versión 0.1.0) | Paso 6: obligaciones con su norma y una ayuda real con su fuente |
| skill | guion-de-trabajo | 0.1.1 | probado en 2.2.6 (2 simulaciones el 2026-11-19, la 2.ª con esta versión) | Paso 7: las 7 fases con fechas, los hitos, responsables y glosario |
| skill | aporte-del-proyecto | 0.1.0 | no probado | Paso 8: hueco y diferenciación en 3-5 líneas |
| skill | comprobar-hecho-cuando | 0.2.1 | probado en 2.2.6 (2 simulaciones el 2026-11-19, la 2.ª con esta versión) | Comprueba la estructura de un paso, del 0 al 8 (✅ / ❌ / ❓) |
| skill | auditar-fuentes | 0.1.0 | no probado | Comprueba enlace, fecha y estado de cada dato externo |
| skill | validar-estructura-semanal | 0.3.0 | probado en 2.2.6 (2 pruebas, de la versión 0.1.0) | Valida la estructura de toda la semana contra su especificación (`references/semana-NN.json`) |
| comando | paso | 0.2.0 | no probado | `/paso <n>`: la guía te acompaña en un paso (0 a 8) |
| comando | comprobar | 0.2.0 | no probado | `/comprobar <n>`: comprueba un paso (0 a 8) |
| comando | documentar | 0.1.0 | no probado | `/documentar <apartado>`: redacta con el documentador |
| comando | validar | 0.2.0 | probado en 2.2.6 (2 pruebas, de la versión 0.1.0) | `/validar <semana>`: valida la estructura de la semana (`semana-01` o `semana-02`) |
| comando | bitacora | 0.1.0 | no probado | `/bitacora`: anota en `asistenciaIA/bitacora.md` lo hecho con los agentes |

**Estado:** `no probado` = escrito, sin prueba registrada · `probado en 2.x` = hay prueba registrada (ver CHANGELOG). Todas se **cargan** en OpenCode 2.2.6 (`opencode debug agents` y `GET /api/skill`).
