#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
#estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
#que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
#João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Insira o peso em kg do total da sua pesca: '))

excesso = peso - 50
multa = 4.00 * excesso

if peso > 50.9:
    print(f'Atenção, a sua carga excedeu {excesso:.1f}kg do limite! Você deverá pagar uma multa de R${multa:.2f}')
else:
    print('O peso está dentro do regulamento e não haverá a aplicação de multas')