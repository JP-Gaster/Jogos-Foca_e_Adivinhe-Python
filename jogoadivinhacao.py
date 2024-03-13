print('*************************************')
print('* Bem Vindo, ao JODO DE ADIVINHAÇÃO *')
print('*************************************')

#Definindo o número secreto
numero_secreto = 6

#Definindo o número de tentativas
numero_tentativas = 3

while(numero_tentativas > 0):
    print('Tentativa, ' numero_tentativas)

#Recebendo o chute do jogador
    chute_string = input('Digite seu número: ')
    print('**** Você  digitou o número *', chute_string)
    chute = int(chute_string)

#Declarando as condições
if numero_secreto == chute_string:
    print('Você acertou!')
elif(chute <numero_secreto):
    print('Você errou! O número secreto é um número menor')
else:
    print('Você errou! O número secreto é um número maior')