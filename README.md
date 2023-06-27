
<h1 align="center">
  <br>
<img src="https://cdn.discordapp.com/attachments/1122367085260062880/1123021349691068666/ensa_logo.png" alt="ENSA TANGER" width="200"></a>
  <br>
  <br>
 Travaux pratiques de la théorie de l'information
</h1>
<h3 align="center">	
Un travail de : Ayman Wadi 
<br>Encadré par : Mme Siham Massou.
</h3>

<p align="center"> <br>
	Ce répertoire contient mes codes Python pour l'apprentissage de la programmation avec Mme Massou. Vous y trouverez différents fichiers, tels que des scripts, des données, et des notes de cours. J'ai créé ce répertoire sur GitHub pour sauvegarder mes codes en toute sécurité et pour les partager avec d'autres développeurs. N'hésitez pas à me contacter pour toute question ou suggestion d'amélioration.
<br>
Merci de visiter mon répertoire GitHub !
<br>
Ceci est mon <a href="https://www.linkedin.com/in/ayman-wadi/" target="_blank">LinkedIn</a>.
</p>


<p align="center">
  <a>
	<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  </a>
  <a>
	<img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=green&labelColor=green">
  </a>
  <a>
	<img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)">
  </a>
  <a>
	<img src="https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white">
  </a>
</p>

<p align="center">
  <a href="#Introduction">Introduction</a>
	<br>
  <a href="#Arithmétique flottante">Arithmetique flottante</a> •
  <a href="#Hamming">Codage Hamming</a> •
  <a href="#Huffman">Codage Huffman</a> •
  <a href="#LZ78">Codage LZ78</a> •
  <a href="#Shannon Fano">Cadage Shannon Fano</a>
</p>

<p align="center">
<img  src="https://media.tenor.com/GfSX-u7VGM4AAAAC/coding.gif" alt="Coding">
</p>

## Introduction

<p>La théorie de l'information est une branche des mathématiques appliquées qui étudie la quantité d'information contenue dans des données et les méthodes de traitement, de transmission et de stockage de l'information. Elle a été développée par Claude Shannon en 1948, mais a des racines plus anciennes dans la théorie de la communication et la statistique.</p>
<p>La théorie de l'information traite de plusieurs concepts fondamentaux, notamment :
	
 - L'entropie : mesure de la quantité de désordre dans un système d'informations.
 - Le canal de communication : le moyen par lequel l'information est transmise d'un point à un autre, souvent soumis à des perturbations et des bruits.
 - Le codage de l'information : la représentation de l'information sous une forme qui peut être stockée, transmise et traitée efficacement.
</p>
<p>La théorie de l'information est utilisée dans de nombreux domaines, notamment la communication, la cryptographie, la compression de données, la reconnaissance de formes et l'apprentissage automatique. Elle est également utilisée dans des applications pratiques telles que la transmission de signaux sans fil, la compression de fichiers multimédias, la correction d'erreurs dans les transmissions numériques, etc.</p>
<p>En résumé, la théorie de l'information fournit un cadre mathématique pour comprendre et quantifier l'information, ce qui est essentiel pour la conception et l'optimisation de systèmes d'informations efficaces et fiables.</p>
<p align="center">
<img  src="https://cdn.discordapp.com/attachments/1122367085260062880/1123234277933465611/rsz_shannon-1200x630-1.jpg" alt="Coding"> <br>
<em> Claude Shannon avec une machine de codage trés développée en 1950 </em>
</p>
<br>
<br>
<br>

## Arithmétique flottante

En codage arithmétique, les caractères sont encodés en utilisant des intervalles. Le résultat de ce codage est un nombre réel compris entre 0 et 1, qui est construit en associant à chaque symbole une portion de l'intervalle [0, 1[ dont la taille est proportionnelle à la probabilité d'occurrence de ce symbole. L'ordre dans lequel les symboles sont associés à des portions de l'intervalle n'a pas d'importance, tant qu'il est le même pour le codage et le décodage.

L'algorithme du codage arithmétique flottante est le suivant :
```bash
Soit bornelnf ← 0.0
Soit borneSup ←	1.0
Tant que il y a des symboles à coder Faire
  C ← symbole à coder
  Soient x, y les bornes de l'intervalle correspondant à C dans la table
  taille ← borneSup — bornelnf;
  borneSup ← bornelnf + taille * y
  bornelnf ← bornelnf + taille * x
Fin Tant que
Retourner borneSup
```
Lien pour voir le code écrit en language Python : [Arithmétique.py](https://github.com/lord-avigi/theorie_de_information/blob/main/arithmetique.py)

 > **Remarque: **
> Ce codage est le plus simple à coder car son algorithme est direct . Cependant , il y a plusieurs variables à tapez . Le code permet la creation d'un tableau ayant 6 variables impérativement.


<br>

## Codage de Hamming

Le codage de Hamming est une technique de correction d'erreur qui utilise des bits de parité pour détecter et corriger les erreurs de transmission de données binaires. Les bits de parité sont ajoutés à la séquence de bits d'origine pour former une séquence de bits plus longue. Lorsque les données sont transmises, la séquence de bits est vérifiée pour détecter les erreurs et les bits de parité sont utilisés pour corriger l'erreur. Bien que largement utilisée, cette technique a une limite quant à la quantité d'erreurs qu'elle peut détecter et corriger, et l'ajout de bits de parité peut augmenter la taille de la séquence de bits.

L'algorithme du codage arithmétique flottante est le suivant :
```bash
msg ← message à envoyer
m ← longueur du message
r ← nombre de bits de correction
n ← longueur totale du message à envoyer (m + r)
code ← nouveau tableau de n bits initialisé à 0
puissance_deux ← 1
i ← 0
j ← 0

tant que (m + r + 1) > puissance_deux faire
    r ← r + 1
    puissance_deux ← 2^r - 1 - r

pour i allant de 1 à n faire
    si i est une puissance de 2 alors
        passer à l'itération suivante
    sinon
        code[i] ← bit j du message
        j ← j + 1

pour i allant de 0 à r - 1 faire
    xor_sum ← 0
    pour j allant de 1 à n faire
        si j & (2^i) == (2^i) alors
            xor_sum ← xor_sum xor code[j]
    code[2^i] ← xor_sum

retourner code Hamming
```
Lien pour voir le code écrit en language Python : [Arithmétique.py](https://github.com/lord-avigi/theorie_de_information/blob/main/arithmetique.py)

 > **Remarque: **
> Ce codage est moyennement difficile à coder car son algorithme utilise des calcul matricielle et plusieurs boucles . 


<br>

## Codage de Huffman

Le codage de Huffman est une technique de compression de données qui utilise des longueurs de code variables pour représenter des symboles. Les symboles les plus fréquents sont représentés par des codes plus courts, tandis que les symboles moins fréquents sont représentés par des codes plus longs. Cette technique permet de réduire la taille de la séquence de données en utilisant moins de bits pour représenter les symboles les plus fréquents. Le codage de Huffman est largement utilisé dans les systèmes de compression de fichiers et de transmission de données pour réduire la taille des données à transférer.

L'algorithme du codage de Huffman est le suivant :
```bash
frequence ← nouvelle table de frequence pour chaque symbole dans la séquence  ←
faire
    si le symbole n'est pas dans la table de frequence alors:
        ajouter le symbole à la table de frequence avec une fréquence de 1
    sinon
        incrémenter la fréquence du symbole dans la table de hachage

arbre ← nouvelle racine
pour chaque symbole et sa fréquence dans la table de frequence Faire
    ajouter un nœud feuille pour le symbole avec sa fréquence comme priorité dans la file de priorité
	tant que la taille de la file de priorité est supérieure à 1 faire
   	 nœud1 ← nœud ayant la plus petite priorité dans la file de priorité
   	 enlever nœud1 de la file de priorité
   	 nœud2 ← nœud ayant la deuxième plus petite priorité dans la file de priorité
   	 enlever nœud2 de la file de priorité
    fusion ← nouveau nœud pour la fusion des nœuds 1 et 2, avec une priorité égale à la somme des priorités de nœud1 et nœud2
    ajouter fusion à la file de priorité
racine ← nœud restant dans la file de priorité

codes ← nouvelle table de frequence Faire
    si nœud est une feuille alors
        ajouter le symbole et son code à la table des codes
    sinon
        assigner_codes(racine gauche de nœud, code + "0")
        assigner_codes(racine droit de nœud, code + "1")
assigner_codes(racine, "")

séquence_encodée ← ""
pour chaque symbole dans la séquence faire
    ajouter le code correspondant à la table des codes à la séquence encodée
```
Lien pour voir le code écrit en language Python : [Arithmétique.py](https://github.com/lord-avigi/theorie_de_information/blob/main/arithmetique.py)

 > **Remarque: **
> Ce codage est le plus compliqué , l'importation de plusieurs bibliothéque était une nécessité.


<br>

## Codage Lz78

Le codage LZ78 est un algorithme de compression de données sans perte qui utilise un dictionnaire pour stocker les séquences de symboles déjà rencontrées dans la séquence de données à compresser. L'idée de base est de remplacer les séquences de symboles répétitives par des références à leur première occurrence dans le dictionnaire, suivies du symbole suivant qui n'a pas encore été vu.

L'algorithme du codage Lz78  est le suivant :
```bash
dictionnaire ← dictionnaire vide
séquence_codée ← nouvelle liste de paires (index, symbole suivant)
préfixe ← ""
index ← 0

pour chaque symbole dans la séquence d'entrée Faire
    nouvelle_chaine ← préfixe + symbole
    si nouvelle_chaine est dans le dictionnaire :
        préfixe ← nouvelle_chaine
        index ← index de nouvelle_chaine dans le dictionnaire
    sinon
        ajouter la paire (index, symbole) à la séquence encodée
        ajouter nouvelle_chaine au dictionnaire avec un nouvel index
        préfixe ← ""
        index ← 0

si préfixe n'est pas vide :
    ajouter la paire (index, "") à la séquence codée

retourner séquence_codée

```
Lien pour voir le code écrit en language Python : [lz78.py](https://github.com/lord-avigi/theorie_de_information/blob/main/LZ78.py)

 > **Remarque: **
> Ce codage est simple car il utilise un dictionnaire et une seule condition.


<br>


## Codage de Shanon Fano

Le codage de Shannon-Fano est un algorithme de compression de données sans perte qui utilise des codes binaires de longueur variable pour représenter les symboles dans une séquence de données. L'algorithme a été développé par Claude Shannon et Robert Fano en 1949.

L'algorithme du codage Shannon Fano est le suivant :
```bash
séquence_symboles ← séquence de symboles à encoder
table_frequence ← table de fréquence des symboles dans la séquence
table_codes ← nouvelle table de hachage pour stocker les codes de chaque symbole

fonction diviser_grouper(symboles, début, fin)
    si début >= fin alors
        retourner
    sinon
        somme ← somme des fréquences des symboles entre les indices début et fin dans la table de fréquence
        moitié ← somme / 2
        somme_partielle ← 0
        index ← début
        tant que somme_partielle < moitié faire
            somme_partielle ← somme_partielle + fréquence[symboles[index]]
            index ← index + 1
        si index == début alors
            index ← index + 1
        pour i allant de début à index - 1 faire
            ajouter "0" au code du symbole[i] dans la table des codes
        pour i allant de index à fin faire
            ajouter "1" au code du symbole[i] dans la table des codes
        diviser_grouper(symboles, début, index - 1)
        diviser_grouper(symboles, index, fin)

diviser_grouper(séquence_symboles, 0, longueur(séquence_symboles) - 1)

retourner table_codes
```
Lien pour voir le code écrit en language Python : [shannon_fano.py](https://github.com/lord-avigi/theorie_de_information/blob/main/Shannon_Fano.py)

 > **Remarque: **
> Ce codage est légerement difficile car il utilise une boucle itérative.


---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)

