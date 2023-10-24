def Main(acesso="primeiro"):  # Primeira função que inicia todo o fluxo
    if acesso == "primeiro":  # Indica a primeiro input na sessao desse usuario.
        print(
            "\n--**{ INICIALIZANDO SISTEMA IFOOD }**--".center(80)
        )  # Formatação para melhorar expericencia do usuario.

    escolha = input(
        "\nDigite o numero da opção desejada.\n 1 - Parceiro \n 2 - Cliente \n"
    )  # opçoes de navegaçao, dividem os usuarios entre parceiros e clientes
    if escolha == "1":
        print("\n***** Bem vindo parceiro! Muito bom telo aqui. *****".center(50))
        pass
        return menu_parceiros()  # acessa funçao menu_parceiros

    elif escolha == "2":
        print("\n***** Bem vindo ao Ifood!!! *****".center(50))
        pass
        return menu_clientes()  # acessa funçao menu_clientes

    else:
        print("\nOpção invalda. Escolha com um número")
        acesso = "segundo"  # define variavel a ser utilizda na invocação da função Main
        return Main(
            acesso="segundo"
        )  # cria loop para input errado. Simplificando tratamento de inputs. Retorna ao inicio.


def menu_parceiros():  # arvore de decisao menu_parceiros
    print(
        "\n ---- Menu parceiros---- ".center(35),
        "\n 1 - Cadastrar restaurante",
        " 2 - Editar restaurantes",
        " 3 - Editar cardápio",
        " 4 - Dar desconto",
        " 5 - Remover restaurante"
        " 6 - Sair",
        sep="\n",
    )
    op = input("\n Digite a opção para acesso: ")
    if op == "1":
        return cadastro()

    elif op == "2":
        return editar_restaurante()

    elif op == "3":
        return editar_cardapio()

    elif op == "4":
        return desconto()
    
    elif op == "5":
        return remover_restaurante()

    elif op == "6" or op == "sair":
        return Main()

    else:
        print("\n********** Comando invalido! **********".center(60))
        return menu_parceiros()


def menu_clientes():  # arvore de decisao menu_clientes
    print(
        "\n ---- Escolha um dos numeros. ---- ".center(35),
        "\n 1 - Restaurantes ",
        " 2 - Busca de restaurantes",
        " 3 - Sair",
        sep="\n",
    )
    op = input("\n Digite a opção: ")
    if op == "1":
        return restaurante()

    elif op == "2":
        return busca()

    elif op == "3" or op == "sair":
        return Main()

    else:
        print("\n********** Comando invalido! **********".center(60))
        return menu_parceiros()

def cadastro():
    nome_restaurante = input("Digite o nome do restaurante: ")
    endereco_restaurante = input("Digite o endereço do restaurante: ")
    telefone_restaurante = input("Digite o telefone do restaurante: ")
    tempo_de_entrega = int(input("Digite o tempo de entrega em minutos: "))
    
    restaurante_info = [nome_restaurante, endereco_restaurante, telefone_restaurante, tempo_de_entrega]

    restaurantes.append(restaurante_info)
    indice_restaurantes.append(nome_restaurante)
    
    print(f"Restaurante '{nome_restaurante}' cadastrado com sucesso!")
    
    return menu_parceiros()

def editar_restaurante():
    
    for indice, numero in enumerate(indice_restaurantes):
        print(indice,'-', numero)
    
    escolha = input("\nDigite o número do restaurante que deseja editar: ")
    
    if escolha.isdigit():
        escolha = int(escolha)
        
        if 0 <= escolha < len(indice_restaurantes):
            restaurante_selecionado = restaurantes[escolha]
            print(f"\nEditando restaurante: {indice_restaurantes[escolha]}")
            
            novo_nome = input("Digite o novo nome do restaurante: ")
            novo_endereco = input("Digite o novo endereço do restaurante: ")
            novo_telefone = input("Digite o novo telefone do restaurante: ")
            
            while True:
                novo_tempo_de_entrega = input("Digite o novo tempo de entrega em minutos: ")
                if novo_tempo_de_entrega.isdigit():
                    novo_tempo_de_entrega = int(novo_tempo_de_entrega)
                    break
                else:
                    print("Tempo de entrega deve ser um número inteiro.")
            
            restaurante_selecionado[0] = novo_nome
            restaurante_selecionado[1] = novo_endereco
            restaurante_selecionado[2] = novo_telefone
            restaurante_selecionado[3] = novo_tempo_de_entrega
            
            print(f"Restaurante '{novo_nome}' editado com sucesso!")
            return menu_parceiros()
        else:
            print("Escolha inválida. Tente novamente.")
            return editar_restaurante()
    else:
        print("Escolha inválida. Deve ser um número. Tente novamente.")
        return editar_restaurante()
 
indice_restaurantes = [
    "Der Haus",
    "Papa de Lucca",
    "Onigiri Sushi ",
    "Muquecas e Cia",
    "Le Jaque Bistro"
]

restaurantes = [
    ["Der Haus", "Rua do chucrute, N.500", "11-3456-9876", 45],
    ["Papa de Lucca", "Rua da pizza, N. 190", "11-1234-0987", 30],
    ["Onigiri Sushi ", "Avenida da Liberdade, N. 999", "11-4312-4576", 50],
    ["Muquecas e Cia", "Rua dos Orixás, N. 30", "11-5678-4321", 25],
    ["Le Jaque Bistro", "Avenida Crpissant, N. 222", "11-76442323", 60],
]  # Lista criada como bd para restaurantes parceiros

cardapios = [
    ["Eisbein", "Currywurst", "Sauar Kraut", "Aftasardemedoem"],
    ["Espagete a bolonhesa", "Polpetone", "Burrata"],
    ["Sukiaki", "Combinado", "Yakisoba", "Sobôro"],
    ["Muqueca de camarão", "Acarajé", "Vatapá"],
    ["Filet ao Poivre", "Escargot", "Rest ondon té"],
]  # Lista criada para os cardapios

precos = [
    [45.5, 25.0, 15.5, 50.5],
    [35.0, 40.0, 20.0],
    [90.0, 60.0, 50.0, 20.0],
    [80.0, 25.5, 25],
    [75.5, 50.0, 20.0],
]



Main()

# teste
