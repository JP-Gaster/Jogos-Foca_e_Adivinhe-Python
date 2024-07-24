def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')
    #Definir qual a palavra secreta
    palavra_secreta = "bolachoito"
    
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
            
        else:
            erros += 1
            
        enforcou = erros == 10
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você acertou!")
    else:
        print("Você errou!")
        
if(__name__ == "__main__"):
    jogar_forca()