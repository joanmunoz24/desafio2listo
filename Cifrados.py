#Joan Muñoz
#Miguel Jaime
#Ignacio Jara


def rot_alpha(n):
    from string import ascii_uppercase as uc#obtiene las mayusculas
    #print("esto hace:"+uc[n:])
    lookup = str.maketrans(uc, uc[n:] + uc[:n])#Intercambia las letras 
    return lambda s: s.translate(lookup)#muerta el mensaje cambiado

def vigenere_encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext
def vigenere_decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext