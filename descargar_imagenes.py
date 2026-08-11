#!/usr/bin/env python3
"""
Descarga las 20 imágenes nuevas del Precio Justo Valdemoro del Rey v2.

Uso:
    python3 descargar_imagenes.py

Requisitos: Python 3 (sin librerías externas, solo la librería estándar).

Qué hace:
    - Lee download_map.json (nombre de archivo local + URL de origen).
    - Descarga cada imagen y la guarda en la carpeta ./imagenes/
    - Si una imagen ya existe, la salta (para poder relanzar el script sin problema).
    - Al final imprime un resumen de aciertos y fallos.

Después de ejecutarlo, sube el contenido de la carpeta imagenes/ a la
carpeta "Precio Justo/imagenes" de Drive, junto a las que ya había.
"""
import json
import os
import urllib.request

DOWNLOAD_MAP_FILE = "download_map.json"
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

    ok, skipped, failed = 0, 0, []

    for item in items:
        # item['image'] viene como "imagenes/nombre.jpg" -> nos quedamos solo con el nombre
        filename = os.path.basename(item["image"])
        dest_path = os.path.join(OUTPUT_DIR, filename)
        url = item["url"]

        if os.path.exists(dest_path):
            print(f"Ya existe, salto: {filename}")
            skipped += 1
            continue

        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as response:
                data = response.read()
            with open(dest_path, "wb") as out:
                out.write(data)
            print(f"Descargada: {filename} ({len(data)} bytes)")
            ok += 1
        except Exception as e:
            print(f"FALLO al descargar {filename}: {e}")
            failed.append(filename)

    print()
    print("=" * 50)
    print(f"Descargadas correctamente: {ok}")
    print(f"Ya existían (saltadas):    {skipped}")
    print(f"Fallidas:                  {len(failed)}")
    if failed:
        print("Archivos que fallaron:", ", ".join(failed))
        print("Puedes relanzar el script para reintentar solo esos (los demás se saltan).")
    print("=" * 50)


if __name__ == "__main__":
    main()
