#Crie um programa que recebe um texto e o repete 49 vezes, sendo 7 vezes dividas em 7 linhas.

#resolucao:
txt2 = input("Digite uma palavra: ")
i = 6
txt = [txt2]
print(txt)
for x in range(0,i,1):
    txt.append(txt2)
for x in range(0,i+1,1):
    print(txt)

#Crie uma função que substitui as vogais de uma palavra por símbolos especiais.

#resolucao
def trocar_vogais(arg):
    troca = {
        "a": "@",
        "e": "&",
        "i":"!",
        "o":"#",
        "u":"*"
    }
    txt = arg
    for x in troca:
        txt = txt.replace(x, troca[x])
    return txt
print(trocar_vogais('aeiou'))



