# Página de prueba de accesibilidad

`index.html` es una página con **fallos puestos a propósito** para comprobar qué detecta una herramienta. No los corrijas. Las imágenes `logo.png` y `fondo.png` no existen a propósito. La usa el requisito RF-01 de [`docs/01-analisis.md`](../../docs/01-analisis.md).

## Qué contiene

| # | Qué hay | Debe salir como |
|---|---|---|
| 1 | Una imagen sin texto alternativo | Fallo detectado |
| 2 | Un texto gris claro (`#bbbbbb`) sobre fondo blanco | Fallo detectado (contraste) |
| 3 | Un campo de formulario sin etiqueta | Fallo detectado |
| 4 | Un texto sobre una imagen de fondo | A revisar a mano (el contraste no se puede calcular solo) |

## Qué se observó el 2026-11-19

Servida en local (`python3 -m http.server`) y analizada con **axe-core 4.14.1** mediante `@axe-core/playwright` y el Chrome for Testing 158 de Playwright:

- **3 fallos** (`image-alt`, `color-contrast` y `label`) y **1 resultado «incomplete»** (`color-contrast`, el texto sobre la imagen de fondo). Coincide con la tabla de arriba.
- 20 reglas pasadas y 68 no aplicables. Análisis: unos 335 ms, sin contar abrir el navegador.

**IBM `accessibility-checker` 4.0.35** se probó sobre una versión anterior de esta página, que no tenía `lang` en `<html>`: dio 4 fallos (los 3 de arriba y `html_lang_exists`), 2 `potentialviolation` y 2 `manual`. **No se repitió sobre esta versión**: la segunda vez la herramienta no consiguió descargar sus reglas de la red (tiempo agotado). Deduzco que ahora daría 3 fallos, pero no está comprobado.

## Cómo repetirlo (herramienta de línea de comandos de IBM)

```
npx achecker --outputFormat json --outputFolder resultados <dirección de la página>
```

Necesita conexión a internet para descargar las reglas y un navegador instalado.
