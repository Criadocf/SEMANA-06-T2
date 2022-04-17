# Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”,
#“número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e
# outro como “símbolo”

def ler(x):
    if x in ('a','e','i','o','u'):
        return 'vogal'
    elif x in ('0','1','2','3','4','5','6','7','8','9'):
        return 'número'
    elif x in ('a','b','c','d','f','g','h','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','y','w'):
        return 'consoante'
    else:
        return 'símbolo'
    
cara = input() .lower()

ch = ler(cara)

print(ch)