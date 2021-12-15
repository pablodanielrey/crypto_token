import os
import sys
import pkcs11


user_pin = os.environ.get('pkcs11_pin')
if not user_pin:
    sys.exit(1)

p = "/opt/CryptoIDEUser/x64/lib/linux/x64/libcryptoide_pkcs11.so"
cry = pkcs11.lib(p)
for slot in cry.get_slots(token_present=True):
    print(f'slot encontrado : {slot}')
    token = slot.get_token()
    print(f'usando : {token}')
    with token.open(user_pin=user_pin) as session:
        print(session)
