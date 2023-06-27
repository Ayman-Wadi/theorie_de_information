# Définiton de la classe du noeud
class node:
    def __init__(self) -> None:
        self.symbole = ''
        self.dictionnaire = [0] * 100
        self.probabilite= 0.0
        self.top = 0
p = [node() for _ in range(100)]

def tri(n, p):
# Définiton de la fonction de tri qui classe les probabilités par ordre décroissant.
    temp = node()
    for j in range(1, n):
        for i in range(n - 1):
            if ((p[i].probabilite) > (p[i + 1].probabilite)):
                temp.probabilite= p[i].probabilite
                temp.symbole= p[i].symbole

                p[i].probabilite= p[i + 1].probabilite
                p[i].symbole= p[i + 1].symbole

                p[i + 1].probabilite= temp.probabilite
                p[i + 1].symbole= temp.symbole

def shannon(l, h, p):
# Définiton des principes du codage de shannon qui attribue 0 en haut et 1 en bas
    pack1, pack2, diff1, diff2 = 0, 0, 0, 0
    if ((l + 1) == h or l == h or l > h):
        if (l == h or l > h):
            return
        p[h].top += 1
        p[h].dictionnaire[(p[h].top)] = 0
        p[l].top += 1
        p[l].dictionnaire[(p[l].top)] = 1
        return
    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].probabilite
        pack2 = pack2 + p[h].probabilite
        diff1 = pack1 - pack2
        if (diff1 < 0):
            diff1 = diff1 * -1
        j = 2
        while (j != h - l + 1):
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].probabilite
            for i in range(h, k, -1):
                pack2 = pack2 + p[i].probabilite
            diff2 = pack1 - pack2
            if (diff2 < 0):
                diff2 = diff2 * -1
            if (diff2 >= diff1):
                break
            diff1 = diff2
            j += 1
        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].dictionnaire[(p[i].top)] = 1
        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].dictionnaire[(p[i].top)] = 0
        shannon(l, k, p)
        shannon(k + 1, h, p)

# # Définiton de la fonction qui affiche le résultat du codage de Shannon par dictionnaire
def display(n, p):
    print("\nL'application du codage de Shannon Fano donne le résultat suivant':\n", end='')
    print("\nSymbole\t\t\tProbabilité\t\t\tCode Binaire", end='')
    for i in range(n-1, -1, -1):
        print("\n  ", p[i].symbole, "\t\t\t   ", p[i].probabilite, " \t\t\t\t", end='')
        for j in range(p[i].top + 1):
            print(p[i].dictionnaire[j], end='')

# Code main
if __name__ == '__main__':
    total=0
    n = int(input("Entrez le nombre de symboles : "))
    p = [node() for _ in range(n)]
    for i in range(n):
        sym = input("Entrez le symbole {} : ".format(i + 1))
        pro = float(input("Entrez la probabilité de {} : ".format(sym)))
        p[i].symbole = sym
        p[i].probabilite = pro
        total += pro
    if total != 1:
        print("La somme des probabilités n'est pas égale à 1. Les données tapées sont incorrectes.")
    tri(n, p)
    for i in range(n):
        p[i].top = -1
    shannon(0, n - 1, p)
    display(n, p)
