from data.infos import carros, camionetes, motosTriciclos


class Veiculo:

    def __init__(self, chassi: str, data_fabr: str, modelo: str, placa: str, valor: int, cpf: int = 0):
        self.vendido = False
        pass

    def vender_veiculo(self):
        pass

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

