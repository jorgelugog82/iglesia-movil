import flet as ft

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

    def abrir_sistema_interno(e):
        # web_view=True le ordena a Flet abrir la IP de la PC de forma incrustada
        # ocupando el 100% de la pantalla adentro de la misma app de la iglesia.
        page.launch_url(url_servidor, web_view=True)

    # Botón compatible con la versión estable 0.22.0
    btn_conectar = ft.ElevatedButton(
        text="INGRESAR AL SISTEMA",
        icon=ft.icons.CHURCH,
        on_click=abrir_sistema_interno,
        width=280,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_900,
        )
    )

    page.add(
        ft.Icon(ft.icons.CHURCH_ROUNDED, size=80, color=ft.colors.BLUE_900),
        ft.Text("Control de Salones", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
        ft.Text(
            "Aplicación oficial de control de espacios físicos de la congregación.",
            size=14,
            color=ft.colors.GREY_600,
            text_align=ft.TextAlign.CENTER
        ),
        ft.Container(height=20),
        btn_conectar
    )

if __name__ == "__main__":
    ft.app(target=main)
