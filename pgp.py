import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm

from pgpy.constants import PubKeyAlgorithm
key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
str(key)
key.add_uid(pgpy.PGPUID.new(''), usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])
key.protect("C0rrectPassphr@se", SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)

print(key)

## hamkey = "-----BEGIN PGP PUBLIC KEY BLOCK-----xsFNBGAa1hkBEACaUGGIbt9okkUe1fsK3PgnvmRYjhCVfjnrI8YccWvOKR1tBmzwtnlAHK/0L2/D8bVTjmDsq5zG4sOXFXvf8wm8mCkFJctYzQjuTipFgd6yY4IczKmJ9jkzvcebIbstLzCPgP3uaO+TCfgSvUU4kf2I2ME2dC5VK2yTCXT7PYNqAshWMZLLMLzdqrtkT1eV3mdt9vVoUuUDZRaFJ9BC8YIgNYyt6AZc+J5JSfge4P7msHKYldLp2gW8OJbeTSux1bmXpGAvzowQjlYI8+Mpg2dZFWyFaCbPhlUlnD1rKDIrQVl69KzVAnHucga/8Kd9IN0TumxNO4zmSdUxblxhjBcymfk0XkLBuigSF0+HBjsmtwUxcVsZptt2MwD2+kdSL+Dv6ez2UlW1tuEU6vEp73Elo22i0FcVDOoZNVRVWcRVYKeNXPrzmk9fdyMNvCWMBK8lFsdFM9XeywNczPyA6cv8/J7bDTio2xkVdA++9v2hnIoP/nyW772kUhyS17qlLkYvIahnKgW3jRKHRksUJF9qAgvxAG/nM27u7bMieH3A3j5RBkku1R6l2hwL3QgaVqTZ8uvIc/zVpordpbfEatRWe/eUyoIxLlrXUqAHnrdoQyRWIae/XLBt9CbEe9jueWLOh57obelAzrHwzt0A66hSFl0L2QOe0VxxLdd13FcA3QARAQAB=c/go-----END PGP PUBLIC KEY BLOCK-----"
m=pgpy.PGPMessage.new("weezy yeezy jeezy")

mcrypted = key.pubkey.encrypt(m)
print(mcrypted)
print("that was encrypted mssg")

key.unlock("C0rrectPassphr@se")

cleartxt = mcrypted.decrypt('C0rrectPassphr@se')
print(cleartxt)
print("that was decrypted mssg")