import forca
import advinhacao

print("*******************************")
print("*******Escolha seu jogo!*******")
print("*******************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if (jogo == 1):
    print('Forca')
elif (jogo == 2):
    advinhacao.jogar()