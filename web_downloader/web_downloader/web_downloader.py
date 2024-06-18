import reflex as rx
import asyncio
import web_downloader.app_pytube as tube
import os 

class ProcesoRuta(rx.State):
    link: str=""
    ruta: str=""
    def obtener_ruta(self,form_data:dict):
        dif_links=['youtu.be','www.youtube.com']
        self.link=form_data["input"]
        if any( dif_link in self.link for dif_link in dif_links):
            self.ruta=tube.download_mp3(self.link)



# Función para definir la página principal (index)
def index() -> rx.Component:
    # Devuelve un contenedor vertical que estructura toda la página
    return rx.vstack(
        # Header
        rx.hstack(
            # Texto de bienvenida en el header con estilo
            rx.text("Bienvenido a mi aplicación Reflex", font_size="24px", font_weight="bold"),
            justify="center",  # Centra el contenido horizontalmente
            align="center",  # Centra el contenido verticalmente
            width="100%",  # Ancho completo del contenedor
            padding_y="16px",  # Espaciado vertical de 16px
            bg="#f8f9fa",  # Color de fondo gris claro para el header
        ),
        # live_progress(),
        # Main Content with Form
        rx.vstack(
            # Formulario para ingresar el enlace
            rx.form(
                # Campo de entrada para el enlace
                rx.input(placeholder="Ingresa un enlace",name="input", id="link",  width="300px"),
                # Botón de envío del formulario
                rx.button("Enviar",type="submit", margin_left="8px"),
                on_submit=ProcesoRuta.obtener_ruta,
                # Estilo para centrar el formulario horizontal y verticalmente
                style={"display": "flex", "justify-content": "center", "align-items": "center"},
            ),
            justify="center",  # Centra el contenido horizontalmente
            align="center",  # Centra el contenido verticalmente
            width="100%",  # Ancho completo del contenedor
            padding_y="32px",  # Espaciado vertical de 32px
        )
        ,rx.text(ProcesoRuta.link)
        ,rx.text(rx.cond(ProcesoRuta.ruta !='',ProcesoRuta.ruta, 'link no correcto'))
        ,rx.button("Descargar MP3", on_click=DownloadState.download_file(ProcesoRuta.ruta))
        ,rx.text(os.getcwd())
        ,
        align="center",  # Centra todo el contenido de la página
        width="100%",  # Ancho completo de la página
        min_height="100vh",  # Altura mínima de la página para ocupar toda la ventana
        # Estilo para distribuir el contenido verticalmente y mantener el footer al fondo
        style={"display": "flex", "flexDirection": "column", "justifyContent": "space-between"}
        
    )




# async def index():
#     show_form = rx.Subject(initial_value=True)

#     async def submit_form():
#         # Aquí puedes realizar cualquier operación de envío de datos (simulada)
#         await asyncio.sleep(2)  # Simulación de operación de envío de datos
#         show_form.on_next(False)  # Ocultar el formulario después de enviar

#         # Iniciar el progreso después de enviar el formulario
#         await ProgressState.start_progress()

#     form = rx.stack(
#         rx.if_else(
#             show_form,
#             rx.div(
#                 rx.input(type="text", placeholder="Ingrese datos aquí"),
#                 rx.button("Enviar", on_click=submit_form),
#             ),
#             None,
#         ),
#         rx.progress(value=ProgressState.value).if_(lambda: not show_form),
#         width="50%",
#     )

#     return form



class DownloadState(rx.State):
    def download_file(self,ruta):
        # Aquí especificas la ruta al archivo MP3 que deseas que el usuario pueda descargar.
        # Asegúrate de que el archivo esté accesible en el servidor.
        return rx.download(url=ruta)

    # return rx.button(
    #     "Download",
    #     on_click=rx.download(
    #         url='/home/ignaciogovo/Pictures/Screenshots/mono_arana_informacion.jpg',
    #         filename="different_name_logo.jpg"
    #     ),
    #     id="download button"
    # )






class ProgressState(rx.State):
    value: int = 0
    ruta: str = ''
    @rx.background
    async def start_progress(self,ruta):
        rx.text(ruta["link"])
        async with self:
            self.value = 0
        while self.value < 100:
            await asyncio.sleep(0.1)
            async with self:
                self.value += 1


# def live_progress():
#     return rx.hstack(
#         rx.progress(value=ProgressState.value),
#         rx.button(
#             "Start", on_click=ProgressState.start_progress
#         ),
#         width="50%",
#     )




# Instancia la aplicación Reflex
app = rx.App()

# Agrega la página principal (index) a la aplicación
app.add_page(index)

# Ejecuta la aplicación Reflex
if __name__ == '__main__':
    app.run()





