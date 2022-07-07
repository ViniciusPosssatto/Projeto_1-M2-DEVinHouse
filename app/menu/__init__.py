from entity import Veiculo, MotoTriciclo, Carro, Camionete, RetornaInfos
from menu_options import MenuOptions
from valida_input import validar_data


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
                    MenuOptions.cadastro_veiculo()
                    sub_option = ' '
                    while sub_option not in [1, 2, 3, 0]:
                        sub_option = int(input('Digite a opção desejada: '))
                    if sub_option == 1:
                        """Cadastrar MOTO/TRICICLO"""
                        modelo = input('Digite nome do modelo: ')
                        rodas = int(input('Digite o número de rodas: '))
                        potencia = int(input('Digite a potencia: '))
                        placa = input('Digite a placa [ AAA11A11 ]: ').upper()
                        valor = int(input('Digite o valor: R$ '))
                        data = validar_data()
                        cor = input('Digite a cor predominante: ')
                        MotoTriciclo(potencia=potencia, rodas=rodas, data_fabr=data, modelo=modelo, placa=placa,
                                     valor=valor, cor=cor).salvar_mototriciclo()
                        print('Cadastro de veículo concluído.')
                    if sub_option == 2:
                        """Cadastrar CARRO"""
                        modelo = input('Digite nome do modelo: ')
                        portas = int(input('Digite o número de portas: '))
                        potencia = int(input('Digite a potência: '))
                        placa = input('Digite a placa [ AAA11A11 ]: ').upper()
                        valor = int(input('Digite o valor: R$ '))
                        data = validar_data()
                        cor = input('Digite a cor predominante: ')
                        combustivel = input('Qual o tipo de combustível(flex/gasolina): ')

                        Carro(potencia=potencia, portas=portas, data_fabr=data, modelo=modelo, placa=placa, valor=valor,
                              combustivel=combustivel, cor=cor).salvar_carro()
                        print('Cadastro de veículo concluído.')
                    if sub_option == 3:
                        """Cadastrar CAMIONETE"""
                        modelo = input('Digite nome do modelo: ')
                        portas = int(input('Digite o número de portas: '))
                        potencia = int(input('Digite a potência: '))
                        placa = input('Digite a placa [ AAA11A11 ]: ').upper()
                        valor = int(input('Digite o valor: R$ '))
                        data = validar_data()
                        cor = input('Digite a cor predominante: ')
                        combustivel = input('Qual o tipo de combustível(diesel/gasolina): ')
                        cacamba = int(input('Qual o tamanho da caçamba(litros): '))
                        Camionete(potencia=potencia, portas=portas, data_fabr=data, modelo=modelo, placa=placa,
                                  valor=valor, combustivel=combustivel, cacamba=cacamba, cor=cor).salvar_camionete()
                        print('Cadastro de veículo concluído.')
                    if sub_option == 0:
                        break

                if option == 2:
                    """Listar informações de veículo."""
                    sub_option = ' '
                    while sub_option not in [1, 2, 3, 4, 0]:
                        sub_option = int(input('Digite a opção desejada: '))
                    if sub_option == 1:
                        chassi = input('Digite a numeração do chassi: ')
                        Veiculo.listar_info_veiculo('moto', chassi)
                    if sub_option == 2:
                        chassi = input('Digite a numeração do chassi: ')
                        Veiculo.listar_info_veiculo('carro', chassi)
                    if sub_option == 3:
                        chassi = input('Digite a numeração do chassi: ')
                        Veiculo.listar_info_veiculo('camionete', chassi)
                    if sub_option == 4:
                        RetornaInfos.retorna_todos_disponiveis()
                    if sub_option == 0:
                        break

                if option == 3:
                    """Vender veículo."""
                    opcao = input('Informe qual tipo de veículo: ')
                    chassi = input('Digite a numeração do chassi: ')
                    cpf = input('Digite o CPF do comprador: ')
                    valor = int(input('Informe o valor de venda: R$ '))
                    Veiculo.vender_veiculo(chassi=chassi, cpf=cpf, opcao=opcao, valor=valor)

                if option == 4:
                    """Alterar dados de veículo."""
                    MenuOptions.altera_info_veiculo()
                    sub_option = ' '
                    while sub_option not in [1, 2, 0]:
                        sub_option = int(input('Digite a opção desejada: '))
                    if sub_option == 1:
                        opcao = input('Qual tipo de veículo deseja alterar: ')
                        chassi = input('Digite a numeração do chassi: ')
                        cor = int(input('Digite a nova cor: '))
                        Veiculo.alterar_info_veiculo(opcao=opcao, chassi=chassi, type_info='cor', nova_info=cor)
                        print('Cor alterada com sucesso!')
                    if sub_option == 2:
                        opcao = input('Qual tipo de veículo deseja alterar: ')
                        chassi = input('Digite a numeração do chassi: ')
                        valor = int(input('Digite o novo valor: R$ '))
                        Veiculo.alterar_info_veiculo(opcao=opcao, chassi=chassi, type_info='valor', nova_info=valor)
                        print('Valor alterado com sucesso!')
                    if sub_option == 0:
                        break

                if option == 5:
                    """Histórico da empresa."""
                    MenuOptions.historico()
                    if option == 1:
                        """Vendas realizadas"""
                        MenuOptions.vendas_realizadas()
                        sub_option = ' '
                        while sub_option not in [1, 2, 3, 0]:
                            sub_option = int(input('Digite a opção desejada: '))
                        if sub_option == 1:
                            RetornaInfos.retorna_todas_vendas()
                        if sub_option == 2:
                            RetornaInfos.retorna_vendido_maior_valor()
                        if sub_option == 3:
                            RetornaInfos.retorna_vendido_menor_valor()
                        if sub_option == 0:
                            break

                    if option == 2:
                        """Veículos disponíveis"""
                        MenuOptions.veiculos_disponiveis()
                        sub_option = ' '
                        while sub_option not in [1, 2, 3, 4, 0]:
                            sub_option = int(input('Digite a opção desejada: '))
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
                    if option == 0:
                        break

                if option == 0:
                    break
            except Exception as erro:
                print(erro)
