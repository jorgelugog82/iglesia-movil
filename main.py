import flet as ft
import sys

def main(page: ft.Page):
    page.title = "Conector Iglesia"
    # Centramos vertical y horizontalmente los elementos para pantallas táctiles
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30

    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"

    # Función nativa móvil gatillada por acción del usuario
    def ejecutar_enlace(e):
        page.launch_url(url_servidor)
    # Diseñamos una tarjeta limpia que le indica al usuario qué hacer
    page.add(
        ft.Icon(ft.Icons.CHURCH_ROUNDED, size=80, color=ft.Colors.BLUE_900),
        ft.Text("Control de Salones", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ft.Text(
            "Conéctate en tiempo real al servidor central de la iglesia.",
            size=14,
            color=ft.Colors.GREY_600,
            text_align=ft.TextAlign.CENTER
        ),
        ft.Container(height=15),
        # Contenedor interactivo universal simulando un botón nativo
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.Icons.WIFI, color=ft.Colors.WHITE),
                ft.Text("CONECTAR AHORA", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            bgcolor=ft.Colors.BLUE_900,
            padding=15,
            border_radius=10,
            width=260,
            on_click=ejecutar_enlace  # Gatilla la apertura autorizada por Android
        )
    )

# Sintaxis de arranque nativa oficial para empaquetadores Android modernos
if __name__ == "__main__":
    ft.run(main)
