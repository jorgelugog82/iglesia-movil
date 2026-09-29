import flet as ft
import os
import sys

def main(page: ft.Page):
    page.title = "Control de Salones"
    # Eliminamos márgenes y barras para que use toda la pantalla del teléfono
    page.padding = 0  
    page.theme_mode = ft.ThemeMode.LIGHT

    # Dirección IP local de tu PC Servidor Central
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    # Al usar ft.WebView directo (en lugar de launch_url), Flet crea un cascarón 
    # de ventana limpia que incrusta el sistema de la iglesia de forma 100% nativa.
    visor_web = ft.WebView(
        url=url_servidor,
        expand=True
    )

    page.add(visor_web)

if __name__ == "__main__":
    ft.app(target=main)
