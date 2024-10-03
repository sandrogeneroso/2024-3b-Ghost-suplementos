import os

suplementos = [
    {'nome': 'creatina', 'categoria': 'saude', 'ativo': True},
    {'nome': 'whey', 'categoria': 'saude', 'ativo': True},
    {'nome': 'pre treino', 'categoria': 'saude', 'ativo': False},
    {'nome': 'glutamina', 'categoria': 'saude', 'ativo': True}
]

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')  # Para compatibilidade com Windows e Linux
    print(texto)
    print('')

def retorna_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def mostra_titulo():
    print('''

    𝐺ℎ𝑜𝑠𝑡 𝑠𝑢𝑝𝑙𝑒𝑚𝑒𝑛𝑡𝑜𝑠

    ''')

def mostra_escolhas():
    print('1. Cadastro de suplementos')
    print('2. Listar suplementos')
    print('3. Ativar/desativar suplementos')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção:', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_suplementos()
        elif opcao_escolhida == 2:
            mostrar_suplementos()
        elif opcao_escolhida == 3:
            ativar_desativar_suplementos()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def cadastrar_suplementos():
    exibir_subtitulo('Cadastrar suplementos')

    nome_suplemento = input('Digite o nome do suplemento: ')
    categoria_suplemento = input('Digite a categoria do suplemento: ')
    ativo_suplemento = input('O suplemento está ativo? (s/n): ').lower() == 's'

    suplementos.append({
        'nome': nome_suplemento,
        'categoria': categoria_suplemento,
        'ativo': ativo_suplemento
    })
    print(f'{nome_suplemento} foi adicionado(a) à loja 𝐺ℎ𝑜𝑠𝑡 𝑠𝑢𝑝𝑙𝑒𝑚𝑒𝑛𝑡𝑜𝑠')

    retorna_menu_principal()

def mostrar_suplementos():
    exibir_subtitulo('Listar suplementos')

    for suplemento in suplementos:
        nome_suplemento = suplemento['nome']
        categoria = suplemento['categoria']
        ativo = 'Ativo' if suplemento['ativo'] else 'Inativo'
        print(f' - {nome_suplemento} | {categoria} | {ativo}')
    
    retorna_menu_principal()

def ativar_desativar_suplementos():
    exibir_subtitulo('Ativar/desativar suplementos')
    nome_suplemento = input('Digite o nome do suplemento para ativar/desativar: ')

    for suplemento in suplementos:
        if suplemento['nome'].lower() == nome_suplemento.lower():
            suplemento['ativo'] = not suplemento['ativo']
            status = 'ativo' if suplemento['ativo'] else 'inativo'
            print(f'O suplemento {nome_suplemento} agora está {status}.')
            break
    else:
        print(f'Suplemento {nome_suplemento} não encontrado.')

    retorna_menu_principal()

def finalizar_programa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Finalizando o programa')

def opcao_invalida():
    print('Essa opção não é válida. Tente novamente.')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()
