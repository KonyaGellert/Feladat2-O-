class SzamStatisztika:
    def __init__(self, szamok):
        self.szamok = szamok

    def legnagyobb(self):
        return max(self.szamok)

    def legkisebb(self):
        return min(self.szamok)

    def median(self):
        rendezett = sorted(self.szamok)
        n = len(rendezett)
        if n % 2 == 1:
            return rendezett[n // 2]
        else:
            kozepso1 = rendezett[n // 2 - 1]
            kozepso2 = rendezett[n // 2]
            return (kozepso1 + kozepso2) / 2

    def paros_paratlan(self):
        paros = sum(1 for x in self.szamok if x % 2 == 0)
        paratlan = len(self.szamok) - paros
        return paros, paratlan

# 7 szám bekérése
szamok = []
for i in range(7):
    szam = int(input(f"Add meg a(z) {i + 1}. számot: "))
    szamok.append(szam)

# Példányosítás
statisztika = SzamStatisztika(szamok)

# Eredmények kiírása
print("\nStatisztika:")
print(f"Számok: {szamok}")
print(f"Legnagyobb szám: {statisztika.legnagyobb()}")
print(f"Legkisebb szám: {statisztika.legkisebb()}")
print(f"Medián: {statisztika.median()}")
paros, paratlan = statisztika.paros_paratlan()
print(f"Páros számok: {paros}")
print(f"Páratlan számok: {paratlan}")