input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    opcion = 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    opcion = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    opcion = 2
})
let oscuridad = 0
let lecturadeluz = 0
let opcion = 0
opcion = 0
basic.forever(function on_forever() {
    
    if (opcion == 1) {
        lecturadeluz = input.lightLevel()
        led.plotBarGraph(lecturadeluz, 255)
    } else if (opcion == 2) {
        lecturadeluz = input.lightLevel()
        oscuridad = 255 - lecturadeluz
        led.plotBarGraph(oscuridad, 255)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    
})
