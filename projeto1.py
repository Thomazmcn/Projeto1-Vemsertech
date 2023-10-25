def Main(acesso="primeiro"):  # Primeira função que inicia todo o fluxo
    if acesso == "primeiro":  # Indica a primeiro input na sessao desse usuario.
        print(
            "\n--**{ INICIALIZANDO SISTEMA IFOOD }**--".center(80)
        )  # Formatação para melhorar expericencia do usuario.

    escolha = input(
        "\nDigite o numero da opção desejada.\n 1 - Parceiro \n 2 - Cliente \n"
    )  # opçoes de navegaçao, dividem os usuarios entre parceiros e clientes
    if escolha == "1":
        print("\n***** Bem vindo parceiro! Muito bom tê-lo aqui. *****".center(50))
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
        " 5 - Remover restaurante",
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
            return menu_parceiros()
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
    continua = "1"  # utilizado para while da linha 161

    while continua == "1":
        prato = input("\nDigite o nome do prato: \n")
        preco = input("\nDigite o preço do prato: \nR$ ")

        # Remove vírgulas, pontos e espaços da entrada do usuário
        preco = preco.replace(",", "").replace(".", "").replace(" ", "")

        if preco.isdigit() and float(preco) > 0:
            cardapio_temp.append(prato)
            preco_temp.append(float(preco))
            continua = input("\nDigite 1 para adicionar um novo item, ou 0 para sair: ")
        else:
            print("\nPor favor, digite um preço válido maior que zero.")

    cardapios.append(cardapio_temp)
    precos.append(preco_temp)
    print(f"\nO cardápio do {nome_restaurante} é: ")
    
    for i in range(len(cardapio_temp)):
        print(cardapio_temp[i], end=" - ")
        print(preco_temp[i])
        return menu_parceiros()

#teste de pull request

def editar_cardapio():
    pass


"""
Função adicional proposta pelos alunos. Cria um desconto aplicado a todo o cardapio. 
"""


def desconto():
    restaurante = None
    desconto = "0.0"
    contador = 0
    while restaurante not in indice_restaurantes:
        if restaurante is not None:
            print("Nome invalido. Digite um restaurante cadastrado.")
        restaurante = input(" Digite o nome do restaurante que fará promoção: ")
    while not desconto.isnumeric():
        desconto = input(" Digite o desconto desejado. Ex: 30 => 30%.\n ")
    coeficiente = (100 - int(desconto)) / 100
    indice = indice_restaurantes.index(restaurante)
    for valor in precos[indice]:
        valor = valor * coeficiente
        contador += 1
    print(
        f" Os {contador} itens do cardapio do restaurante {restaurante} receberam desconto de {desconto}%. \n "
    )
    return menu_parceiros()


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
