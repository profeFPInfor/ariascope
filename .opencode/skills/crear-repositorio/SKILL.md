---
name: crear-repositorio
description: "Guía paso a paso para crear el repositorio público del proyecto en GitHub con un README.md inicial y copiar los tres primeros documentos a docs/. Úsala cuando la persona diga «crear el repositorio», «paso 0», «subir mi proyecto a GitHub» o «README inicial»."
---

# crear-repositorio

**Versión:** 0.1.0 · **Estado:** no probado

## Objetivo

Que la persona tenga un repositorio **nuevo, público y con README**, con `docs/00-documentoInicio.md`, `docs/01-analisis.md` y `docs/01b-sota.md`, **sin instalar nada** (todo desde la web de GitHub).

## Antes de empezar (díselo primero)

El repositorio es **público**. No se sube nunca: claves, contraseñas, datos personales (suyos o de otras personas) ni información de empresas reales. El **nombre** puede ser real o un alias. Si se equivoca y sube algo así, **no lo borra ella**: avisa al tutor sin copiar el dato.

## Pasos (uno cada vez; tras cada uno, pide qué ve)

1. **Crear:** en github.com, botón **+** (arriba a la derecha) → **New repository**. Nombre en minúsculas, sin tildes ni espacios (guiones). Una frase en **Description**. Marcar **Public** y **Add a README file** → **Create repository**.
   *Debe ver:* la página del repositorio con `README.md` en la lista.
2. **README inicial:** abrir `README.md` → icono del lápiz → escribir título, una frase de qué es, estado («en construcción»), autoría (nombre o alias) y enlaces a los tres documentos → **Commit changes…** → mensaje corto («Añade README») → botón verde.
   *Debe ver:* el README con su título. Los enlaces a `docs/` todavía no abren (es normal).
3. **Los tres documentos:** para cada uno, abrir la plantilla del curso → **Raw** → copiar todo → en su repositorio **Add file → Create new file** → nombre `docs/<fichero>` (al escribir `/` se crea la carpeta) → pegar → **Commit changes…**.
   *Debe ver:* la carpeta `docs/` con tres ficheros.
4. **Comprobar:** abrir el enlace del repositorio en una **ventana privada o de incógnito**: debe cargar sin iniciar sesión. Escribir ese enlace en `docs/00-documentoInicio.md`, apartado 1.

## Hecho cuando

- [ ] El repositorio se abre en una ventana de incógnito y es **público**.
- [ ] Tiene `README.md` con nombre del proyecto, una frase y autoría.
- [ ] Tiene los tres ficheros en `docs/`.
- [ ] El enlace está escrito en `docs/00-documentoInicio.md`.
- [ ] No hay claves ni datos personales.

## Si algo no sale

| Qué ve | Qué hacer |
|---|---|
| Repositorio privado | **Settings** → final de la página → **Danger Zone** → **Change repository visibility** → **Public** (los menús cambian de nombre: si no lo encuentra, que escriba al tutor) |
| Fichero fuera de `docs/` | Abrirlo → lápiz → escribir `docs/` delante del nombre → commit |
| No puede abrir la plantilla | Puede que no tenga acceso al repositorio del curso: que escriba al tutor |

## Qué NO haces

- No creas el repositorio ni los ficheros por la persona (no tienes permiso y no es tu papel).
- No das por bueno un paso sin que te diga qué ve.

## Cómo probarla

Pedir «Guíame en el paso 0». Debe preguntar en qué punto estoy, dar **un** paso y pedir qué veo.
