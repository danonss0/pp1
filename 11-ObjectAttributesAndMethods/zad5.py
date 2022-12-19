class Music():
    
    def __init__(self, artist,track_title,album,year):
        self.artist = artist
        self.track_title = track_title 
        self.album = album 
        self.year = year
    
    def __str__(self):
        return "Performer: "+self.artist + "\nSong:      "+self.track_title + "\nAlbum:     "+ self.album + "\nYear:      "+self.year
    
song1 = Music('Ed Sheeran','Hearts Don\'t Break Around Here','Divide','2017')
song2 = Music('Shed Eeran','Here Around Break Don\'t Hearts','Edive','2015')
song3 = Music('Ted Ranshee','Hearts Break Around Here','Multiply','2011')
print(song1)
print(song2)
print(song3)
