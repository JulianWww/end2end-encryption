import socket, requests
from end2end import createComunicator

data = requests.get("http://wandhoven.ddns.net/code/testFiles/Shakespeare/aMidSummerNightsDream").content

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 25900))



c = createComunicator(sock, 2048)
c.send(data)
