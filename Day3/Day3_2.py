# Skapa en Numpy 2D array eller en PD dataframe och sedan börja sortera dessa två!

import numpy as np

# Open file and add it to a numpy array
with open("input_day3.txt", "r", encoding="utf-8") as file:
    first_row = file.readline()             # läser in först raden
    first_row_strip = first_row.strip()     # strippar
    string_list = list(first_row_strip)     # gör en lista för alla siffror
    # Konvertera till en int lista
    int_list = [int(i) for i in string_list]    # Convert to int list
    array = np.array([int_list])            # Create first numpy array
    print(array)
    # Keep adding all values to a 2D array!
    for row in file:
        row_s = row.strip()
        list_s = list(row_s)
        list_i = [int(i) for i in list_s]
        array = np.append(array,[list_i], axis = 0)

array_copy = array # Skapa kopia för andra for slingan

for i in range(len(array.T)):
    extract_data = array[:,i]       # extract the data from row i
    # Kolla om det finns flest ettor(1) eller nollor(0)
    # remove_int sätts till motsatt värde
    if np.bincount(extract_data)[1] >= np.bincount(extract_data)[0]:
        remove_int = 0
    else:
        remove_int = 1
    array = array[(array[:, [i]] != remove_int).any(1)]
    # remove in the i:th row all of that value
    print(f"---{i}-----{remove_int}--------------")
    print(array)

# convert remaning numpy array to a str
bin_str = ""
for number in array[0]:
    bin_str += str(number)
print(bin_str)
first_dec = int(bin_str,2)
print(first_dec)

# ---------------- Nedan är en kopia av koden men vi byter bara på 0 och 1 ----------
for i in range(len(array_copy.T)-3):
    extract_data_copy = array_copy[:,i]       # extract the data from row i
    # Kolla om det finns flest ettor(1) eller nollor(0)
    # remove_int sätts till motsatt värde
    # behåller den det är minst av
    if np.bincount(extract_data_copy)[1] >= np.bincount(extract_data_copy)[0]:
        remove_int = 1
    else:
        remove_int = 0
    array_copy = array_copy[(array_copy[:, [i]] != remove_int).any(1)]             # remove in the i:th row all of that value
    print(f"---{i}-----{remove_int}--------------")
    print(array_copy)

# convert remaning numpy array to a str
bin_str_copy = ""

for number in array_copy[0]:
    bin_str_copy += str(number)
print(bin_str_copy)
first_dec_copy = int(bin_str_copy,2)
print(first_dec_copy)

print(first_dec_copy*first_dec)



# Gå igenom kod - skriv med funktioner --> Snygga till!