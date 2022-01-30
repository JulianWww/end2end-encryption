import socket, requests
from end2end import createComunicator

txt = requests.get("http://wandhoven.ddns.net/code/testFiles/Shakespeare/aMidSummerNightsDream").content.decode()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 25900))
sock.listen()
other, addrs = sock.accept()

c = createComunicator(sock, 1024)
data = c.recv().decode()
print(data==txt)
