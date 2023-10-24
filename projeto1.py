restaurantes = []  # Lista criada como bd para restaurantes parceiros
cardapios = []  # Lista criada para os cardapios


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
        " 5 - Sair",
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

    elif op == "5" or op == "sair":
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


Main()

#teste