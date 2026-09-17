import flet as ft
import time

def main(page: ft.Page):
    page.title = "Conector Iglesia"
    
    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Ordena a Android abrir de forma inmediata Google Chrome o el navegador nativo
    page.launch_url(url_servidor)
    
    # Le damos 3 segundos al teléfono para procesar la apertura de la página
    time.sleep(3)
    page.window_close()
# Cierre del archivo usando el formato obligatorio del empaquetador de Android
if __name__ == "__main__":
    ft.app(target=main)
