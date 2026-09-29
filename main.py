import os
import sys
import time
import webbrowser

# Inicializa de forma inmediata la ruta de certificados nativa de Android
try:
    import certifi
    os.environ["SSL_CERT_FILE"] = certifi.where()
    os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
except Exception:
    pass
def conectar_servidor():
    # Dirección IP local de tu PC Servidor Central
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Ordena a Android abrir el panel de salones directamente en Google Chrome/Safari
    webbrowser.open(url_servidor)

if __name__ == "__main__":
    # Pausa de seguridad para permitir que los servicios de red del celular respondan
    time.sleep(1)
    conectar_servidor()
    # Forzamos la salida limpia para que no consuma batería de fondo
    sys.exit(0)
