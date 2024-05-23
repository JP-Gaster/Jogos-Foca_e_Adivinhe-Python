import forca
import jogoadivinhacao

print('*************************************')
print('******** Escolha o seu Jogo! ********')
print('*************************************')

print('(1)-Forca (2)-Adivinhação')

jogo = int(input('Qual é o Jogo?'))


if(jogo == 1):
    print('Jogando jogo da Forca')
    forca.jogar_forca()
else:
    print('Jogando jogo da Adivinhação')
    jogoadivinhacao.jogar_adivinhhacao()