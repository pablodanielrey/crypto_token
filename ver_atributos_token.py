import os
import sys
import pkcs11
from pkcs11 import KeyType, ObjectClass, Mechanism


user_pin = os.environ.get('pkcs11_pin')
if not user_pin:
    sys.exit(1)

p = "/opt/CryptoIDEUser/x64/lib/linux/x64/libcryptoide_pkcs11.so"
cry = pkcs11.lib(p)
print('libreria inicializada')
for slot in cry.get_slots(token_present=True):
    print(f'slot encontrado : {slot}')
    token = slot.get_token()
    print(token)
    print(token.label)
    print(token.flags)