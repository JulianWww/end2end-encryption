from .core.decryptor import DummyDecoder, RSADecoder
from .core.encryptor import DummyEncoder, RSAEncoder
from .core.keys import pubkeyToBin, pubkeyFromBin
from rsa import newkeys


class Communicator():
    def __init__(self, sock, encoder, decoder):
        self.sock = sock
        self.encoder = encoder
        self.decoder = decoder

        key = self.encoder.key
        self._send(pubkeyToBin(key))

        self.encoder.key = pubkeyFromBin(self._recv())
    
    def _send(self, data):
        self.sock.send(int.to_bytes(len(data), 4, "little"))
        self.sock.send(data)
    
    def _recv(self):
        size =  int.from_bytes(self.sock.recv(4), "little")
        return self.sock.recv(size)
    
    def send(self, data):
        data = self.encoder.encrypt(data)
        self._send(data)
    
    def recv(self):
        data = self._recv()
        return self.decoder.decrypt(data)


def createComunicator(sock, keySize):
    (pubkey, privkey) = newkeys(keySize)
    return Communicator(sock, RSAEncoder(pubkey), RSADecoder(privkey))
