szamok = []

for i in range(7):
    szam = int(input(f"Add meg a(z) {i + 1}. számot: "))
    szamok.append(szam)

pozitiv = sum(1 for x in szamok if x > 0)
negativ = sum(1 for x in szamok if x < 0)

print(f"\nBeírt számok: {szamok}")
print(f"Pozitív számok száma: {pozitiv}")
print(f"Negatív számok száma: {negativ}")
print(f"Legnagyobb szám: {max(szamok)}")
print(f"Legkisebb szám: {min(szamok)}")