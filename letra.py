#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for
# uma LETRA (vogal ou consoante) ou o valor booleano False (falso) caso contrário.

def let(x):
    if x in('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z','Y','W'):
        return 'True'
    else:
        return 'False'
    
letra = input() .upper()

ch = let(letra)

print(ch)