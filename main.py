import flet as ft
import time

def main(page: ft.Page):
    page.title = "Salones Iglesia"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30

    # Dirección IP local de tu PC Servidor Central
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"

    # Componente visual temporal que evita que Android congele la pantalla blanca
    barra_progreso = ft.ProgressBar(width=250, color=ft.colors.BLUE_900, visible=True)
    texto_espera = ft.Text("Conectando al Servidor de la Iglesia...", size=14, color=ft.colors.GREY_600)

    page.add(
        ft.Icon(ft.icons.CHURCH_ROUNDED, size=80, color=ft.Colors.BLUE_900),
        ft.Text("Control de Salones", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ft.Container(height=20),
        texto_espera,
        ft.Container(height=10),
        barra_progreso
    )
    page.update()

    # Pausa milimétrica de seguridad para activar las antenas del celular
    time.sleep(1)

    try:
        # 'web_view=True' obliga a Android a cargar el sistema adentro de la misma app
        # de la iglesia en pantalla completa, de forma nativa y sin abrir Google Chrome.
        page.launch_url(url_servidor, web_view=True)
    except Exception:
        texto_espera.value = "Error de conexión. Verifica el Wi-Fi."
        barra_progreso.visible = False
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
