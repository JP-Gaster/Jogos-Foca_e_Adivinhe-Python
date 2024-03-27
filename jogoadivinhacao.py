import random;

print('*************************************')
print('* Bem Vindo, ao JOGO DE ADIVINHAÇÃO *')
print('*************************************')

#Definindo o número secreto

numero_secreto = round(random.random()*100)
rodada = 1
#Definindo o número de tentativas
numero_tentativas = 8

while(rodada <= numero_tentativas):
    print('Tentativa ', rodada,'de ', numero_tentativas, 'tentativas restantes')

#Recebendo o chute do jogador
    chute_string = input('Digite um número entre 1 e 100: ')
    chute = int(chute_string)

#Declarando as condições
    if (numero_secreto == chute):
        print('ヅ Você ACERTOU!!! ヅ')
        break
    elif(chute < numero_secreto):
        print('Você errou! O número secreto é um número maior')
    else:
        print('Você errou! O número secreto é um número menor')
    rodada = rodada +1