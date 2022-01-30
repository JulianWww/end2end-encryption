import rsa

def getIntSize(i):
    return (i.bit_length() + 7) // 8

def pubkeyToBin(key):
    out = bytearray()
    out += getIntSize(key.n).to_bytes(4, "little")
    out += key.n.to_bytes(getIntSize(key.n), "little")
    out += key.e.to_bytes(getIntSize(key.e), "little")
    return out

def pubkeyFromBin(data):
    n_size = int.from_bytes(data[:4] , "little") + 4
    n = int.from_bytes(data[4:n_size], "little")
    e = int.from_bytes(data[n_size:] , "little")
    return rsa.PublicKey(n, e)
