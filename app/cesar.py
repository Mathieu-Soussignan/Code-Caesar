import unidecode

def chiffrement_cesar(texte, decalage):
    # Utilisation de unidecode pour supprimer les accents
    texte = unidecode.unidecode(texte)
    resultat = []
    for caractere in texte:
        if caractere.isalpha():  # Si c'est une lettre
            decalage_base = 65 if caractere.isupper() else 97
            nouvelle_lettre = chr((ord(caractere) - decalage_base + decalage) % 26 + decalage_base)
            resultat.append(nouvelle_lettre)
        else:
            resultat.append(caractere)
    return ''.join(resultat)

def dechiffrement_cesar(texte, decalage):
    return chiffrement_cesar(texte, -decalage)

# Pour tester / éxécuter dans le terminal
# if __name__ == "__main__":
#     choix = input("Tapez C pour chiffrer ou D pour déchiffrer : ").strip().upper()
#     texte = input("Entrez le texte : ")
#     decalage = int(input("Entrez le décalage : "))

#     if choix == 'C':
#         print("Texte chiffré : ", chiffrement_cesar(texte, decalage))
#     elif choix == 'D':
#         print("Texte déchiffré : ", dechiffrement_cesar(texte, decalage))
#     else:
#         print("Choix non valide. Veuillez entrer C ou D.")