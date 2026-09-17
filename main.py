import flet as ft
import sys
import os

def main(page: ft.Page):
    page.title = "Salones Iglesia - Conector"
    
    # IP del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Función que abre el navegador del celular apuntando a la PC
    def abrir_sistema(e):
        page.launch_url(url_servidor)
        # Cierra la pequeña app conector de apoyo para no gastar recursos
        page.window.close()

    # CORREGIDO: Usamos ft.Icons.WIFI que es un icono nativo universal garantizado
    btn_conectar = ft.Button(
        text="Conectar al Servidor",
        icon=ft.Icons.WIFI,
        on_click=abrir_sistema,
        width=280,
        style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_900)
    )

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.CHURCH_ROUNDED, size=80, color=ft.Colors.BLUE_900),
                ft.Text("Sistema de Salones", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text("Presiona el botón para conectar con el servidor central de la PC", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                ft.Container(height=20),
                btn_conectar
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            padding=40,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.run(main)
