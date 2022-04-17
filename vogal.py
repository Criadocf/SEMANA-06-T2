# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for
#uma VOGAL ou o valor booleano False (falso) caso contrário.

def ler(x):
    if x in ('A','E','I','O','U'):
        return 'True'
    else:
        return 'False'
    
vog = input() .upper()

ch = ler(vog)

print(ch)