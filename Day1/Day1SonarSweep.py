

"""
def readfile_and_count():
    with open("input.txt", "r", encoding="utf-8") as file:
        counter = 0
        minne = 1000                        # Välj ett stort minne som överskrivs.
        for line in file:
            tal_rad = line.strip()          # Städa lite
            tal = int(tal_rad)
            if tal > minne:
                counter += 1;

            minne = tal                     # Spara talet som ett minne så det går att jämföra

    return counter

antal = readfile_and_count()
print(antal)
"""



def readfile_and_count_two():
    # Ska addera de tre första värdena och spara dessa!
    with open("input.txt", "r", encoding="utf-8") as file:
        counter = 0
        value_list = []
        for line in file:
            tal_rad = line.strip()          # Städa lite
            tal = int(tal_rad)
            if len(value_list) == 3:
                value_list.pop(0)           # plockar bort första element
                value_list.append(tal)      # append lägger till längst bak
                summa = sum(value_list)     # Beräkna summa av list
                if summa > minne:
                    counter +=1;            # Addera 1 om ny summa är större än förra
                minne = summa
            else:                           # Om vi inte har tre element behöver vi lägga till fler
                value_list.append(tal)
                if len(value_list) == 3:        # Beräknar summan första gången vi går in
                    minne = sum(value_list)

    return counter
print(readfile_and_count_two())

