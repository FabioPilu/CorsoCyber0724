import math

def calcola_perimetro_quadrato(lato):
    return 4 * lato
def calcola_perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)
def calcola_perimetro_cerchio(raggio):
    return 2 * math.pi * raggio

print("Ciao! \nSono qui per aiutari con il calcolo di alcuni perimetri")
print("Scegli quale dei seguenti perimetri vuoi calcolare: ")
print("1. Quadrato")
print("2. Rettangolo")
print("3. Cerchio")

scelta = input("Inserisci il numero della forma voluta (1,2,3): ")

if scelta == '1':
    lato = float(input("Inserisci quanto è lungo il lato del quadrato: "))
    perimetro = calcola_perimetro_quadrato(lato)
    print(f"Il perimetro del tuo quadrato è di {perimetro}.")
elif scelta =='2':
    base = float(input("Inserisci il primo lato del tuo rettangolo: "))
    altezza = float(input("Inserisci il secondo lato del tuo rettangolo: "))
    perimetro = calcola_perimetro_rettangolo(base, altezza)
    print(f"Il perimetro del rettangolo con base {base} e altezza {altezza}")
elif scelta == '3':
    raggio = float(input("Inserisci il raggio del tuo cerchio: "))
    perimetro =calcola_perimetro_cerchio(raggio)
    print(f"Il perimetro del tuo cerchio con raggio {raggio} è {perimetro:.2f}")
else:
    print("Sono stato chiaro quando ho chiesto quale delle 3 opzioni potevi scegliere... \n1\n2\n3\nDai,riprova ;)")