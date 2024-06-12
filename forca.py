def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')
    #Definir qual a palavra secreta
    palavra_secreta = "bolachoito"

    enforcou = False
    acertou = False

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        chute = input("Qual a letra?")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print("Jogando....")


    print("Fim de jogo!")
if(__name__ == "__main__"):
    jogar_forca()