class MenuOptions:

    @staticmethod
    def dashboard():
        print("""
             ______     ________   ____   ____    _                ______                   
            |_   _ `.  |_   __  | |_  _| |_  _|  (_)             .' ___  |                  
              | | `. \   | |_ \_|   \ \   / /    __    _ .--.   / .'   \_|  ,--.    _ .--.  
              | |  | |   |  _| _     \ \ / /    [  |  [ `.-. |  | |        `'_\ :  [ `/'`\] 
             _| |_.' /  _| |__/ |     \ ' /      | |   | | | |  \ `.___.'\ // | |,  | |     
            |______.'  |________|      \_/      [___] [___||__]  `.____ .' \ -;__/ [___]  

            Bem vindo!!

                Opções:
                [1] Cadastrar Veículo
                [2] Listar informações de veículo
                [3] Vender veículo
                [4] Alterar dados de veículo
                [5] Histórico da empresa
                [0] Sair do sistema\n
            """)

    @staticmethod
    def cadastro_veiculo():
        """OPCAO 1 dashboard"""
        print("""
                Cadastro de veículos:

                    Opções:
                    [1] Cadastrar Moto/Triciclo
                    [2] Cadastrar Carro
                    [3] Cadastrar Camionete
                    [0] Voltar\n
                    """)

    @staticmethod
    def listar_infos():
        print("""
               Listar informações de veículos:
               "Lembre-se de ter em mãos o chassi do veículo"

                   Opções:
                   [1] Iformações de Moto/Triciclo
                   [2] Informações de Carro
                   [3] Informações de Camionete
                   [0] Voltar\n
                   """)

    @staticmethod
    def historico():
        """OPCAO 5 dashboard"""
        print("""
                   Histórico da empresa:

                       Opções:
                       [1] Vendas realizadas
                       [2] Veículos disponíveis
                       [0] Voltar\n
                       """)

    @staticmethod
    def vendas_realizadas():
        print("""
            Vendas realizadas:

               Opções:
               [1] Todas as vendas
               [2] Venda de maior valor
               [3] Venda de menor valor
               [0] Voltar\n
               """)

    @staticmethod
    def veiculos_disponiveis():
        print("""
            Veículos disponíveis

               Opções:
               [1] Todos os veículos
               [2] Moto/Triciclo
               [3] Carro
               [4] Camionete
               [0] Voltar\n
               """)
