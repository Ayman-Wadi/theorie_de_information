msg = input('Tapez votre message à coder: ')
k = len(msg)
if k == 4:
    n = 7
elif k == 5:
    n = 9
elif k == 6:
    n = 10
elif k == 7:
    n = 11
elif k == 8:
    n = 12
elif k == 9:
    n = 13
elif k == 10:
    n = 14
elif k == 11:
    n = 15
elif k == 12:
    n = 17
elif k == 13:
    n = 18
elif k == 14:
    n = 19
elif k == 15:
    n = 20
else:
    print('Message plus long que 15 bits , pas encore codé.')

r = 0
while 2 ** r < n:
    r += 1
print('Le nombre total de bits de correction à ajouter est', r, '. La taille totale du bloc à envoyer est alors', n ,'.')

code = [0] * n
j = 0
for i in range(n):
    if i + 1 not in [2 ** k for k in range(r)]:
        code[i] = int(msg[j])
        j += 1

for i in range(r):
    parity_bit = 0
    for j in range(n):
        if ((j + 1) >> i) & 1:
            parity_bit ^= code[j]
    code[2 ** i - 1] = parity_bit
code_str = ''.join([str(bit) for bit in code])

print("Le bloc envoyé en utilisant le code de Hamming est le suivant: ", code_str)
