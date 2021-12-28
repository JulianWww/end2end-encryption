import socket, rsa, requests
from end2end import communicator

txt = requests.get("http://wandhoven.ddns.net/code/testFiles/Shakespeare/aMidSummerNightsDream").content.decode()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 25900))
sock.listen()

other, addrs = sock.accept()

(pubkey, privkey) = rsa.newkeys(512)

c = communicator.Communicator(other, communicator.RSAEncoder(pubkey), communicator.RSADecoder(privkey))
data = c.recv().decode()
print(data==txt)
