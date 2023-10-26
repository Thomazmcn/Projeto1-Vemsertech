def Main(acesso="primeiro"):  # Primeira função que inicia todo o fluxo
    if acesso == "primeiro":  # Indica a primeiro input na sessao desse usuario.
        print(
            "\n--**{ INICIALIZANDO SISTEMA IFOOD }**--".center(80)
        )  # Formatação para melhorar expericencia do usuario.

    escolha = input(
        """\nDigite o numero da opção desejada.
 1 - Gestão de restaurantes
 2 - Gestão de cardápio 
 3 - Apresentação de informações
  Opção - """
    )
    if escolha == "1":
        print("\n***** Gestão de restaurantes *****".center(50))
        return menu_gestao_rest()  # acessa funçao menu_gestao_rest

    elif escolha == "2":
        print("\n***** Gestao de cardápio *****".center(50))
        return menu_gestao_cardapio()

    elif escolha == "3":
        print("\n***** Gestao de cardápio *****".center(50))
        return menu_informacoes()  # acessa funçao menunformaçoes_

    else:
        print("\nOpção invalda. Escolha com um número")
        acesso = "segundo"  # define variavel a ser utilizda na invocação da função Main
        return Main(acesso="segundo")
        # cria loop para input errado. Simplificando tratamento de inputs. Retorna ao inicio.


def menu_gestao_rest():
    print(
        "\n ---- Escolha pelo numero ---- ".center(35),  
        "\n 1 - Cadastrar restaurante",
        " 2 - Editar restaurantes",
        " 3 - Remover restaurante",
        " 4 - Voltar",
        sep="\n",
    )
    op = input("\n Digite a opção para acesso: ")
    if op == "1":
        return cadastro()

    elif op == "2":
        return editar_restaurante()

    elif op == "3":
        return remover_restaurante()

    elif op == "4" or op == "sair":
        return Main(acesso="segundo")

    else:
        print("\n********** Comando invalido! **********".center(60))
        return menu_gestao_rest()


def menu_gestao_cardapio():
    print(
        "\n ---- Escolha pelo numero ---- ".center(35), 
        "\n 1 - Editar cardapios",
        " 2 - Dar desconto",
        " 3 - Voltar",
        sep="\n",
    )
    op = input("\n Digite a opção: ")
    if op == "1":
        return editar_cardapio()

    elif op == "2":
        return desconto()

    elif op == "3" or op == "sair":
        return Main(acesso="segundo")

    else:
        print("\n********** Comando invalido! **********".center(60))
        return menu_gestao_cardapio()


def menu_informacoes():
    print(
        "\n ---- Escolha pelo numeros ---- ".center(35),
        "\n 1 - Listar restaurantes",
        " 2 - Detalhar restaurantes",
        " 3 - Cardapio",
        " 4 - Voltar",
        sep="\n",
    )
    op = input("\n Digite a opção: ")
    if op == "1":
        return listar_restaurantes("menu_info")

    elif op == "2":
        return detalhar_restaurantes()

    elif op == "3":
        return visualizar_cardapio("menu_info")

    elif op == "4" or op == "sair":
        return Main(acesso="segundo")

    else:
        print("\n********** Comando invalido! **********".center(60))
        return menu_gestao_cardapio()


def cadastro():
    nome_restaurante = input("\n Digite o nome do restaurante: ")
    endereco_restaurante = input(" Digite o endereço do restaurante: ")
    telefone_restaurante = input(" Digite o telefone do restaurante: ")
    tempo_de_entrega = int(input(" Digite o tempo de entrega em minutos: "))

    restaurante_info = [
        nome_restaurante,
        endereco_restaurante,
        telefone_restaurante,
        tempo_de_entrega,
    ]

    restaurantes.append(restaurante_info)
    indice_restaurantes.append(nome_restaurante)

    print(f"\n Restaurante '{nome_restaurante}' cadastrado com sucesso!")
    print("\n Agora crie um cardapio! ")

    return criar_cardapio(nome_restaurante)


def editar_restaurante():
    opcoes = []
    escolha = "-1"
    for indice, numero in enumerate(indice_restaurantes):
        opcoes.append(str(indice))
        print(indice, "-", numero)

    while escolha not in opcoes:
        escolha = input("\nDigite o número do restaurante que deseja editar: ")

    if escolha.isdigit():
        escolha = int(escolha)

        if 0 <= escolha < len(indice_restaurantes):
            restaurante_selecionado = restaurantes[escolha]
            print(f"\nEditando restaurante: {indice_restaurantes[escolha]}")

            novo_nome = input("\nDigite o novo nome do restaurante: ")
            novo_endereco = input("Digite o novo endereço do restaurante: ")
            novo_telefone = input("Digite o novo telefone do restaurante: ")

            while True:
                novo_tempo_de_entrega = input(
                    "Digite o novo tempo de entrega em minutos: "
                )
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
            return menu_gestao_rest()
        else:
            print("Escolha inválida. Tente novamente.")
            return editar_restaurante()
    else:
        print("Escolha inválida. Deve ser um número. Tente novamente.")
        return editar_restaurante()


"""
Função cria cardapio do novo restaurante cadastrado.
"""


def criar_cardapio(nome_restaurante):
    cardapio_temp = []
    preco_temp = []
    continua = "1"

    while continua == "1":
        prato = input("\nDigite o nome do prato: \n")
        preco = input("\nDigite o preço do prato: \nR$ ")

        # Troca a virgula por ponto
        preco = preco.replace(",", ".")

        if preco.replace(".", "", 1).isdigit() and float(preco) > 0:
            cardapio_temp.append(prato)
            preco_temp.append(float(preco))
            continua = input(
                "\nDigite 1 para adicionar um novo item, ou qualquer tecla para sair: "
            )
        else:
            print("\nPor favor, digite um preço válido maior que zero.")

    cardapios.append(cardapio_temp)
    precos.append(preco_temp)
    print(f"\nO cardápio do {nome_restaurante} é: ")

    for i in range(len(cardapio_temp)):
        print(cardapio_temp[i], end=" - ")
        print(preco_temp[i])
        return menu_gestao_rest()


def editar_cardapio():
    print("*** Editor de cardapios***")
    id_restaurante = visualizar_cardapio(
        "ed_cardapio"
    )  # Return a variavel id_restaurante
    opcao = input(
        "Para editar prato digite 1, 2 para deletar prato, 3 para adicionar prato ou qualquer tecla para sair:\n"
    )

    if opcao == "1":
        id_prato = tratar_prato(id_restaurante)  # Obtém o índice do prato
        novo_prato = input(f"Digite novo nome para o prato N - {id_prato+1}\n")
    
        novo_preco = input("\nDigite o preço do prato: \n R$ ")

    #substitui vírgulas por pontos
        novo_preco = novo_preco.replace(",", ".")

        while not novo_preco.replace(".", "", 1).isdigit() or float(novo_preco) <= 0:
            print("Por favor, digite um preço válido maior que zero.")
            novo_preco = input("\nDigite o preço do prato: \n R$ ")

        cardapios[id_restaurante][id_prato] = novo_prato
        precos[id_restaurante][id_prato] = float(novo_preco)
        repetir = input("Para editar outro prato digite 1, qualquer tecla para sair:")
        if repetir == "1":
            return editar_cardapio()
        else:
            return menu_gestao_cardapio()


    elif opcao == "2":
        id_prato = tratar_prato(id_restaurante)
        deletar = input(
            f"""Deseja deletar o prato {cardapios[id_restaurante][id_prato]}?
    \nDigite 1 para sim, qualquer tecla para não."""
        )
        if deletar == "1":
            del cardapios[id_restaurante][id_prato]
            del precos[id_restaurante][id_prato]
            repetir = input(
                "Para editar outro prato digite 1, qualquer tecla para sair:"
            )
            if repetir == "1":
                return editar_cardapio()
            else:
                return menu_gestao_cardapio()
        else:
            return menu_gestao_cardapio()

    elif opcao == "3":
        novo_prato = input("Digite o nome do novo prato: ")
        novo_preco_prato = input("Digite o preço do novo prato: R$ ")

        novo_preco_prato = novo_preco_prato.replace(",", ".")
        
        while not novo_preco_prato.replace(".", "", 1).isdigit() or float(novo_preco_prato) <= 0:
            print("Por favor, digite um preço válido maior que zero.")
            novo_preco_prato = input("\nDigite o preço do prato: \n R$ ")
            
        cardapios[id_restaurante].append(novo_prato)
        precos[id_restaurante].append(float(novo_preco_prato))
        print(f"Prato '{novo_prato}' adicionado com sucesso!")

        repetir = input("Para adicionar outro prato digite 1, qualquer tecla para sair: ")
        if repetir == "1":
            return editar_cardapio()
        else:
            return menu_gestao_cardapio()


def tratar_prato(id_restaurante):
    id_prato = "-1"
    while id_prato not in range(len(cardapios[id_restaurante][:])):
        id_prato = int(input(("\nDigite o numero do prato.\n"))) - 1
    return id_prato


def visualizar_cardapio(origem):
    id_restaurante = "-1"
    listar_restaurantes("cardap")
    while id_restaurante not in range(len(indice_restaurantes)):
        id_restaurante = int(input("\nDigite o numero do restaurante desejado:\n ")) - 1
    print(f"\nSegue o cardapio do restaurante {indice_restaurantes[id_restaurante]}:")
    for pratos in range(len(cardapios[id_restaurante][:])):
        print(
            pratos + 1,
            " - ",
            cardapios[id_restaurante][pratos],
            " - ",
            precos[id_restaurante][pratos],
        )
    if origem == "ed_cardapio":
        return id_restaurante
    else:
        return menu_informacoes()


def listar_restaurantes(origem):
    for i in range(len(indice_restaurantes)):
        print(i + 1, " - ", indice_restaurantes[i])
    if origem == "menu_info":
        return menu_informacoes()
    else:
        return


def detalhar_restaurantes():
    id_restaurante = "-1"
    print("Detalhamento de restaurante.")
    listar_restaurantes("det_rest")
    while id_restaurante not in range(len(indice_restaurantes)):
        id_restaurante = int(input("\nDigite o numero do restaurante desejado:\n ")) - 1
    print(
        f"""Nome - {restaurantes[id_restaurante][0]}
Endereço - {restaurantes[id_restaurante][1]}
Telefone - {restaurantes[id_restaurante][2]}
Tempo de entrega - {restaurantes[id_restaurante][3]}
    """
    )
    return menu_informacoes()


"""
Função adicional proposta pelos alunos. Cria um desconto aplicado a todo o cardapio. 
"""


def desconto():
    restaurante = None
    desconto = "0.0"
    contador = 0
    listar_restaurantes("descont")
    while restaurante not in range(len(indice_restaurantes)):
        if restaurante is not None:
            print("Numero invalido. Digite um numero cadastrado.")
        restaurante = (
            int(input(" Digite o numero do restaurante que fará promoção: ")) - 1
        )
    while not desconto.isnumeric():
        desconto = input(" Digite o desconto desejado. Ex: 30 => 30%.\n ")
    coeficiente = (100 - int(desconto)) / 100
    for valor in precos[restaurante]:
        valor = valor * coeficiente
        precos[restaurante][contador] = valor
        contador += 1

    print(
        f" Os {contador} itens do cardapio do restaurante {indice_restaurantes[restaurante]} receberam desconto de {desconto}%. \n "
    )
    return menu_gestao_cardapio()


"""
Função de remoçao de restaurantes. Quando tentei corrigir versões, 
gerei um codigo com 2 funçoes iguais escritas pelo Thiago. Quando 
apaguei a que aparecia como sendo feita por mim, sumiu o log do Thiago. 
"""


def remover_restaurante():
    print("Lista de restaurantes para remoção:")

    for i, restaurante in enumerate(indice_restaurantes):
        print(f"{i + 1} - {restaurante}")

    escolha = input(
        "\nDigite o número do restaurante que deseja remover ou '0' para cancelar: "
    )

    if escolha == "0":
        return menu_gestao_rest()

    if escolha.isdigit():
        escolha = int(escolha) - 1
        if 0 <= escolha < len(indice_restaurantes):
            restaurante_removido = indice_restaurantes.pop(escolha)
            restaurante_info = restaurantes.pop(escolha)
            cardapio_removido = cardapios.pop(escolha)
            preco_removido = precos.pop(escolha)
            print(f"Restaurante '{restaurante_removido}' removido com sucesso!")
        else:
            print("Escolha inválida. Tente novamente.")
    else:
        print("Escolha inválida. Deve ser um número. Tente novamente.")

    return menu_gestao_rest()


indice_restaurantes = [
    "Das Haus",
    "Papa de Lucca",
    "Onigiri Sushi ",
    "Muquecas e Cia",
    "Le Jaque Bistro",
]

restaurantes = [
    ["Das Haus", "Rua do chucrute, N.500", "11-3456-9876", 45],
    ["Papa de Lucca", "Rua da pizza, N. 190", "11-1234-0987", 30],
    ["Onigiri Sushi ", "Avenida da Liberdade, N. 999", "11-4312-4576", 50],
    ["Muquecas e Cia", "Rua dos Orixás, N. 30", "11-5678-4321", 25],
    ["Le Jaque Bistro", "Avenida Crpissant, N. 222", "11-76442323", 60],
]  # Lista criada como bd para restaurantes parceiros

cardapios = [
    ["Eisbein", "Currywurst", "Sauerkraut", "Aftasardemedoem"],
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
