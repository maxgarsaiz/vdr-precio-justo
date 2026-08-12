#!/usr/bin/env python3
"""
Descarga las imágenes de sustitución para la edición retro (pesetas) del
Precio Justo Valdemoro del Rey v3: Singer 15K y Gramola "La Voz de su Amo".

Uso:
    python3 sustituir_imagenes.py

A diferencia de descargar_imagenes.py (que salta archivos ya existentes),
este script SIEMPRE sobrescribe, porque el objetivo es precisamente
reemplazar imágenes antiguas (p. ej. gramofono.jpg pasa de ser el
gramófono sin fecha a ser la gramola "La Voz de su Amo" de 1940).

Después de ejecutarlo, sube los archivos de la carpeta imagenes/ a la
carpeta "Precio Justo/imagenes" de Drive, sobrescribiendo los que ya había.
"""
import json
import os
import urllib.request

DOWNLOAD_MAP_FILE = "download_map_v3.json"
OUTPUT_DIR = "imagenes"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def main():
    if not os.path.exists(DOWNLOAD_MAP_FILE):
        print(f"ERROR: no encuentro {DOWNLOAD_MAP_FILE} en esta carpeta.")
        print("Asegúrate de ejecutar este script desde la misma carpeta donde lo has guardado.")
        return

    with open(DOWNLOAD_MAP_FILE, "r", encoding="utf-8") as f:
        items = json.load(f)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    ok, failed = 0, []

    for item in items:
        filename = os.path.basename(item["image"])
        dest_path = os.path.join(OUTPUT_DIR, filename)
        url = item["url"]
        existed = os.path.exists(dest_path)

        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as response:
                data = response.read()
            with open(dest_path, "wb") as out:
                out.write(data)
            accion = "Sustituida" if existed else "Descargada"
            print(f"{accion}: {filename} ({len(data)} bytes)")
            ok += 1
        except Exception as e:
            print(f"FALLO al descargar {filename}: {e}")
            failed.append(filename)

    print()
    print("=" * 50)
    print(f"Correctas: {ok}")
    print(f"Fallidas:  {len(failed)}")
    if failed:
        print("Archivos que fallaron:", ", ".join(failed))
    print("=" * 50)


if __name__ == "__main__":
    main()
