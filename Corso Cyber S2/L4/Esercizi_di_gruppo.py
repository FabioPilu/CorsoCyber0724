numero=int(input("Inserisci numro per il calcolo fattoriale: "))
fattoriale = numero
for n in range(1, numero):
    fattoriale = fattoriale * n

    print(f"Il fattoriale di {numero} è {fattoriale}")