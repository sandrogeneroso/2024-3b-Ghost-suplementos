import os

def mostra_titulo():
    print('''
        
    𝐺ℎ𝑜𝑠𝑡 𝑠𝑢𝑝𝑙𝑒𝑚𝑒𝑛𝑡𝑜𝑠

    ''')

def mostra_escolhas():
    print('1. cadastro de suplementos')
    print('2. listar suplementos')
    print('3. ativar suplementos')
    print('4. sair da aplicação')

def escolha_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print('você escolheu a opção: ',opcao_escolhida)

    def finalizar_programa():
        os.system('cls')
        print('finalizar programa')


    if opcao_escolhida==1:
        print('cadastrar suplementos')
    elif opcao_escolhida==2:
        print('listar suplementos')
    elif opcao_escolhida==3:
        print('ativar/desativar suplementos')
    else:
        finalizar_programa()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolha_opcao()

if __name__ =='__main__':
     main()

