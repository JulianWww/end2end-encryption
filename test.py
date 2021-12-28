import socket, rsa, requests
from end2end import communicator

data = requests.get("http://wandhoven.ddns.net/code/testFiles/Shakespeare/aMidSummerNightsDream").content

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 25900))
(pubkey, privkey) = rsa.newkeys(512)

c = communicator.Communicator(sock, communicator.RSAEncoder(pubkey), communicator.RSADecoder(privkey))
c.send(data)
