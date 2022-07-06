from datetime import date
from uuid import uuid4

from data.infos import carros, camionetes, motosTriciclos, historico_vendas


class Veiculo:

    def __init__(self, data_fabr: str, modelo: str, placa: str, valor: int, cpf: int = 0):
        self.chassi = str(uuid4()).split('-')[0]
        self.data_fabr = data_fabr
        self.modelo = modelo
        self.placa = placa
        self.valor = valor
        self.data_atual = date.today().strftime("%d/%m/%y")
        self.cpf = cpf
        self.tipos_veiculos = {'carro': carros, 'moto': motosTriciclos, 'camionete': camionetes}

    def vender_veiculo(self, opcao, chassi, cpf, valor):
        if opcao not in self.tipos_veiculos:
            print('Opção de veículo inválida.')
        veiculo = None
        for item in self.tipos_veiculos.get(opcao):
            if chassi == item['chassi']:
                item['cpf'] = cpf
                print(f"O veiculo modelo {item['modelo']} cuja placa é {item['placa'].upper()}, foi vendido no valor de"
                      f" R$ {item['valor']} no dia {self.data_atual}.")
                veiculo = item
                Historico().save_transation(veiculo, cpf, valor, self.data_atual, opcao)
                self.tipos_veiculos.get(opcao).remove(item)
            else:
                print('Chassi não corresponde a um veiculo.')

    def listar_info_veiculo(, self, opcao, chassi):
        if opcao not in self.tipos_veiculos:
            print('Opção de veículo inválida.')
        for item in self.tipos_veiculos.get(opcao):
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
        if opcao == 'carro':
            for car in carros:
                if chassi == car['chassi']:
                    if type_info == 'cor':
                        car['cor'] = nova_info
                        print(f'Alteração de cor de veículo carro para {nova_info}.')
                    if type_info == 'valor':
                        car['valor'] = nova_info
        if opcao == 'moto':
            for moto in motosTriciclos:
                print(moto)
        if opcao == 'camionete':
            for camionete in camionetes:
                print(camionete)
        else:
            print('Opção inválida.')


class Historico:

    @staticmethod
    def save_transation(info_veiculo, cpf, valor, data, tipo):
        historico_vendas.append({'infos veiculo': info_veiculo, 'cpf': cpf, 'valor de venda': valor,
                                 'data da venda': data, 'tipo': tipo})



