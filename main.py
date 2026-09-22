import webbrowser
import time
import sys

def main():
    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Forzamos a Android a abrir el panel de salones directamente en Google Chrome/Safari
    webbrowser.open(url_servidor)

if __name__ == "__main__":
    # Pausa de un segundo para asegurar que los servicios de red del celular respondan
    time.sleep(1)
    main()
    # Forzamos el cierre del conector invisible para no gastar batería en el celular
    sys.exit(0)
