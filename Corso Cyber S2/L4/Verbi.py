import http.client

host = input("Inserisci host/IP del sistema target: ")
port = input("Insert the target system door (default:80)")
path = input("Inserisci il percorso (default:'/): ")
if(port==""): port = 80
if(path==""): path = '/'
try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    if(response.status == 200 and response.status <= 299):
        print("I metodi abilitati sono:", response.getheaders("Allow"))
    else:
        print("Usa un metodo alternativo per determinare i verbi\n", response .status, "\n" ,response.getheaders())
    connection.close()
except ConnectionError:
    print("Connessione fallita", ConnectionError.strerror)