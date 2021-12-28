import rsa


(pubkey, privkey) = rsa.newkeys(512)

print(pubkey)
