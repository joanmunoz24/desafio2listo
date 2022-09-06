#Joan Muñoz
#Miguel Jaime
#Ignacio Jara


import requests
import Cifrados as deci
import json

def obtenermensaje():
    headers = {
        'Content-Type': 'text/plain',
    }
    response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)

    return response.json()["msg"]

def enviarmensaje(mensaje):
    headers = {
        'Content-Type': 'text/plain',
    }
    data = {"msg":mensaje}
        
    response = requests.post('https://finis.mmae.cl/SendMsg', headers=headers, data=json.dumps(data))
    
    return response

def desafio1():
    #Proceso de cifrado
    mensaje_entrada="hola mundo"
    rot_8=deci.rot_alpha(8)(mensaje_entrada.upper())
    password="heropassword"
    vige=deci.vigenere_encrypt(rot_8,password.upper())
    rot_12=deci.rot_alpha(12)(vige)
    print("Mensaje cifrado")
    print(rot_12)
    print("\n")
    enviarmensaje(rot_12)
    # print(enviarmensaje(rot_12).text)
    #Proceso de descifrado
    rot12=deci.rot_alpha(-12)(rot_12)
    vige1=deci.vigenere_decrypt(rot12,password.upper())
    rot8=deci.rot_alpha(-8)(vige1)
    print("Mensaje cifrado enviado al servidor")
    print(rot8)
    print("\n")


def desafio2():
    mensaje_servidor=obtenermensaje()
    rotpr=deci.rot_alpha(-12)(mensaje_servidor.upper())
    password = "finispasswd"
    vigenere1 = deci.vigenere_decrypt(rotpr,password.upper())
    rot_8 = deci.rot_alpha(-8)(vigenere1)
    print("Mensaje descrifado que proviene del servidor" + "")
    print(rot_8)
    
def main():
    desafio1()
    desafio2()

if __name__ == "__main__":
    main()