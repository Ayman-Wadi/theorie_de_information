import heapq
from heapq import heappop, heappush

def isLeaf(root):
    return root.left is None and root.right is None

class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def codage(root, s, huffman_code):
    if root is None:
        return
    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'
    codage(root.left, s + '0', huffman_code)
    codage(root.right, s + '1', huffman_code)
def arbre_huffman(text):
    if len(text) == 0:
        return
    freq = {i: text.count(i) for i in set(text)}

    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)
    while len(pq) != 1:
        left = heappop(pq)
        right = heappop(pq)
        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))
    root = pq[0]
    huffmanCode = {}
    codage(root, '', huffmanCode)
    # imprime les codes Huffman
    print('Les codes de Huffman sont les suivants :', huffmanCode)
    s = ''
    for c in text:
        s += huffmanCode.get(c)
    print('Le message original \"', text,'" devient après le codage de Huffman :', s)

if __name__ == '__main__':
    text = input('Tapez le message que vous voulez codez : ')
    arbre_huffman(text)
