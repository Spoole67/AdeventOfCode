
import numpy as np

class Bincounter:

    def __init__(self, data):
        length = len(data)
        self.datalist = np.zeros(length, int)          # Create a numpy array with 0s

    def __str__(self):
        return str(print(self.datalist))

    def add(self, data_list):
        for i in range(len(data_list)):
            if data_list[i] == "1":
                self.datalist[i] += 1
            else:
                self.datalist[i] -= 1

    def to_bin(self):
        bin_number = ""
        for i in self.datalist:
            if i > 0:
                bin_number += "1"
            else:
                bin_number += "0"
        return bin_number

    def reverse(self):
        reversed_bin_str = ""
        for i in self.datalist:
            if i > 0:
                reversed_bin_str += "0"
            else:
                reversed_bin_str += "1"
        return reversed_bin_str


## --- Main ---------


with open("input_day3.txt", "r", encoding="utf-8") as file:
    first_row = file.readline()
    first_row_strip = first_row.strip()
    bin_objekt = Bincounter(list(first_row_strip))      # Skapar ett första objekt
    bin_objekt.add(list(first_row_strip))               # Läser av första raden också
    for row in file:
        stripped_row = row.strip()                      # Stripped row är en städad string
        number_list = list(stripped_row)                # En string lista
        bin_objekt.add(number_list)

print(bin_objekt)
bin_string = bin_objekt.to_bin()
bin_reverese = bin_objekt.reverse()
print(bin_string)
print(bin_reverese)
dec_int = int(bin_string,2)
print(dec_int)
dec_int_re = int(bin_reverese,2)
print(dec_int_re)
print(dec_int_re*dec_int)
