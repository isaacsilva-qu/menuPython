carrinho = []
while True:
    print('-- Bem vindo ao menu --')
    print('1 - Adicionar produto')
    print('2 - Editar produto')
    print('3 - Remover produto')
    print('4 - Lista todos os produto')
    print('5 - Sair')
    opcao = input('Selecione a opção: ')
    if opcao == '1':
        produto = input('Digite o nome do produto: ')
        carrinho.append(produto)
        print('Produto adicionado com sucesso!')
    elif opcao == '2':
        produto = input('Digite o porduto que deseja editar: ')
        if produto in carrinho:
            indice = carrinho.index(produto)
            carrinho[indice] = input('Digite o novo nome do produto: ')
            print('Produto editado com sucesso!')
        else:
            print('Produto não encontrado!')
    elif opcao == '3':
        produto = input('Digite o que deseja remover: ')
        if produto in carrinho:
            carrinho.remove(produto)
            print('Produto removido com sucesso!')
        else:
            print('Produto não foi encontrado!')
    elif opcao == '4':
        print('---- Seu carrinho ----')
        for produto in carrinho:
            print(f'Nome do produto: {produto}')
    elif opcao == '5':
        print('Você saiu do programa')
        break
print(carrinho)