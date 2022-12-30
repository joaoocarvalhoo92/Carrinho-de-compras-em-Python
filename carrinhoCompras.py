carrinho = []
produto = ''
soma = 0

pergunta = input("Deseja realizar compras ?")
if pergunta == 'sim':
    #produto = input("Digite o produto ou digite 'sair' : ")
    while  produto != 'sair':
            produto = input("Digite o produto ou digite 'sair' : ")
            if produto == 'sair':
                    print('Carrinho finalizado !')
            else:
                preco = float(input("Preço do produto : "))
                carrinho.append(f'{produto} --- R$ {preco} Reais')
                #carrinho.append(preco)
                soma += preco
else :
    print("Carrinho finalizado !\n")

if pergunta != 'sim':
    print("Nenhum produto foi adicionado ao Carrinho de compras, volte sempre !")
else:
    print("Os produtos do seu carrinho : ")
for cod, items in enumerate(carrinho,1):
    print(cod,items)
print(f'\n O total do seu carrinho é de : R$ {soma:.2f} reais')
print(f'Foram comprados {len(carrinho)} produtos na loja !')