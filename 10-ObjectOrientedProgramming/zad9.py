class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
    def show_status(self):
        if self.is_on:
            print("Tv is on, channel",self.channel_no)
            
        else:
            print("Tv is off")
        

tv=TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.turn_off()
tv.show_status()

