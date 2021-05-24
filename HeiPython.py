pituus = float(input("Mikä on pituutesi (cm): "))
paino = float(input("Miten paljon painat (kg): "))

PIndeksi = paino / (pituus/100)**2

print(f"Painoindeksisi on {PIndeksi}")

if PIndeksi <=  25:
    print("Et (vielä) ole ylipainoinen.")
else:
    print("Aika lähteä lenkille!") 

#in addition to lesson material, I was inspired by https://www.youtube.com/watch?v=kqtD5dpn9C8 , and w3 schools
