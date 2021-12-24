from menu import Menu
menu = Menu()
tentativas: int = 3

while tentativas != 0:
    senha = int(input('Digite sua senha para acessar: '))
    tentativas -= 1
    if senha != 123:
        print(f'senha errada você tem mais {tentativas} tentativas')
    else:
        print('senha correta')
        menu.escolher()
        break
else:
    print('limite total atingido')