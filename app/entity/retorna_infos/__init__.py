from data import carros, camionetes, motosTriciclos, historico_vendas
from entity.class_veiculo import tipos_veiculos


class RetornaInfos:

    @staticmethod
    def retorna_todas_vendas():
        print(f"{'MODELO'.center(15)}|{'DATA-FABRICAÇÃO'.center(20)}|{'CHASSI'.center(15)}|{'PLACA'.center(15)}|"
              f"{'VALOR'.center(15)}|{'COR'.center(15)}|{'POTÊNCIA'.center(15)}|{'DATA-VENDA'.center(15)}|"
              f"{'VEÍCULO'.center(20)}")
        for i in historico_vendas:
            print(f"{i['infos veiculo']['modelo'].center(15)} |{i['infos veiculo']['data-fabricação'].center(20)}|"
                  f"{i['infos veiculo']['chassi'].center(15)}|{i['infos veiculo']['placa'].center(15)}|   R$"
                  f"  {i['valor de venda']}   |{i['infos veiculo']['cor'].center(15)}|    "
                  f"  {i['infos veiculo']['potencia']}      |{i['data da venda'].center(15)}|{i['tipo'].center(20)}")

    @staticmethod
    def retorna_todos_disponiveis():
        print(f" {'MODELO'.center(15)} | {'DATA-FABRICAÇÃO'.center(20)} | {'CHASSI'.center(15)}")
        for i in motosTriciclos:
            print(f" {i['modelo'].center(15)} | {i['data-fabricação'].center(20)} | {i['chassi'].center(15)}Moto")
        for i in carros:
            print(f" {i['modelo'].center(15)} | {i['data-fabricação'].center(20)} | {i['chassi'].center(15)}Carro")
        for i in camionetes:
            print(f" {i['modelo'].center(15)} | {i['data-fabricação'].center(20)} | {i['chassi'].center(15)}Camionete")

    @staticmethod
    def retorna_veiculos_por_tipo(tipo):
        if tipo not in tipos_veiculos:
            print('Opção de veículo inválida.')
        for item in tipos_veiculos.get(tipo):
            if tipo == 'carro':
                print(f"\nModelo: {item['modelo']} - Portas: {item['portas']} - Potência: {item['potencia']} "
                      f"cavalos - Placa: {item['placa'].upper()} - Valor: R$ {item['valor']}. "
                      f"Data fabricação: {item['data-fabricação']} - Cor: {item['cor']} - Chassi: {item['chassi']}.")
            elif tipo == 'moto':
                print(f"\nModelo: {item['modelo']} - Rodas: {item['rodas']} - Potência: {item['potencia']} "
                      f"cavalos - Placa: {item['placa'].upper()} - Valor: R$ {item['valor']}. "
                      f"Data fabricação: {item['data-fabricação']} - Cor: {item['cor']} - Chassi: {item['chassi']}.")
            elif tipo == 'camionete':
                print(f"\nModelo: {item['modelo']} - Portas: {item['portas']} - Potência: {item['potencia']} "
                      f"cavalos - Placa: {item['placa'].upper()} - Valor: R$ {item['valor']}. "
                      f"Data fabricação: {item['data-fabricação']} - Cor: {item['cor']} - Chassi: {item['chassi']} - "
                      f"Caçamba: {item['cacamba']} litros.")

    @staticmethod
    def retorna_vendido_maior_valor():
        maior = sorted(historico_vendas, key=lambda value: value["valor de venda"], reverse=True)
        item = maior[0]
        return print(f"O veículo vendido pelo maior valor foi um(a) {item['tipo']}, modelo "
                     f"{item['infos veiculo']['modelo']}, no valor de R${item['valor de venda']}.")

    @staticmethod
    def retorna_vendido_menor_valor():
        menor = sorted(historico_vendas, key=lambda value: value["valor de venda"], reverse=False)
        item = menor[0]
        return print(f"O veículo vendido pelo menor valor foi um(a) {item['tipo']}, modelo "
                     f"{item['infos veiculo']['modelo']}, no valor de R${item['valor de venda']}")

    @staticmethod
    def retorna_resultado():
        total_valor_base = 0
        total_valor_venda = 0
        for item in historico_vendas:
            total_valor_base += item['infos veiculo']['valor']
            total_valor_venda += item['valor de venda']
        total = total_valor_venda - total_valor_base
        if total > 0:
            resultado = '\033[1;92mlucro\033[0;0m'
        else:
            resultado = '\033[1;91mprejuízo\033[0;0m'
        return print(f'Atualmente a empresa tem um {resultado} de R${total:.2f} nas vendas de veículos.')

    @staticmethod
    def retorna_todos_veiculos():

        print(f"""______________________________________________________________________________
    DISPONÍVEIS:
{'MODELO'.center(15)}  | {'DATA-FABRICAÇÃO'.center(20)} | {'CHASSI'.center(15)}| {'TIPO'.center(15)}""")
        for i in motosTriciclos:
            print(f" {i['modelo'].center(15)} | {i['data-fabricação'].center(20)} | {i['chassi'].center(15)}|  Moto")
        for i in carros:
            print(f" {i['modelo'].center(15)} | {i['data-fabricação'].center(20)} | {i['chassi'].center(15)}|  Carro")
        for i in camionetes:
            print(
                f" {i['modelo'].center(15)} | {i['data-fabricação'].center(20)} | {i['chassi'].center(15)}|  Camionete")
        print(f""" ______________________________________________________________________________
    VENDIDOS:
{'MODELO'.center(15)}  | {'DATA-FABRICAÇÃO'.center(20)} | {'CHASSI'.center(15)}| {'TIPO'.center(15)}""")
        for i in historico_vendas:
            print(f" {i['infos veiculo']['modelo'].center(15)} | {i['infos veiculo']['data-fabricação'].center(20)} | "
                  f"{i['infos veiculo']['chassi'].center(15)}|{i['tipo'].center(15)}")
