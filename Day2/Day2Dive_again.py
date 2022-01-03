
# Vad är det för kod!

class Submarie:

    def __init__(self, data):
        self.depth = None
        self.hori = None

    def __str__(self):
        return print(f"Djupet är {self.depth} och längden är {self.hori}.")

    def multiplicate(self):
        return self.depth * self.hori


