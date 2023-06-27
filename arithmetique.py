precision = int(input('Tapez le nombre de chiffre aprés la virgule à utiliser : '))
a1 = float(input('Tapez la borne inférieure de l\'intervalle contenant A: '))
a2 = float(input('Tapez la borne supérieure de l\'intervalle contenant A: '))
b1 = float(input('Tapez la borne inférieure de l\'intervalle contenant B: '))
b2 = float(input('Tapez la borne supérieure de l\'intervalle contenant B: '))
c1 = float(input('Tapez la borne inférieure de l\'intervalle contenant C: '))
c2 = float(input('Tapez la borne supérieure de l\'intervalle contenant C: '))
d1 = float(input('Tapez la borne inférieure de l\'intervalle contenant D: '))
d2 = float(input('Tapez la borne supérieure de l\'intervalle contenant D: '))
e1 = float(input('Tapez la borne inférieure de l\'intervalle contenant E: '))
e2 = float(input('Tapez la borne supérieure de l\'intervalle contenant E: '))
f1 = float(input('Tapez la borne inférieure de l\'intervalle contenant F: '))
f2 = float(input('Tapez la borne supérieure de l\'intervalle contenant F: '))

message = input('Tapez votre message à coder: ')
liste = []
for char in message:
    liste.append(char)
nombre = len(liste)

Binf = 0
Bsup = 1
i, x, y = 0, 0, 0
for i in range(0, nombre):
    if liste[i] == 'A':
        x, y = a1, a2
    elif liste[i] == "B":
        x, y = b1, b2
    elif liste[i] == "C":
        x, y = c1, c2
    elif liste[i] == "D":
        x, y = d1, d2
    elif liste[i] == "E":
        x, y = e1, e2
    elif liste[i] == "F":
        x, y = f1, f2
    else:
        print('Charactère introuvable dans le tableau.')
        print('Vérifie que le message est écrit en majuscule puis réessayez.')
    taille = Bsup - Binf
    Bsup = Binf + (taille * y)
    Binf = Binf + (taille * x)
Affichage = round(Bsup, precision)
print('Le codage Arithmétique flottante donne ce chiffre: ', Affichage)
