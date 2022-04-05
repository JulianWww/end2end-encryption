import rsa
from end2end.core.keys import getIntSize


class RSAHandler():
    def __init__(self, key):
        super(RSAHandler, self).__init__()

        self.key = key

    def getMaxEncryptSize(self):
        return self.getMaxDecryptSize() - 11

    def getMaxDecryptSize(self):
        return getIntSize(self.key.n)
