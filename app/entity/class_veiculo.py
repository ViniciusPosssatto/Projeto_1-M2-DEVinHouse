from datetime import date
from uuid import uuid4

from data.infos import carros, camionetes, motosTriciclos, historico_vendas


data_atual = date.today().strftime("%d/%m/%y")
tipos_veiculos = {'carro': carros, 'moto': motosTriciclos, 'camionete': camionetes}


class Veiculo:

    def __init__(self):
        self.chassi = str(uuid4()).split('-')[0]
        self.data_fabr = None
        self.modelo = None
        self.placa = None
        self.valor = None
        self.cpf = 0
        self.cor = None

    def cadastrar_veiculo(self):
        self.modelo = input('Digite o modelo do veiculo: ')
        self.placa = input('Digite a placa (ex: dtt5i67): ')
        self.valor = input('Digite o valor: ')
        self.cor = input('Digite a cor predominante no veículo: ')
        self.data_fabr = input('Digite a data de fabricação [dd/mm/aa]: ')

    @staticmethod
    def vender_veiculo(opcao, chassi, cpf, valor):
        if opcao not in tipos_veiculos:
            print('Opção de veículo inválida.')
        veiculo = None
        for item in tipos_veiculos.get(opcao):
            if chassi == item['chassi']:
                item['cpf'] = cpf
                print(f"O veiculo modelo {item['modelo']} cuja placa é {item['placa'].upper()}, foi vendido no valor de"
                      f" R$ {item['valor']} no dia {data_atual}.")
                veiculo = item
                Historico().save_transation(veiculo, cpf, valor, data_atual, opcao)
                tipos_veiculos.get(opcao).remove(item)
            else:
                print('Chassi não corresponde a um veiculo.')

    @staticmethod
    def listar_info_veiculo(opcao, chassi):
        if opcao not in tipos_veiculos:
            print('Opção de veículo inválida.')
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
            else:
                print('Veículo não encontrado.')

    @staticmethod
    def alterar_info_veiculo(opcao, chassi, type_info, nova_info):
        if opcao not in tipos_veiculos:
            print('Opção de veículo inválida.')
        for item in tipos_veiculos.get(opcao):
            if chassi == item['chassi']:
                if type_info == 'cor':
                    item['cor'] = nova_info
                    print(f"Alteração de cor de veículo {item['modelo']} para {nova_info}.")
                if type_info == 'valor':
                    item['valor'] = nova_info


class Historico:

    @staticmethod
    def save_transation(info_veiculo, cpf, valor, data, tipo):
        historico_vendas.append({'infos veiculo': info_veiculo, 'cpf': cpf, 'valor de venda': valor,
                                 'data da venda': data, 'tipo': tipo})
