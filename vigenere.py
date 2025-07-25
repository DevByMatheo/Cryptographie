import string 


def creation_matrice():
    L = []
    for i in range(26):
        ligne =[]
        for j in range(26): 
            ligne.append(chr((i + j) % 26 + ord('A')))
        L.append(ligne)
    return L


def cryptage(msg, cle):
    matrice = creation_matrice()
    L = []
    for i in range(len(msg)):
        if msg[i] in string.ascii_letters:
            pos_letter_cle = ord(cle[i % len(cle)]) - ord('A')
            pos_letter_msg = ord(msg[i]) - ord('A')
            L.append(matrice[pos_letter_cle][pos_letter_msg])
        else:
            L.append(msg[i])
    return "".join(L)


def decryptage(msg, cle):
    matrice = creation_matrice()
    L = []
    for i in range(len(msg)):
        pos_cle = ord(cle[i % len(cle)]) - ord('A')
        if msg[i] in string.ascii_letters:
            pos_elt = ord(msg[i]) - ord('A')
            L.append(matrice[0][pos_elt - pos_cle])
        else:
            L.append(msg[i])
    return "".join(L)


def main():
    msg = input("Quel est votre message : ").upper()
    cle = input("Entrez une clée : ").upper()

    msg_crypte = cryptage(msg, cle)
    print("Le message crypté est : ", msg_crypte)
    print(f"Avec le code de Vigenère {msg_crypte} donne {decryptage(msg_crypte, cle)}")


main()