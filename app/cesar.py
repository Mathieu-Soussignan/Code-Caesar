def chiffrement_cesar(texte, decalage):
    # Fonction de chiffrement
    resultat = []
    for caractere in texte:
        if caractere.isalpha():
            decalage_base = 65 if caractere.isupper() else 97
            nouvelle_lettre = chr((ord(caractere) - decalage_base + decalage) % 26 + decalage_base)
            resultat.append(nouvelle_lettre)
        else:
            resultat.append(caractere)
    return ''.join(resultat)

def dechiffrement_cesar(texte, decalage):
    # Fonction de déchiffrement
    return chiffrement_cesar(texte, -decalage)