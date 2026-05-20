# Sistema de cadastro de usuarios e produtos 
# O sistema devera permitir 
# - cadastrar 
# - Listar 
# - deletar 

# Criação de listas 
usuarios = []
produtos = []

#-----------------------------------------
# ---------Função menu ususario----------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print("----------Menu Usuários----------")
        print("1 - Cadastrar Usuários")
        print("2 - Listar usuários")
        print("3 - Deletar usuário ")
        print("4 - Voltar")

        opcao_menu_usuario = int(input("Digite uma opção: "))

        match opcao_menu_usuario:
            # Cadastrar ususario
            case 1: 
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")
                email = input("Digite o email: ")
            
                # Criação do json de usuarios (cahve: valor)
                usuario = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email
                }
                
                #Adicionar o json no array
                usuarios.append(usuario)
                print(f"Usuario {usuario['nome']} cadastrado com sucesso!")
            # Listar usuarios
            case 2: 
                print("\n Lista de Usuarios: ")

                if(len(usuarios) == 0):
                    print("Nenhum usuário cadastrado!")
                else:
                    for usu in usuarios:
                        print("--------------------")
                        print("Nome: ", usu["nome"])
                        print("Telefone: ", usu["telefone"])
                        print("email: ", usu["email"])

            # Deletar usuario
            case 3:
                nome_deletar = input("Digite o nome do usuario que deseja deletar: ")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("Usuario removido com sucesso!")
                if(encontrado == False):
                    print("usuario não encontrado")

            # Voltar ao menu principal
            case 4:
                print("Voltando ao menu principal...")
                break
            # ---------Função menu produtos----------
def menu_produtos():
    opcao_menu_produto = 0

    while(opcao_menu_produto != 5):
        print()
        print("----------Menu Produtos----------")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Deletar produto ")
        print("4 - Calcular total")
        print("5 - Voltar")

        opcao_menu_produto = int(input("Digite uma opção: "))

        match opcao_menu_produto:
            # Cadastrar produto
            case 1: 
                nome = input("Digite o nome: ")
                descricao = input("Digite a descricao: ")
                quantidade = input("Digite o quantidade: ")
                valor = float(input("Digite o valor: "))
            
                # Criação do json de usuarios (cahve: valor)
                produto = {
                    "nome": nome,
                    "descricao": descricao,
                    "quantidade": quantidade,
                    "valor": valor
                }
                
                #Adicionar o json no array
                produtos.append(produto)
                print(f"Produto {produto['nome']} cadastrado com sucesso!")
            # Listar Produtos
            case 2: 
                print("\n Lista de Produto: ")

                if(len(produtos) == 0):
                    print("Nenhum produto cadastrado!")
                else:
                    for pro in produtos:
                        print("--------------------")
                        print("Nome: ", pro["nome"])
                        print("descricao: ", pro["descricao"])
                        print("quantidade: ", pro["quantidade"])
                        print("valor", pro ["Valor"])

            # Deletar produto
            case 3:
                produto_deletar = input("Digite o nome do produto que deseja deletar: ")
                encontrado = False

                for pro in produtos:
                    if(pro["nome"] == produto_deletar):
                        produtos.remove(pro)
                        encontrado = True
                        print("Produto removido com sucesso!")
                if(encontrado == False):
                    print("Produto não encontrado")

            # Voltar ao menu principal
            case 5:
                print("Voltando ao menu principal...")
                break



# ---------------------------------------------
# ----------menu principal----------
opcao_menu = 0
while(opcao_menu != 3):
    print("---------------Menu - sistema de casdastro--------------")
    print("Opções: ")
    print("1- Usuários")
    print("2- Produtos")
    print("3- Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu:
        # Menu usuarios 
        case 1:
            menu_usuarios()
        #Menu Produto
        case 2:
            menu_produtos
        case 3:
            print("Até logo!")
        case _:
            print("Opção inválida!")

