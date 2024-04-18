import random;

print('*************************************')
print('* Bem Vindo, ao JOGO DE ADIVINHAÇÃO *')
print('*************************************')

#Definindo o número secreto

numero_secreto = random.randrange(1,101)
rodada = 1

print('Qual o nível de dificuldade?')
print('(1)-Fácil, (2)-Médio, (3)-Difícil, (4)-Hardcore, (5)-Nightmare, (6)-Perfection')

nivel = int(input('Defina o nível: '))

#Definindo o número de tentativas
if(nivel == 1):
    numero_tentativas = 24
elif(nivel == 2):
    numero_tentativas = 18
elif(nivel == 3):
    numero_tentativas = 12
elif(nivel == 4):
    numero_tentativas = 6
elif(nivel == 5):
    numero_tentativas = 3
else:
    numero_tentativas = 1

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