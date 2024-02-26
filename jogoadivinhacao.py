print('*************************************')
print('* Bem Vindo, ao JODO DE ADIVINHAÇÃO *')
print('*************************************')

numero_secreto = 6

chute_string = input('Digite seu número')

print('**** Você  digitou o número *', chute_string)

chute = int(chute_string)

if numero_secreto == chute_string:
    print('Você acertou!')
elif(chute>numero_secreto):
    print('Você errou! O número secreto é um número menor')
else:
    print('Você errou! O número secreto é um número maior')