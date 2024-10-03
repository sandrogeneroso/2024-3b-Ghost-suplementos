import os

suplementos = [{'nome':'creatina', 'categoria':'saude', 'ativo':True},
             {'nome':'whey', 'categoria':'saude','ativo':True},
             {'nome':'pre treino', 'categoria':'saude','ativo':False},
             {'nome':'glutamina', 'categoria':'saude', 'ativo':True}]

def exbir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def mostra_titulo():
    print('''

    𝐺ℎ𝑜𝑠𝑡 𝑠𝑢𝑝𝑙𝑒𝑚𝑒𝑛𝑡𝑜𝑠

    ''')

    def mostra_escolhas():
    print('1. Cadastro de suplementos')
    print('2. Listar suplementos')
    print('3. Ativar suplementos')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_suplementos()
        elif opcao_escolhida == 2:
            mostrar_suplementos()
        elif opcao_escolhida == 3:
            print('Ativar/desativar suplementos')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_suplementos():
    exbir_subtitulo('Cadastrar suplementos')

    nome_suplemento = input('Digite o nome do suplemento: ')
    suplementos.append(nome_suplemento)/
    print(f'{nome_suplemento} foi adicionado(a) a loja 𝐺ℎ𝑜𝑠𝑡 𝑠𝑢𝑝𝑙𝑒𝑚𝑒𝑛𝑡𝑜𝑠')

    retorna_menu_principal()

def mostrar_nadadores():
    exbir_subtitulo('Listar suplementos')

    for suplemento in suplementos:
        nome_suplemento = suplemento['nome']
        categoria = suplemento['categoria']
        ativo = suplemento['ativo']
        print(f' - {nome_suplemento} | {categoria} | {ativo}')
    
    retorna_menu_principal()


def finalizar_programa():
    os.system('clear')
    print('Finalizando programa')

def opcao_invalida():
    print('Esse caracter não é permitido')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()