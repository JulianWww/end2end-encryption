import rsa
from end2end.core.rsaHandler import RSAHandler


class DummyEncoder():
    def encrypt(self, data):
        return data

class RSAEncoder(DummyEncoder, RSAHandler):
    def __init__(self, key):
        super(RSAEncoder, self).__init__(key)

    def encrypt(self, data):
        size = self.getMaxEncryptSize()
        data = [data[idx:idx+size] for idx in range(0, len(data), size)]
        encrypted = [rsa.encrypt(segment, self.key) for segment in data]
        return bytearray().join(encrypted)


if __name__ == "__main__":
    (pubkey, privkey) = rsa.newkeys(512)
    r = RSAEncoder(pubkey)
