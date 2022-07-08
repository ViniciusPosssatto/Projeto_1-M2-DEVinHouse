from time import sleep

from entity import *
from menu.menu_options import MenuOptions
from menu.valida_input import *


class Menu:

    @staticmethod
    def start():
        while True:
            try:
                MenuOptions.dashboard()
                option = ' '
                while option not in [1, 2, 3, 4, 5, 0]:
                    option = int(input('Digite a opção desejada: '))
                if option == 1:
                    """Cadastrar veículo."""
                    while True:
                        MenuOptions.cadastro_veiculo()
                        sub_option = validar_options('c')
                        if sub_option == 1:
                            print("\033[1;94m\nCadastrar MOTO/TRICICLO\033[0;0m\n")
                            modelo = input('Digite nome do modelo: ')
                            rodas = validar_rodas()
                            potencia = validar_potencia()
                            placa = validar_placa('moto')
                            valor = validar_valor()
                            data = validar_data()
                            cor = input('Digite a cor predominante: ')
                            MotoTriciclo(potencia=potencia, rodas=rodas, data_fabr=data, modelo=modelo, placa=placa,
                                         valor=valor, cor=cor).salvar_mototriciclo()
                            print('\033[1;94msalvando...\033[0;0m')
                            sleep(1)
                            print('\033[1;32mCadastro de veículo concluído.\033[0;0m')
                        if sub_option == 2:
                            print("\033[1;94m\nCadastrar CARRO\033[0;0m\n")
                            modelo = input('Digite nome do modelo: ')
                            portas = validar_portas()
                            potencia = validar_potencia()
                            placa = validar_placa('carro')
                            valor = validar_valor()
                            data = validar_data()
                            cor = input('Digite a cor predominante: ')
                            combustivel = validar_combustivel('carro')

                            Carro(potencia=potencia, portas=portas, data_fabr=data, modelo=modelo, placa=placa,
                                  valor=valor, combustivel=combustivel, cor=cor).salvar_carro()
                            print('\033[1;94msalvando...\033[0;0m')
                            sleep(1)
                            print('\033[1;32mCadastro de veículo concluído.\033[0;0m')
                        if sub_option == 3:
                            print("\033[1;94m\nCadastrar CAMIONETE\033[0;0m\n")
                            modelo = input('Digite nome do modelo: ')
                            portas = validar_portas()
                            potencia = validar_potencia()
                            placa = validar_placa('camionete')
                            valor = validar_valor()
                            data = validar_data()
                            cor = input('Digite a cor predominante: ')
                            combustivel = validar_combustivel('camionete')
                            cacamba = validar_cacamba()
                            Camionete(potencia=potencia, portas=portas, data_fabr=data, modelo=modelo, placa=placa,
                                      valor=valor, combustivel=combustivel, cacamba=cacamba, cor=cor).salvar_camionete()
                            print('\033[1;94mSalvando...\033[0;0m')
                            sleep(1)
                            print('\033[1;32mCadastro de veículo concluído.\033[0;0m')
                        if sub_option == 0:
                            break

                if option == 2:
                    """Listar informações de veículo."""
                    while True:
                        MenuOptions.listar_infos()
                        sub_option = validar_options('b')
                        if sub_option == 1:
                            chassi = input('Digite a numeração do chassi: ')
                            Veiculo.listar_info_veiculo('moto', chassi)
                            sleep(1)
                        if sub_option == 2:
                            chassi = input('Digite a numeração do chassi: ')
                            Veiculo.listar_info_veiculo('carro', chassi)
                            sleep(1)
                        if sub_option == 3:
                            chassi = input('Digite a numeração do chassi: ')
                            Veiculo.listar_info_veiculo('camionete', chassi)
                            sleep(1)
                        if sub_option == 4:
                            RetornaInfos.retorna_todos_disponiveis()
                            sleep(2)
                        if sub_option == 0:
                            break

                if option == 3:
                    print("Vender veículo: ")
                    opcao = validar_opcao()
                    chassi = validar_chassi(opcao)
                    cpf = validar_cpf()
                    valor = validar_valor()
                    Veiculo.vender_veiculo(chassi=chassi, cpf=cpf, opcao=opcao, valor=valor)

                if option == 4:
                    """Alterar dados de veículo."""
                    while True:
                        MenuOptions.altera_info_veiculo()
                        sub_option = validar_options('d')
                        if sub_option == 1:
                            print("\033[1;94m\nAlterar COR\033[0;0m")
                            opcao = validar_opcao()
                            chassi = validar_chassi(opcao)
                            cor = input('Digite a nova cor: ')
                            Veiculo.alterar_info_veiculo(opcao=opcao, chassi=chassi, type_info='cor', nova_info=cor)
                            print('\033[1;32mCor alterada com sucesso!\033[0;0m')
                            sleep(1)
                        if sub_option == 2:
                            print("\033[1;94m\nAlterar VALOR\033[0;0m")
                            opcao = validar_opcao()
                            chassi = validar_chassi(opcao)
                            valor = validar_valor()
                            Veiculo.alterar_info_veiculo(opcao=opcao, chassi=chassi, type_info='valor', nova_info=valor)
                            print('\033[1;32mValor alterado com sucesso!\033[0;0m')
                            sleep(1)
                        if sub_option == 0:
                            break

                if option == 5:
                    """Histórico da empresa."""
                    while True:
                        MenuOptions.historico()
                        sub_option = validar_options('d')
                        if sub_option == 1:
                            """Vendas realizadas"""
                            while True:
                                MenuOptions.vendas_realizadas()
                                sub_option = validar_options('c')
                                if sub_option == 1:
                                    RetornaInfos.retorna_todas_vendas()
                                if sub_option == 2:
                                    RetornaInfos.retorna_vendido_maior_valor()
                                if sub_option == 3:
                                    RetornaInfos.retorna_vendido_menor_valor()
                                if sub_option == 0:
                                    break

                        if sub_option == 2:
                            """Veículos disponíveis"""
                            while True:
                                MenuOptions.veiculos_disponiveis()
                                sub_option = validar_options('b')
                                if sub_option == 1:
                                    RetornaInfos.retorna_todos_disponiveis()
                                if sub_option == 2:
                                    RetornaInfos.retorna_veiculos_por_tipo('moto')
                                if sub_option == 3:
                                    RetornaInfos.retorna_veiculos_por_tipo('carro')
                                if sub_option == 4:
                                    RetornaInfos.retorna_veiculos_por_tipo('camionete')
                                if sub_option == 0:
                                    break
                        if sub_option == 0:
                            break

                if option == 0:
                    break
            except Exception as erro:
                print(erro)
        print('\033[1;94mSaindo do sistema...\033[0;0m')
        sleep(1)
        print('\033[1;91mFIM\033[0;0m')
