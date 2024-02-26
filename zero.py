numero_determinador = 0

chute_string = input('Digite o seu número')

print('Você digitou o número', chute_string)

chute = int(chute_string)

if numero_determinador == chute_string:
    print('O número que você digitou é igual a zero')
elif(chute>numero_determinador):
    print('O número que você digitou é positivo')
else:
    print('O número que você digitou é negativo')