def cryptage(msg):
    L = []
    for elt in msg:
        L.append(chr(ord(elt) + 1) if elt.isalpha() else elt)
    return "".join(L)
    

def decryptage(msg):
    L = []
    for elt in msg:
        L.append(chr(ord(elt) - 1) if elt.isalpha() else elt)
    return "".join(L)


def main():
    msg = input("Quel est votre message : ")
    msg_crypte = cryptage(msg)
    print("Le message crypté est : ", msg_crypte)
    print(f"Avec le code de César {msg_crypte} donne {decryptage(msg_crypte)}")
    

main()