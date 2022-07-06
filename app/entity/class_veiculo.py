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
        self.tipos_veiculos = ['carro', 'moto', 'camionete']
        self.tipos_veiculos_2 = {'carro': carros, 'moto': motosTriciclos, 'camionete': camionetes}

    def vender_veiculo(self, opcao, chassi, cpf, valor):
        if opcao not in self.tipos_veiculos_2:
            print('Opção inválida.')
        veiculo = None
        for car in self.tipos_veiculos_2.get(opcao):
            if chassi == car['chassi']:
                car['cpf'] = cpf
                print(f"O carro modelo {car['modelo']} cuja placa é {car['placa'].upper()}, foi vendido no valor de"
                      f" R$ {car['valor']} no dia {self.data_atual}.")
                veiculo = car
        Historico().save_transation(veiculo, cpf, valor, self.data_atual)

    @staticmethod
    def listar_info_veiculo(opcao, chassi):
        if opcao == 'carro':
            for car in carros:
                if chassi == car['chassi']:
                    print(f"O modelo é {car['modelo']}, possui {car['portas']} portas e {car['potencia']} "
                          f"cavalos de potência. A placa é {car['placa'].upper()} e o valor: R$ {car['valor']}. "
                          f"Foi fabricado em {car['data-fabricação']} na cor {car['cor']}.")
        if opcao == 'moto':
            for moto in motosTriciclos:
                print(moto)
        if opcao == 'camionete':
            for camionete in camionetes:
                print(camionete)
        else:
            print('Opção inválida.')

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
    def save_transation(info_veiculo, cpf, valor, data):
        historico_vendas.append({'infos veiculo': info_veiculo, 'cpf': cpf, 'valor de venda': valor,
                                 'data da venda': data})


print(str(uuid4()).split('-')[0])
