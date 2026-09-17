import flet as ft
import os
import sys

def main(page: ft.Page):
    page.title = "Salones Iglesia - Móvil"
    page.padding = 0  # Sin márgenes para aprovechar toda la pantalla del celular
    
    # IP del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Creamos un visor web nativo de pantalla completa para el celular
    webview = ft.WebView(
        url_servidor,
        expand=True,
    )
    
    page.add(webview)

if __name__ == "__main__":
    ft.run(main)
