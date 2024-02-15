print('*************************************')
print('* Bem Vindo, ao JODO DE ADIVINHAÇÃO *')
print('*************************************')

numeroSecreto = 6

chute = input('Digite seu número')

print('**** Você  digitou o número *', chute )

if numeroSecreto == chute:
    print('Você acertou!')

else:
    print('Você errou!')