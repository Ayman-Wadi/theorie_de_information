def codageLZ78(message):
    dictionnaire = {"" : 0}
    phrase = ""
    code = {}
    index = 1
    for character in message:
        pc = phrase + character
        if pc in dictionnaire:
            phrase = pc
        else:
            code[index] = (dictionnaire[phrase], character)
            dictionnaire[pc] = index
            index += 1
            phrase = ""
    if phrase != "":
        code[index] = (dictionnaire[phrase], "")
    return code

message = input('Tapez le message à coder: ')
code = codageLZ78(message)
print('Le dictionnaire LZ78 établi est le suivant: ')
for index, value in code.items():
    print(index,": (",value[0],",",value[1],")")
