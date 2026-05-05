fogyasztas = int(input("Adja meg az autója fogyasztását 100km-en:"))
urtartalom = int(input("Adja meg a tank űrtartalmát: "))
tavolsag = int(input("Mennyi távot akar megtenni:"))

ut = (urtartalom/fogyasztas)*100
print(f"AEnnyi utat tud megtenni: {ut}")

if tavolsag > ut:
    print("Tankolnunk kell.")

else:
    print("Nem kell tankolnunk odaérünk.")


