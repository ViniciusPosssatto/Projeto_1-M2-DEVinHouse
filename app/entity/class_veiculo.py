from uuid import uuid4

from data import carros, camionetes, motosTriciclos
from entity.historico import Historico


tipos_veiculos = {'carro': carros, 'moto': motosTriciclos, 'camionete': camionetes}


class Veiculo:

    def __init__(self, data_fabr: str, modelo: str, placa: str, valor: int, cor: str):
        self.chassi = str(uuid4()).split('-')[0]
        self.data_fabr = data_fabr
        self.modelo = modelo
        self.placa = placa
        self.valor = valor
        self.cor = cor
        self.cpf = 0

    @staticmethod
    def vender_veiculo(opcao, chassi, cpf, valor):
        if opcao not in tipos_veiculos:
            print('\033[1;91mOpção de veículo inválida.\033[0;0m')
        veiculo = None
        for item in tipos_veiculos.get(opcao):
            if chassi == item['chassi']:
                item['cpf'] = cpf
                print(f"O veiculo modelo {item['modelo']} cuja placa é {item['placa'].upper()}, foi vendido no valor de"
                      f" R$ {item['valor']}.")
                veiculo = item
                Historico().save_transation(veiculo, cpf, valor, opcao)
                tipos_veiculos.get(opcao).remove(item)

    @staticmethod
    def listar_info_veiculo(opcao, chassi):
        if opcao not in tipos_veiculos:
            print('\033[1;91mOpção de veículo inválida.\033[0;0m')
        for item in tipos_veiculos.get(opcao):
            if chassi == item['chassi']:
                if opcao == 'carro':
                    print(f"O modelo é {item['modelo']}, possui {item['portas']} portas e {item['potencia']} "
                          f"cavalos de potência. A placa é {item['placa'].upper()} e o valor: R$ {item['valor']}. "
                          f"Foi fabricado em {item['data-fabricação']} na cor {item['cor']}. O número do chassi é "
                          f"{item['chassi']}.")
                elif opcao == 'moto':
                    print(f"O modelo é {item['modelo']}, tem {item['potencia']} cavalos de potência. A placa é "
                          f"{item['placa'].upper()} e o valor: R$ {item['valor']}. O número do chassi é "
                          f"{item['chassi']}. Foi fabricado em {item['data-fabricação']} na cor {item['cor']}.")
                elif opcao == 'camionete':
                    print(f"O modelo é {item['modelo']}, possui {item['portas']} portas e {item['potencia']} "
                          f"cavalos de potência. A placa é {item['placa'].upper()} e o valor: R$ {item['valor']}. "
                          f"Foi fabricado em {item['data-fabricação']} na cor {item['cor']}. O tamanho da caçamba é de "
                          f"{item['cacamba']} litros e a numeração do chassi é {item['chassi']}.")
                return True
        else:
            print('\033[1;91mVeículo não encontrado\033[0;0m. Verifique a numeração do chassi e tente novamente.')

    @staticmethod
    def alterar_info_veiculo(opcao, chassi, type_info, nova_info):
        if opcao not in tipos_veiculos:
            print('\033[1;91mOpção de veículo inválida.\033[0;0m')
        for item in tipos_veiculos.get(opcao):
            if chassi == item['chassi']:
                if type_info == 'cor':
                    item['cor'] = nova_info
                    print(f"Alteração de cor de veículo {item['modelo']} para {nova_info}.")
                if type_info == 'valor':
                    print(f"Alteração de valor de veículo {item['modelo']} para {nova_info}.")
                    item['valor'] = nova_info
