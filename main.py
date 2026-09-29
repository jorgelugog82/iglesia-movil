import webbrowser
import time
import sys

def main():
    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Ordena de forma nativa e inmediata a Android abrir el navegador predeterminado
    webbrowser.open(url_servidor)

if __name__ == "__main__":
    # Pausa de un segundo para garantizar la inicialización de los servicios de red del móvil
    time.sleep(1)
    main()
    # Forzamos la salida limpia para que no consuma batería de fondo en el celular
    sys.exit(0)
