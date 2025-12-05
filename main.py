import flet as ft
import flet_core.types 

def main(page: ft.Page):
    # 1. Função que será chamada após a câmera/seleção ser fechada
    def on_camera_result(e: ft.FilePickerResultEvent):
        if e.files:
            # Pega o caminho do arquivo selecionado/capturado
            caminho_arquivo = e.files[0].path
            page.add(ft.Text(f"Foto capturada/selecionada em: {caminho_arquivo}"))
            # Agora você pode usar este caminho para exibir a imagem (ft.Image)
            # ou fazer o upload (file_picker.upload())

    # 2. Cria a instância do FilePicker
    file_picker = ft.FilePicker(on_result=on_camera_result)

    # Adiciona o FilePicker à página
    page.overlay.append(file_picker)
    page.update()

    def abrir_camera(e):
        file_picker.pick_files(
            allow_multiple=False,  # Queremos apenas uma foto
            allowed_extensions=['jpg', 'jpeg', 'png'],
            file_type=ft.FilePickerFileType.IMAGE,  # Crucial: Restringe a imagens
            # Isso fará com que o Android/iOS ofereça a opção de Câmera/Galeria
            dialog_title="Tirar foto ou selecionar imagem"
        )

    page.add(
        ft.ElevatedButton("Abrir Câmera / Galeria", on_click=abrir_camera)
    )

ft.app(target=main)