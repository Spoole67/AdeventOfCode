
# Vad är det för kod!

class Submarine:

    def __init__(self, aim, hori):
        self.hori = hori
        self.aim = aim
        self.depth = 0

    def __str__(self):
        return print(f"Djupet är {self.depth} och längden är {self.hori}.")

    def mult(self):
        return self.depth * self.hori

    def mult_2(self):
        return self.depth * self.hori

    # down, forward or up
    # increase the values of these to the object
    def add(self, direction, value):
        if direction == "forward":
            self.hori += value
            self.depth += (self.aim*value)
        elif direction == "up":
            self.aim -= value
        elif direction == "down":
            self.aim += value



# Create object
# Main
sub = Submarine(0,0)
with open("input_Day2.txt", "r", encoding = "utf-8") as file:
    for row in file:
        row_stripped = row.strip()
        row_list = row_stripped.split(" ")
        sub.add(row_list[0], int(row_list[1]))
        #

print(sub.mult_2())

print("test")

