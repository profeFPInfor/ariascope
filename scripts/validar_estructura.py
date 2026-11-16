#!/usr/bin/env python3
"""Valida la ESTRUCTURA semanal de un repositorio contra una especificación JSON.

Uso:
  python3 scripts/validar_estructura.py semana-01 [--raiz RUTA] [--spec FICHERO] [--json]

- Comprueba estructura (¿existe el fichero, está relleno el apartado, la tabla tiene las
  columnas y filas esperadas, cada fila lleva enlace/fecha y estado?). NO evalúa calidad ni califica.
- La especificación vive junto a la skill `validar-estructura-semanal`
  (.opencode/skills/validar-estructura-semanal/references/<semana>.json): la leen los agentes
  y este script, de modo que ambos aplican exactamente las mismas reglas.
- Código de salida: 0 si todos los controles de nivel «minimo» pasan; 1 si no; 2 si hay un error de uso.
- Solo biblioteca estándar de Python 3.
"""
import argparse
import json
import re
import sys
from pathlib import Path

FECHA = re.compile(r"\d{4}-\d{2}-\d{2}")
URL = re.compile(r"https?://\S+")
GUIA_CURSIVA = re.compile(r"^\s*(\*[^*].*\*|_[^_].*_)\s*$")
COMENTARIO_HTML = re.compile(r"<!--.*?-->", re.S)


def leer_apartado(texto, prefijo):
    """Devuelve el cuerpo del apartado cuyo encabezado '## ...' empieza por `prefijo`."""
    lineas = texto.splitlines()
    ini = None
    for i, l in enumerate(lineas):
        if l.startswith(prefijo):
            ini = i
            break
    if ini is None:
        return None
    fin = len(lineas)
    for j in range(ini + 1, len(lineas)):
        if lineas[j].startswith("## ") or lineas[j].startswith("# "):
            fin = j
            break
    return "\n".join(lineas[ini + 1:fin])


def cuerpo_util(cuerpo):
    """Líneas con contenido real: sin vacías, sin comentarios HTML y sin notas guía en cursiva."""
    cuerpo = COMENTARIO_HTML.sub("", cuerpo)
    return [l for l in cuerpo.splitlines() if l.strip() and not GUIA_CURSIVA.match(l)
            and not l.strip().startswith(">") and l.strip() != "---"]


def celdas(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def primera_tabla(cuerpo):
    """(cabecera, separador, filas) de la primera tabla Markdown, o None."""
    ls = cuerpo.splitlines()
    for i in range(len(ls) - 1):
        if ls[i].strip().startswith("|") and re.match(r"^\s*\|[\s:\-|]+\|\s*$", ls[i + 1]):
            filas = []
            for l in ls[i + 2:]:
                if l.strip().startswith("|"):
                    filas.append(l)
                else:
                    break
            return ls[i], ls[i + 1], filas
    return None


def controlar_apartado(texto, ap):
    res = []
    t = ap["titulo"]
    cuerpo = leer_apartado(texto, t)
    if cuerpo is None:
        return [(False, f"{t}: no existe el apartado")]
    util = cuerpo_util(cuerpo)
    if ap.get("rellenado"):
        res.append((len(util) > 0, f"{t}: tiene contenido propio (no solo las notas guía)"))
    for m in ap.get("sin_marcadores", []):
        res.append((m not in cuerpo, f"{t}: no quedan marcadores «{m}»"))
    if ap.get("mermaid"):
        res.append(("```mermaid" in cuerpo, f"{t}: hay un diagrama Mermaid"))
    if "enlaces_min" in ap:
        n = len(URL.findall(cuerpo))
        res.append((n >= ap["enlaces_min"], f"{t}: al menos {ap['enlaces_min']} enlace(s) (hay {n})"))
    if "tabla" in ap:
        c = ap["tabla"]
        tb = primera_tabla(cuerpo)
        if tb is None:
            res.append((False, f"{t}: hay una tabla Markdown"))
            return res
        cab, sep, filas = tb
        ncab, nsep = len(celdas(cab)), len(celdas(sep))
        res.append((ncab == c["columnas"] and nsep == c["columnas"],
                    f"{t}: la tabla tiene {c['columnas']} columnas en cabecera y separador (hay {ncab} y {nsep})"))
        reales = [f for f in filas if "[RELLENAR" not in f]
        res.append((len(reales) >= c.get("filas_min", 0),
                    f"{t}: al menos {c.get('filas_min', 0)} filas rellenadas (hay {len(reales)})"))
        if "filas_max" in c:
            res.append((len(reales) <= c["filas_max"], f"{t}: como máximo {c['filas_max']} filas (hay {len(reales)})"))
        res.append((all(len(celdas(f)) == c["columnas"] for f in reales),
                    f"{t}: todas las filas tienen {c['columnas']} celdas"))
        res.append((all(all(x for x in celdas(f)) for f in reales), f"{t}: ninguna celda está vacía (usa «no lo dice»)"))
        if "columna_enlace_fecha" in c:
            k = c["columna_enlace_fecha"]
            ok = True
            for f in reales:
                cs = celdas(f)
                if len(cs) <= k:
                    ok = False
                    continue
                v = cs[k]
                if not (FECHA.search(v) and (URL.search(v) or "no aplica" in v.lower())):
                    ok = False
            res.append((ok, f"{t}: cada fila lleva enlace (o «no aplica») y fecha AAAA-MM-DD"))
        if "columna_estado" in c:
            k = c["columna_estado"]
            validos = set(c.get("estados_validos", []))
            ok = all(len(celdas(f)) > k and celdas(f)[k].strip("` ") in validos for f in reales)
            res.append((ok, f"{t}: cada fila tiene estado {' / '.join(sorted(validos))}"))
    return res


def validar(raiz, spec):
    resultados = []
    for fe in spec["ficheros"]:
        ruta = raiz / fe["ruta"]
        nivel, paso = fe["nivel"], fe["paso"]
        cabecera = f"[paso {paso}] {fe['ruta']}"
        if not ruta.exists():
            resultados.append((nivel, paso, False, f"{cabecera}: existe el fichero"))
            continue
        texto = ruta.read_text(encoding="utf-8")
        resultados.append((nivel, paso, True, f"{cabecera}: existe el fichero"))
        if "min_lineas_no_vacias" in fe:
            n = len([l for l in texto.splitlines() if l.strip()])
            resultados.append((nivel, paso, n >= fe["min_lineas_no_vacias"],
                               f"{cabecera}: al menos {fe['min_lineas_no_vacias']} líneas con contenido (hay {n})"))
        for s in fe.get("contiene", []):
            resultados.append((nivel, paso, s in texto, f"{cabecera}: contiene «{s}»"))
        for ap in fe.get("apartados", []):
            for ok, msg in controlar_apartado(texto, ap):
                resultados.append((nivel, paso, ok, f"[paso {paso}] {fe['ruta']} · {msg}"))
    return resultados


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("semana", help="p. ej. semana-01")
    ap.add_argument("--raiz", default=".", help="raíz del repositorio a validar")
    ap.add_argument("--spec", help="ruta a la especificación (por defecto, la de la skill)")
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    a = ap.parse_args()
    raiz = Path(a.raiz).resolve()
    spec_path = Path(a.spec) if a.spec else raiz / ".opencode/skills/validar-estructura-semanal/references" / f"{a.semana}.json"
    if not spec_path.exists():
        print(f"No existe la especificación: {spec_path}", file=sys.stderr)
        return 2
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    res = validar(raiz, spec)
    if a.json:
        print(json.dumps([{"nivel": n, "paso": p, "ok": ok, "control": m} for n, p, ok, m in res], ensure_ascii=False, indent=2))
    else:
        print(f"{spec['titulo']} · especificación {spec['version']} · {raiz}")
        for nivel in ("minimo", "completo"):
            sub = [r for r in res if r[0] == nivel]
            if not sub:
                continue
            print(f"\nNivel {nivel.upper()}: {spec['niveles'][nivel]}")
            for _, _, ok, m in sub:
                print(f"  {'✅' if ok else '❌'} {m}")
    falla_min = [r for r in res if r[0] == "minimo" and not r[2]]
    falla_comp = [r for r in res if r[0] == "completo" and not r[2]]
    if not a.json:
        print(f"\nMínimo: {'CUMPLE' if not falla_min else f'NO cumple ({len(falla_min)} controles)'} · "
              f"Completo: {'CUMPLE' if not falla_comp else f'faltan {len(falla_comp)} controles'}")
    return 0 if not falla_min else 1


if __name__ == "__main__":
    sys.exit(main())
