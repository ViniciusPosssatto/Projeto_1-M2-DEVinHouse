from time import sleep

from entity import *
from menu.menu_options import MenuOptions
from menu.valida_input import ValidarInputs


class Menu:

    def __init__(self):
        """OBS: utilizei conceito de composição aqui"""
        self.validar = ValidarInputs()
        self.options = MenuOptions()

    def start(self):
        while True:
            try:
                self.options.dashboard()
                option = ' '
                while option not in ['1', '2', '3', '4', '5', '0']:
                    option = input('Digite a opção desejada: ')
                self.validar.cls()
                if option == '1':
                    """Cadastrar veículo."""
                    while True:
                        self.options.cadastro_veiculo()
                        sub_option = self.validar.validar_options('c')
                        if sub_option == 1:
                            print("\033[1;94m\nCadastrar MOTO/TRICICLO\033[0;0m\n")
                            modelo = input('Digite nome do modelo: ')
                            rodas = self.validar.validar_rodas()
                            potencia = self.validar.validar_potencia()
                            placa = self.validar.validar_placa('moto')
                            valor = self.validar.validar_valor()
                            data = self.validar.validar_data()
                            cor = input('Digite a cor predominante: ')
                            MotoTriciclo(potencia=potencia, rodas=rodas, data_fabr=data, modelo=modelo, placa=placa,
                                         valor=valor, cor=cor).salvar_mototriciclo()
                            print('\033[1;94msalvando...\033[0;0m')
                            sleep(1)
                            print('\033[1;32mCadastro de veículo concluído.\033[0;0m')
                            sleep(2)
                            self.validar.cls()
                        if sub_option == 2:
                            print("\033[1;94m\nCadastrar CARRO\033[0;0m\n")
                            modelo = input('Digite nome do modelo: ')
                            portas = self.validar.validar_portas()
                            potencia = self.validar.validar_potencia()
                            placa = self.validar.validar_placa('carro')
                            valor = self.validar.validar_valor()
                            data = self.validar.validar_data()
                            cor = input('Digite a cor predominante: ')
                            combustivel = self.validar.validar_combustivel('carro')

                            Carro(potencia=potencia, portas=portas, data_fabr=data, modelo=modelo, placa=placa,
                                  valor=valor, combustivel=combustivel, cor=cor).salvar_carro()
                            print('\033[1;94msalvando...\033[0;0m')
                            sleep(1)
                            print('\033[1;32mCadastro de veículo concluído.\033[0;0m')
                            sleep(2)
                            self.validar.cls()
                        if sub_option == 3:
                            print("\033[1;94m\nCadastrar CAMIONETE\033[0;0m\n")
                            modelo = input('Digite nome do modelo: ')
                            portas = self.validar.validar_portas()
                            potencia = self.validar.validar_potencia()
                            placa = self.validar.validar_placa('camionete')
                            valor = self.validar.validar_valor()
                            data = self.validar.validar_data()
                            cor = input('Digite a cor predominante: ')
                            combustivel = self.validar.validar_combustivel('camionete')
                            cacamba = self.validar.validar_cacamba()
                            Camionete(potencia=potencia, portas=portas, data_fabr=data, modelo=modelo, placa=placa,
                                      valor=valor, combustivel=combustivel, cacamba=cacamba, cor=cor).salvar_camionete()
                            print('\033[1;94mSalvando...\033[0;0m')
                            sleep(1)
                            print('\033[1;32mCadastro de veículo concluído.\033[0;0m')
                            sleep(2)
                            self.validar.cls()
                        if sub_option == 0:
                            self.validar.cls()
                            break

                if option == '2':
                    """Listar informações de veículo."""
                    while True:
                        self.options.listar_infos()
                        sub_option = self.validar.validar_options('a')
                        if sub_option == 1:
                            chassi = input('Digite a numeração do chassi: ')
                            Veiculo.listar_info_veiculo('moto', chassi)
                            click = input('\nPessione uma tecla para sair...')
                            self.validar.cls()
                        if sub_option == 2:
                            chassi = input('Digite a numeração do chassi: ')
                            Veiculo.listar_info_veiculo('carro', chassi)
                            click = input('\nPessione uma tecla para sair...')
                            self.validar.cls()
                        if sub_option == 3:
                            chassi = input('Digite a numeração do chassi: ')
                            Veiculo.listar_info_veiculo('camionete', chassi)
                            click = input('\nPessione uma tecla para sair...')
                            self.validar.cls()
                        if sub_option == 4:
                            RetornaInfos.retorna_todos_disponiveis()
                        if sub_option == 5:
                            RetornaInfos.retorna_todos_veiculos()
                            click = input('\nPessione uma tecla para sair...')
                            self.validar.cls()
                        if sub_option == 0:
                            self.validar.cls()
                            break

                if option == '3':
                    print("Vender veículo: ")
                    opcao = self.validar.validar_opcao()
                    chassi = self.validar.validar_chassi(opcao)
                    cpf = self.validar.validar_cpf()
                    valor = self.validar.validar_valor()
                    print('\n\033[1;94mRealizando transferência...\033[0;0m\n')
                    sleep(1)
                    Veiculo.vender_veiculo(chassi=chassi, cpf=cpf, opcao=opcao, valor=valor)
                    sleep(1)
                    click = input('\n\nPessione uma tecla para sair...')
                    self.validar.cls()

                if option == '4':
                    """Alterar dados de veículo."""
                    while True:
                        self.options.altera_info_veiculo()
                        sub_option = self.validar.validar_options('d')
                        if sub_option == 1:
                            print("\033[1;94m\nAlterar COR\033[0;0m")
                            opcao = self.validar.validar_opcao()
                            chassi = self.validar.validar_chassi(opcao)
                            cor = input('Digite a nova cor: ')
                            Veiculo.alterar_info_veiculo(opcao=opcao, chassi=chassi, type_info='cor', nova_info=cor)
                            sleep(1)
                            print('\033[1;32mCor alterada com sucesso!\033[0;0m')
                            click = input('\n\nPessione uma tecla para sair...')
                            self.validar.cls()
                        if sub_option == 2:
                            print("\033[1;94m\nAlterar VALOR\033[0;0m")
                            opcao = self.validar.validar_opcao()
                            chassi = self.validar.validar_chassi(opcao)
                            valor = self.validar.validar_valor()
                            Veiculo.alterar_info_veiculo(opcao=opcao, chassi=chassi, type_info='valor', nova_info=valor)
                            sleep(1)
                            print('\033[1;32mValor alterado com sucesso!\033[0;0m')
                            click = input('\n\nPessione uma tecla para sair...')
                            self.validar.cls()
                        if sub_option == 0:
                            self.validar.cls()
                            break

                if option == '5':
                    """Histórico da empresa."""
                    while True:
                        self.options.historico()
                        sub_option = self.validar.validar_options('d')
                        self.validar.cls()
                        if sub_option == 1:
                            """Vendas realizadas"""
                            while True:
                                self.options.vendas_realizadas()
                                sub_option = self.validar.validar_options('b')
                                self.validar.cls()
                                if sub_option == 1:
                                    RetornaInfos.retorna_todas_vendas()
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 2:
                                    RetornaInfos.retorna_vendido_maior_valor()
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 3:
                                    RetornaInfos.retorna_vendido_menor_valor()
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 4:
                                    RetornaInfos.retorna_resultado()
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 0:
                                    self.validar.cls()
                                    break

                        if sub_option == 2:
                            """Veículos disponíveis"""
                            while True:
                                self.options.veiculos_disponiveis()
                                sub_option = self.validar.validar_options('b')
                                self.validar.cls()
                                if sub_option == 1:
                                    RetornaInfos.retorna_todos_disponiveis()
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 2:
                                    RetornaInfos.retorna_veiculos_por_tipo('moto')
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 3:
                                    RetornaInfos.retorna_veiculos_por_tipo('carro')
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 4:
                                    RetornaInfos.retorna_veiculos_por_tipo('camionete')
                                    click = input('\n\nPessione uma tecla para sair...')
                                    self.validar.cls()
                                if sub_option == 0:
                                    break
                        if sub_option == 0:
                            break

                if option == '0':
                    break
            except Exception as erro:
                print(erro)
        print('\n\033[1;94mSaindo do sistema...\033[0;0m\n')
        sleep(1)
        print('\033[1;91mFIM\033[0;0m')
