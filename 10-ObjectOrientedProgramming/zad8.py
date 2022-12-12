class TV():
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print("Tv is on")
        else:
            print("Tv is off")

tv=TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.turn_off()
tv.show_status()