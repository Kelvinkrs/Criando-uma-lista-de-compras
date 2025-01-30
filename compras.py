import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indices = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indices)
            del lista[indice]
        except ValueError:
            print('Por favor insira um número inteiro')
        except IndexError:
            print('Índice inexistente')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada pra listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha "i", "a" ou "l"')
