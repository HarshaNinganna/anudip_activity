class KannadaFilm:
    film = ""
    Director = ""
    Hero = ""
    def status(self):
        if self.name == "Kantara Chapter 1":
            return "Blockbuster"
        elif self.name == "Martin":
            return "Flop"
f1 = KannadaFilm()
f1.name = "Kantara Chapter 1"
f1.director = "Rishab shetty"
f2 = KannadaFilm()
f2.name = "Martin"
f2.director = "AP Arjun"

print(f1.status())
    
