import flet as ft
import sys
import os

# Usamos la estructura básica de Flet sin agregar botones ni cajas para evitar fallos de diseño
def main(page: ft.Page):
    page.title = "Conector Iglesia"
    
    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # CORREGIDO: Usamos la función nativa de Flet para ordenar a Android abrir Chrome/Safari
    page.launch_url(url_servidor)
    import time
    # Mantenemos la aplicación abierta 3 segundos para darle tiempo a Android de procesar el enlace
    time.sleep(3)
    page.window.close()

# Punto de arranque compatible con el empaquetador móvil actual
if __name__ == "__main__":
    ft.app(target=main)
