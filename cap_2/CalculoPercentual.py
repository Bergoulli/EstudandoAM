n = int(input('Digite a quantidade de números que quer: '))
p = float(input('Digite em percentual (entre 0 e 1) o quanto quer: '))

valores = []
for i in range(n):
    valor = float(input(f'Digite o {i+1}º valor: '))
    valores.append(valor)

valores.sort()  # ordena a lista
posicao = n * p  # posição proporcional

if posicao % 1 != 0:  # se não for número inteiro
    posicao = round(posicao)
    print(f'O valor correspondente é: {valores[posicao]}')
else:
    posicao = int(posicao)
    media = (valores[posicao] + valores[posicao + 1]) / 2
    print(media)
