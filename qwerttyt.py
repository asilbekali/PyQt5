class Talaba:
    def __init__(self, name, bahosi):
        self.name = name
        self.bahosi = bahosi

    def __repr__(self):
        return self.name + " " + str(self.bahosi)

    def __gt__(self, other):
        return self.bahosi > other.bahosi

    def __lt__(self, other):
        return self.bahosi < other.bahosi

m = Talaba("Vali", 5)
n = Talaba("Ali", 10)

lst = [m, n]
lst.sort(key=lambda x: x.bahosi)
print(lst)
