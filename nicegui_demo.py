from nicegui import ui

with ui.row().classes("mx-auto"):
    with ui.card():
        ui.label("Hello World! Making Changes").classes("text-2xl") # creates a base layer
        input_field = ui.input()
        button = ui.button("lowercase")
        result = ui.label()
ui.run()

