from nicegui import ui

ui.colors(
      primary='#13189e', # changed the colors to have more contrast and aesthetics
      secondary='#e5e848',
      accent='#9b7da1',
      positive='#10dee6',
      negative='#917175',
      info='#d60202',
      warning='#b50d20'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: sets the color of the answer to positive color (in ui.colors).
        
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: sets the color of the text to negative color (in ui.colors)

def convert_slider():
    try:
        temp = float(temp_slider.value)  # read slider value
        converted_value = (temp * 9/5) + 32  # celcius to Fahrenheit Convert
        slider_result_label.set_text(f"{temp}°C = {converted_value:.2f}°F")
        slider_result_label.classes("text-lg font-semibold text-positive mt-4")
    except ValueError:
        slider_result_label.set_text("Invalid slider value.")
        slider_result_label.classes("text-lg font-semibold text-negative mt-4")

with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: set the padding of 1.5 rem on all sides
        # shadow-xl: sets a large drop shadow, making the card stand-out
        # mx-auto: centers the card horizontally by applying margin
        # mt-10: adds a top margin of 2.5 rem
        # rounded-xl: gives the card extra rounded corners
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: sets the size of the text to extra large
        # font-bold: sets the text to bold 
        # text-accent: sets the color from ui.colors to bold.
        # mb-4: adds a bottom margin of 1 rem, creating space from below. 
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: makes the input take the full available length
        # border: adds a border around the input
        # rounded: rounds the corners of the input
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: sets the color of the text to white.
        # py-2: adds a vertical padding of 0.5 rem
        # px-4: adds a horizontal padding of 0.5 rem
        result_label = ui.label("").classes("text-lg mt-4")
        
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):       
        ui.label("Celsius to Fahrenheit Slider").classes("text-2xl font-bold text-accent mb-4") 
        ui.label("Slide to select temperature (-50 °C to 100 °C):").classes("mb-2 text-lg font-semibold") 

        temp_slider = ui.slider(min=-50, max=100, value=0, step=1).props('track-color="accent" thumb-color="primary"') 
        temp_slider.on('change', convert_slider)

        slider_result_label = ui.label("").classes("text-lg mt-4")

ui.run()