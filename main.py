import os
import sys
import time
import webbrowser

# Parcha de manera inmediata el entorno para enseñarle a Android dónde buscar los certificados
try:
    import certifi
    os.environ["SSL_CERT_FILE"] = certifi.where()
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
except Exception:
    pass
def conectar_servidor():
    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Ordena a Android abrir el panel de salones directamente en Google Chrome/Safari
    webbrowser.open(url_servidor)

if __name__ == "__main__":
    # Pausa de un segundo para dar tiempo a que los servicios del celular se despierten
    time.sleep(1)
    conectar_servidor()
    # Cierra el disparador de fondo de forma limpia
    sys.exit(0)
