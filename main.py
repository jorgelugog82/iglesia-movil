import flet as ft
import sys
import os

def main(page: ft.Page):
    page.title = "Salones Iglesia - Conector"
    
    # Dirección IP local del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Función que redirige al navegador del teléfono celular apuntando a la PC
    def abrir_sistema(e):
        page.launch_url(url_servidor)
        page.window.close()
    # Contenedor interactivo universal. Simula un botón perfecto usando texto centrado.
    boton_fijo_universal = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.WIFI, color=ft.Colors.WHITE),
            ft.Text("Conectar al Servidor", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD, size=16)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
        bgcolor=ft.Colors.BLUE_900,
        padding=15,
        border_radius=10,
        width=280,
        on_click=abrir_sistema  # Hace que toda la caja azul sea presionable
    )

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.CHURCH_ROUNDED, size=80, color=ft.Colors.BLUE_900),
                ft.Text("Sistema de Salones", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text("Presiona el botón para conectar con el servidor central de la PC", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                ft.Container(height=25),
                boton_fijo_universal
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            padding=40,
            expand=True
        )
    )

# CORREGIDO: Reemplazado ft.run(main) por ft.app(target=main) exigido por Flet 0.86.5+
if __name__ == "__main__":
    ft.app(target=main)
