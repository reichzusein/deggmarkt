basic.show_icon(IconNames.HEART)

def on_forever():
    basic.show_string("Hello ozgur !")
basic.forever(on_forever)

def on_forever2():
    basic.show_number(4)
basic.forever(on_forever2)
