import flet as ft
import os
import sys

def main(page: ft.Page):
    page.title = "Salones Iglesia - Móvil"
    # Sin márgenes para aprovechar el 100% de la pantalla del celular
    page.padding = 0  
    
    # IP del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # CORREGIDO: Usamos CupertinoWebView que es el nuevo estándar compatible con móviles en Flet moderno
    webview = ft.CupertinoWebView(
        url=url_servidor,
        expand=True,
    )
    
    page.add(webview)

if __name__ == "__main__":
    ft.run(main)
