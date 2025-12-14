import flet as ft

def main(page: ft.Page):
    page.title = "Flet Mobile App"
    page.window_width = 400
    page.window_height = 800
    
    # Create main content
    greeting = ft.Text(
        "Teste ^v^",
        size=28,
        weight="bold",
    )
    
    description = ft.Text(
        "Esse é um app simples com flet.",
        size=16,
        color="gray600",
    )
    
    button = ft.ElevatedButton(
        text="Click Me!",
        on_click=lambda e: handle_button_click(page),
    )
    
    # Layout
    page.add(
        ft.Column(
            [
                greeting,
                description,
                button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


def handle_button_click(page: ft.Page):
    page.snack_bar = ft.SnackBar(ft.Text("Button clicked!"))
    page.snack_bar.open = True
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
