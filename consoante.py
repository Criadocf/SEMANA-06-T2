#Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for
#uma CONSOANTE ou o valor booleano False (falso) caso contrário.

def ler(x):
    if x in('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y'):
        return 'True'
    else:
        return 'False'
    
val = input() .lower()

ch = ler(val)

print(ch)