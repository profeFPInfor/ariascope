# Bitácora de uso de IA

Aquí anotas cuándo has usado IA para algo que **acaba en tu proyecto**. **Una fila por tarea**, no por cada pregunta. No hace falta apuntar consultas sueltas ni pruebas que no cambian nada. Si no sabes algo, escribe «pendiente».

| Fecha | Agente y modelo | Qué pediste | Qué aceptaste o cambiaste |
|---|---|---|---|
| 2026-11-16 | Claude Code (Anthropic) | README, documentos `00`, `01` y `01b` con investigación de fuentes (sector, soluciones, marco legal) | Se reabrieron las fuentes y se suavizaron 2 afirmaciones sobre WCAG-EM que no estaban comprobadas. La entrada en vigor de la Ley 11/2023 no se pudo verificar |
| 2026-11-16 | Claude Code (Anthropic) | `.opencode/` (agentes, skills y comandos), validación semanal, ZIP semanal y `.gitignore` | Aceptado; se cargan en OpenCode 2.2.6. Una auditoría de comprensión simulada dio 8,4 (no es una prueba con alumnado) |
| 2026-11-16 | `guia` de OpenCode con modelos gratuitos (`opencode/deepseek-v4.1-flash-free`; `glm`, `minimax` y `hy4` de respaldo) y uno local | «Guíame en el paso 0» y `/validar semana-01` | Con el modelo local falló (intentó la herramienta de preguntas). Con deepseek funcionó y coincidió con el script de validación |
| 2026-11-19 | Claude Code (Anthropic), con búsqueda web | Semana 2: pasos 5 a 8, estado del arte completo, registro de tutoría y hoja de publicación | Se abrieron las leyes (BOE) y los extractos del BOPA citados. No se leyeron las bases de la ayuda, los anexos de la Ley 11/2023 ni la web de TAW. Los umbrales de los requisitos son propuestas por medir |
| 2026-11-19 | Claude Code (Anthropic) | Probar IBM `accessibility-checker` y axe-core sobre una página de prueba nueva (`pruebas/pagina-prueba/`) | Los dos detectan los mismos fallos. `@axe-core/cli` no llegó a ejecutarse (ChromeDriver no coincidía con Chrome) y la repetición de IBM sobre la versión final falló por la red |
| 2026-11-19 | Claude Code (Anthropic) con `guia` y `documentador` de OpenCode | Simular el trabajo del alumnado en los pasos 5 a 8 y arreglar lo que falló | Se aplicaron 4 arreglos; 3 se comprobaron en una 2.ª simulación. La persona la interpretó Claude Code, con contenidos ya investigados |
