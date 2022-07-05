from datetime import date
from data.infos import carros, camionetes, motosTriciclos, historico_vendas


class Veiculo:

    def __init__(self, chassi: str, data_fabr: str, modelo: str, placa: str, valor: int, cpf: int = 0):
        self.chassi = chassi
        self.data_fabr = data_fabr
        self.modelo = modelo
        self.placa = placa
        self.valor = valor
        self.info_veiculo = []
        self.data_atual = date.today().strftime("%d/%m/%y")
        self.cpf = cpf
        self.historico = Historico()

    def vender_veiculo(self, opcao, chassi, cpf, valor):
        if opcao == 'carro':
            for car in carros:
                if chassi == car['chassi']:
                    car['cpf'] = cpf
                    self.historico.save_transation(car, cpf, valor, self.data_atual)
                    print(f"O carro modelo {car['modelo']} cuja placa é {car['placa'].upper()}, foi vendido no valor de"
                          f" R$ {car['valor']} no dia {self.data_atual}.")
        if opcao == 'moto':
            for moto in motosTriciclos:
                print(moto)
        if opcao == 'camionete':
            for camionete in camionetes:
                print(camionete)
        else:
            print('Opção inválida.')

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

