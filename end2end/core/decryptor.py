import rsa
from end2end.core.rsaHandler import RSAHandler


class DummyDecoder():
    def decrypt(self, data):
        return data

class RSADecoder(RSAHandler, DummyDecoder):
    def __init__(self, key):
        super(RSADecoder, self).__init__(key)

    def decrypt(self, data):
        size = self.getMaxDecryptSize()
        data = [data[idx:idx+size] for idx in range(0, len(data), size)]
        data = [rsa.decrypt(segment, self.key) for segment in data]
        return bytearray().join(data)

if __name__ == "__main__":
    (pubkey, privkey) = rsa.newkeys(512)
    d = RSADecoder(privkey)
