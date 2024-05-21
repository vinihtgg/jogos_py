def jogar():

    print("*******************************")
    print("Bem vindo ao Jogo de Forca")
    print("*******************************")
    
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    acertou = False
    enforcou = False
    erros = 0
    
    print(letras_acertadas)
    
    while(not acertou and not enforcou):
        letra_chute = input("Qual letra?")
        letra_chute = letra_chute.strip().upper()
        
        if (letra_chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra_chute == letra):
                    letras_acertadas[index] = letra    
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    
if (__name__ == "__main__"):
    jogar()