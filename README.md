# end2end-encryption
The end2end encryption module implements end to end encryption for python. The module is designed for sockets.
## installation
The package can be installed using pip:
```
$ pip install end2end
```

## basic usage
The encryption uses a `communicator` that encrypts, decrypts and handles the key exchange. The Communicator can be created with a socket `sock` and the size of the key `key_size` the client uses. 
```
com = end2end.createComunicator(sock, key_size)
``` 
a full simple mock-up of the server can be found in the `test.py` and `test2.py` files.
