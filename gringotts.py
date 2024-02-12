class Gringotts:
    def __init__(self, knuts=0, sickles=0, galleons=0):
        self.knuts = knuts
        self.sickles = sickles
        self.galleons = galleons
        self.convert()


    def __str__(self):
        return f"{self.knuts} Knuts, {self.sickles} Sickles, {self.galleons} Galleons."


    def convert(self):
        self.sickles += self.knuts // 29
        self.knuts %= 29
        self.galleons += self.sickles // 17
        self.sickles %= 17


    def add_knuts(self, n):
        self.knuts += n
        self.convert()

    def add_sickles(self, n):
        self.sickles += n
        self.convert()

    def add_galleons(self, n):
        self.galleons += n


gringotts = Gringotts()
gringotts.add_knuts(0)
gringotts.add_sickles(0)
gringotts.add_galleons(0)

print(gringotts)