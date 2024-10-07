# Projet Chiffrement César

Ce projet implémente le chiffrement et déchiffrement de César avec prise en compte des majuscules, minuscules, espaces et caractères spéciaux (accents inclus).

## Description

Le chiffrement de César est un algorithme de cryptographie simple basé sur le décalage des lettres de l'alphabet. Ce projet permet de chiffrer et déchiffrer des textes tout en gérant les caractères spéciaux et les accents en français.

## Fonctionnalités

- Chiffrement d'un texte avec un décalage donné.
- Déchiffrement d'un texte chiffré avec le même décalage.
- Gestion des majuscules, minuscules, espaces, ponctuation et caractères accentués.
- Interface graphique avec Streamlit pour une utilisation interactive.
- Téléchargement du résultat chiffré/déchiffré sous forme de fichier texte.

## Installation

### Prérequis

Assurez-vous d'avoir Python installé sur votre machine.

### Étapes

1. Clonez le dépôt :

    ```bash
    git clone <URL_DU_DEPOT>
    ```

2. Installez les dépendances nécessaires :

    ```bash
    pip install -r requirements.txt
    ```

3. Exécutez les tests unitaires avec `pytest` :

    ```bash
    pytest
    ```

## Utilisation

### Utilisation dans le terminal

Vous pouvez utiliser les fonctions de chiffrement et déchiffrement dans le terminal. Exécutez simplement le script Python :

```bash
python app/cesar.py
```
L'application vous demandera d'entrer le texte à chiffrer ou déchiffrer, ainsi que le décalage souhaité.

## Utilisation avec Streamlit

### Pour une interface graphique interactive, utilisez Streamlit :

Exécutez l'application Streamlit :

```bash
streamlit run app_streamlit.py
```
Une interface web s'ouvrira dans votre navigateur où vous pourrez entrer le texte à chiffrer ou déchiffrer, choisir le décalage, et télécharger le résultat sous forme de fichier texte.

## Téléchargement des résultats

L'application Streamlit permet également de télécharger le texte chiffré ou déchiffré sous forme de fichier .txt. Après avoir exécuté l'opération (chiffrement ou déchiffrement), un bouton vous permet de télécharger le résultat.

## Personnalisation du thème

Le projet utilise un thème personnalisé pour l'interface Streamlit. Vous pouvez ajuster les couleurs et les polices en modifiant le fichier .streamlit/config.toml.

## Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration ou des fonctionnalités à ajouter, n'hésitez pas à soumettre une pull request.

## Auteurs

- Mathieu Soussignan.
