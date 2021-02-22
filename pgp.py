import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
from pgpy import PGPKey, PGPMessage
key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)

# create private key. Note that the UID is blank
key.add_uid(pgpy.PGPUID.new(''), usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])

# password protect private key
key.protect("Password", SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)

# print private and public key
private_key = str(key)
public_key = str(key.pubkey)
print (private_key)
print(public_key)

# encrypt message using public key
message=pgpy.PGPMessage.new(" This is the message cleartext")
encryptedmessage = str(PGPKey.from_blob(public_key)[0].encrypt(message))
print(encryptedmessage)

## decrypt using private key
private_key = PGPKey.from_blob(private_key)[0] # reads in from string format
with private_key.unlock('Password') as unlocked_private_key :
    result = unlocked_private_key.decrypt(PGPMessage.from_blob(encryptedmessage))
##get cleartext  to a variable
plaintext = result.message
print(plaintext)