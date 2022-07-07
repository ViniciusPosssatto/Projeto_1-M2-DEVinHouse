from entity import Veiculo, MotoTriciclo, Carro, Camionete, Historico, RetornaInfos
from menu_options import MenuOptions

class Menu:

    @staticmethod
    def start():
        while True:
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
                    modelo = input('Digite nome do modelo: ')
                    rodas = int(input('Digite o número de rodas: '))
                    potencia = int(input('Digite a potencia: '))
                    placa = input('Digite a placa [ AAA11A11 ]: ').upper()
                    valor = int(input('Digite o valor: R$ '))
                    data = input('Digite a data de fabricação [ dd/mm/aa ]: ')
                    cor = input('Digite a cor predominante: ')
                    MotoTriciclo(potencia=potencia, rodas=rodas, data_fabr=data, modelo=modelo, placa=placa,
                                 valor=valor, cor=cor).salvar_mototriciclo()
                if sub_option == 2:
                    modelo = input('Digite nome do modelo: ')
                    rodas = int(input('Digite o número de rodas: '))
                    potencia = int(input('Digite a potencia: '))
                    placa = input('Digite a placa [ AAA11A11 ]: ').upper()
                    valor = int(input('Digite o valor: R$ '))
                    data = input('Digite a data de fabricação [ dd/mm/aa ]: ')
                    cor = input('Digite a cor predominante: ')
                    MotoTriciclo(potencia=potencia, rodas=rodas, data_fabr=data, modelo=modelo, placa=placa,
                                 valor=valor, cor=cor).salvar_mototriciclo()
                if sub_option == 3:
                    print('opt 3')
                if sub_option == 0:
                    break

            if option == 2:
                """Listar informações de veículo."""
                sub_option = ' '
                while sub_option not in [1, 2, 3, 0]:
                    option = int(input('Digite a opção desejada: '))
                if sub_option == 1:
                    pass
                if sub_option == 2:
                    pass
                if sub_option == 3:
                    pass
                if sub_option == 0:
                    break

            if option == 3:
                """Vender veículo."""
                # Veiculo.vender_veiculo()

            if option == 4:
                """Alterar dados de veículo."""
                # Veiculo.alterar_info_veiculo()

            if option == 5:
                """Histórico da empresa."""
                MenuOptions.historico()
                if option == 1:
                    """Vendas realizadas"""
                    MenuOptions.vendas_realizadas()
                    sub_option = ' '
                    while sub_option not in [1, 2, 3, 0]:
                        option = int(input('Digite a opção desejada: '))
                    if sub_option == 1:
                        pass
                    if sub_option == 2:
                        pass
                    if sub_option == 3:
                        pass
                    if sub_option == 0:
                        break

                if option == 2:
                    """Veículos disponíveis"""
                    MenuOptions.veiculos_disponiveis()
                    sub_option = ' '
                    while sub_option not in [1, 2, 3, 4, 0]:
                        option = int(input('Digite a opção desejada: '))
                if option == 0:
                    break

            if option == 0:
                break
