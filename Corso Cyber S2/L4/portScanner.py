import socket as so

target = input("inserisci l'indirizzo da scansionare: ")
portrange = input("Inserisci porta minima\n e porta massima min-max es [5-200]")

lport = int(portrange.split('-')[0])
hport = int(portrange.split('-')[1])

print = ("Scansione in corso di", target, "dalla porta", lport, "alla porta", hport)
closed = []
for port in range(lport, hport+1):
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    status = s.connect_ex((target, port))
    
    if(status == 0):
        print('*** Porta', port, '-APERTA ***')
    else:
        closed.append(port)

if(len(closed) > 0):
    yesno=input(f"Trovate {len(port)} aperte, le vuoi visualizzare (s/n)? ")
    if(yesno.lower()) .startswith("s"):
        print(f"Porte chiuse: {closed}")
s.close()
