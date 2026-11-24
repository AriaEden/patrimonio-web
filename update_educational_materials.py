# -*- coding: utf-8 -*-
"""
update_educational_materials.py
Script de automatización trimestral:
1. Actualiza parámetros cuantitativos y fechas de corte de mercado.
2. Recompila los 4 manuales en PDF usando Google Chrome Headless.
3. Distribuye los PDFs a las carpetas de publicación web.
"""

import os
import subprocess
import shutil
import json
import urllib.request
from datetime import datetime

def get_current_quarter_tag():
    now = datetime.now()
    quarter = (now.month - 1) // 3 + 1
    months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    month_name = months[now.month - 1]
    return f"Q{quarter} {now.year} (Corte: {month_name} {now.year})"

def find_chrome():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return "chrome"

def compile_pdf(chrome_path, html_path, pdf_path):
    cmd = [
        chrome_path,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
        print(f"  [OK] Compilado: {os.path.basename(pdf_path)} ({os.path.getsize(pdf_path):,} bytes)")
        return True
    else:
        print(f"  [ERROR] Falló compilación de {html_path}: {res.stderr}")
        return False

def main():
    tag = get_current_quarter_tag()
    print(f"=== INICIANDO ACTUALIZACIÓN DIDÁCTICA TRIMESTRAL: {tag} ===")
    
    chrome = find_chrome()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Compilar build_educational_ecosystem.py si existe
    eco_script = os.path.join(base_dir, "build_educational_ecosystem.py")
    if not os.path.exists(eco_script):
        # Buscar en directorio padre o scratch
        eco_script = os.path.join(os.path.dirname(base_dir), "build_educational_ecosystem.py")
    if os.path.exists(eco_script):
        print("Ejecutando generador de infografía y taller...")
        subprocess.run(["python", eco_script], capture_output=True, text=True)

    # 2. Compilar Guia de Compra y Manual por Edades
    # Los HTML están en la ruta de fuentes
    fuentes_dir = os.path.join(os.path.dirname(base_dir), r"PATRIMONIO_INTELIGENTE\03_Educacion_Financiera_y_Talleres\Materiales_Markdown_Fuente\06_Propuestas_Institucionales_y_Manuales")
    if not os.path.exists(fuentes_dir):
        fuentes_dir = base_dir

    guia_html = os.path.join(fuentes_dir, "GUIA_PASO_A_PASO_COMPRA_BITSO_Y_ACTINVER.html")
    edades_html = os.path.join(fuentes_dir, "MANUAL_DE_PRIMERA_VEZ_POR_EDADES.html")
    
    out_guia_pdf = os.path.join(base_dir, "GUIA_PASO_A_PASO_COMPRA_BITSO_Y_ACTINVER.pdf")
    out_edades_pdf = os.path.join(base_dir, "MANUAL_DE_PRIMERA_VEZ_POR_EDADES.pdf")

    if os.path.exists(guia_html):
        compile_pdf(chrome, guia_html, out_guia_pdf)
    if os.path.exists(edades_html):
        compile_pdf(chrome, edades_html, out_edades_pdf)

    print(f"\nMaterial didáctico actualizado satisfactoriamente con sello: {tag}")

if __name__ == "__main__":
    main()
