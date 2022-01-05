# Läsa in filen
# Spara första två rader som en lista

# skapa ett objekt class bingoruta
# Instance variable är en 2d array
# lägg till alla objekt i en lista

# Itererar igenom en lista genom att apllicera metod "bingo?"
# "Bingo?" kollar om det siffran fiins i detta objekts 2d array


class Bingobricka:

    def __init__(self, array):
        self.bricka = array
        self.copy = array

    def __str__(self):
        # skriv en dubbel for loop som skriver ut snyggt
        pass

    def add_number(self):
        # Om siffra finns replace med 0
        pass

    def check_bingo(self):
        # kolla om det finns fem nollor i rad eller kolumn
        # Om detta finns så ska vi in och plocka ut denna raden
        pass



# ---------- Main -------------
with open("input_Day4.txt", "r", encoding="utf-8") as file:
    row = file.readline()           # Plockar ut första listan
    row_s = row.strip()
    drag_lista = [int(i) for i in row_s.split(",")]         # Skapar int drag lista

    for row in file:            # kollar så vi fortfarande har rader + plockar ut första raden
        #rad = file.readline()   # Plockar ut tom rad
        print(f"första raden är {row}")
        counter = 0
        while counter < 5:
            siffer_rad = file.readline()
            siffer_rad_s = siffer_rad.strip()
            # Skapa en tom numpy array
            # Lägg in alla dessa fem i denna array
            try:
                fem_rads_lista = [int(j) for j in siffer_rad_s.split(" ")]
            except ValueError:  # Hanterar fel när siffra är ental och ej tiotal
                fem_rads_lista_str = siffer_rad_s.split(" ")
                while "" in fem_rads_lista_str:
                    fem_rads_lista_str.remove("")
                fem_rads_lista = [int(j) for j in fem_rads_lista_str]
            counter += 1
        counter = 0




    for i in range(5):
        pass