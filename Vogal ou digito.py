# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for
# uma letra (vogal ou consoante) ou um dígito (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso
# contrário.

def ler(x):
    if x in ('a','b','c','d','e','f','g','h','i','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z','y','w','0','1','2','3','4','5','6','7','8','9'):
        return 'True'
    else:
        return 'False'
        
cara = input() .lower()

ch = ler(cara)

print(ch)