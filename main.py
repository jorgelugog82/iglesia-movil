import webbrowser
import time

def main():
    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Forzamos a Android a abrir el panel de salones directamente en su navegador nativo
    webbrowser.open(url_servidor)
# Modificado para que actúe de manera independiente a los módulos visuales móviles de Flet
if __name__ == "__main__":
    # Agregamos una pausa de un segundo para asegurar que los servicios de red del celular respondan
    time.sleep(1)
    main()
