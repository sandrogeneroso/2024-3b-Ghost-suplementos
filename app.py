print('''
      
𝐺ℎ𝑜𝑠𝑡 𝑠𝑢𝑝𝑙𝑒𝑚𝑒𝑛𝑡𝑜𝑠

''')

print('1. cadastro de suplementos')
print('2. listar suplementos')
print('3. ativar suplementos')
print('4. sair da aplicação')

opcao_escolhida = int(input('Escolha uma opção: '))
print('você escolheu a opção: ',opcao_escolhida)

if opcao_escolhida==1:
    print('cadastrar suplementos')
elif opcao_escolhida==2:
    print('listar suplementos')
elif opcao_escolhida==3:
    print('ativar/desativar suplementos')
else:
    print('sair da aplicação')

