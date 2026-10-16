def on_button_pressed_a():
    global opcion
    opcion = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
     global opcion
     opcion = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global opcion
    opcion = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

oscuridad = 0
lecturadeluz = 0
opcion = 0
opcion = 0

def on_forever():
    global lecturadeluz, oscuridad
    if opcion == 1:
        lecturadeluz = input.light_level()
        led.plot_bar_graph(lecturadeluz, 255)
    elif opcion == 2:
        lecturadeluz = input.light_level()
        oscuridad = 255 - lecturadeluz
        led.plot_bar_graph(oscuridad, 255)
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
