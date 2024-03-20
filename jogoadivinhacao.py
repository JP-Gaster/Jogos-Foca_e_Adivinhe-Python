print('*************************************')
print('* Bem Vindo, ao JOGO DE ADIVINHAÇÃO *')
print('*************************************')

#Definindo o número secreto
import random
numero_secreto = int(random.random()*100)
rodada = 1
#Definindo o número de tentativas
numero_tentativas = 3

while(rodada <= numero_tentativas):
    print('Tentativa ', rodada,'de ', numero_tentativas, 'tentativas restantes')

#Recebendo o chute do jogador
    chute_string = input('Digite seu número: ')
    chute = int(chute_string)

#Declarando as condições
    if (numero_secreto == chute):
        print('Você acertou!')
        break
    elif(chute < numero_secreto):
        print('Você errou! O número secreto é um número menor')
    else:
        print('Você errou! O número secreto é um número maior')
    rodada = rodada +1