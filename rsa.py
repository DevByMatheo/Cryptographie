import secrets
import random


def pgcd(x, y):
    """
    Calcul du plus grand diviseur commun de x et y
    """
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y
    
    for i in range(y//2, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


def est_premier(nb):
    """
    Test de primalité de Miller-Rabin
    nb -> nb à tester
    s -> nombre de fois ou on peut diviser nb-1 par 2
    d -> partie impair de nb -1
    a -> base aléatoire entre 2 et nb-2
    x = a^d mod nb
    """
    s = 0
    d = nb - 1

    if nb == 0:
        return False
    
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(40):
        a = random.randrange(2, nb - 1)
        x = pow(a, d, nb)  # x = a^d mod nb

        if x == 1 or x == nb - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, nb)
            if x == nb - 1:
                break
        else:
            return False 

    return True 


def gen_premier(bits):
    """
    Généré un nombre premier
    """
    nb = secrets.randbits(bits) | 1 # Forcer à l'impair
    while not est_premier(nb):
        nb = secrets.randbits(bits) | 1
    return nb


def generate_key_4096():
    """
    p & q -> deux nombres premiers
    n -> modulus : nombre premier ou n = p * q
    phi -> indicateur d Euler de n
    e -> exposant public
    d -> exposant privé : inverse modulaire de e modulo φ(n)
    """
    p = secrets.randbits(2048)
    q = secrets.randbits(2048)
    n = q * p
    phi = (p-1)*(q-1)
    e = 65537
    d = 0
    while pgcd(e, phi*n) != 1:
        e += 1

    # Calcul du d

    return (n,e), (n,d)


def encodage(msg):
    """
    Encode le message via ASCII
    """
    encodage_msg = ""
    for elt in msg:
        encodage_msg += f"{ord(elt):03}"
    return int(encodage_msg)


def main():
    msg = input("Quel est votre message : ")
    print(encodage(msg))

    
main()