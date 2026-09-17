import flet as ft

def main(page: ft.Page):
    page.title = "Salones Iglesia - Conector"
    
    # IP del Servidor Central de tu iglesia (tu PC)
    IP_SERVIDOR = "192.168.0.111" 
    PUERTO = "8550"
    url_servidor = f"http://{IP_SERVIDOR}:{PUERTO}"
    
    # Función que se ejecuta apenas abre la app
    def abrir_sistema(e):
        page.launch_url(url_servidor)
        # Cerramos la app de apoyo para no consumir batería
        page.window.close()

    # Diseñamos una interfaz limpia con un botón de acceso directo
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Icon(ft.Icons.CHURCH_ROUNDED, size=80, color=ft.Colors.BLUE_900),
                ft.Text("Sistema de Salones", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text("Presiona el botón para conectar con el servidor central de la PC", size=14, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                ft.Container(height=20),
                ft.Button(
                    "Conectar al Servidor",
                    icon=ft.Icons.V_PAD_ROUNDED,
                    on_click=abrir_sistema,
                    width=280,
                    style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_900)
                )
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center,
            padding=40,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.run(main)
