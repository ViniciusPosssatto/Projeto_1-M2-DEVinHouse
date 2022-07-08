from data.infos import carros, camionetes, motosTriciclos, historico_vendas
from entity.class_veiculo import tipos_veiculos


class RetornaInfos:

    @staticmethod
    def retorna_todas_vendas():
        for i in historico_vendas:
            print(f"Veiculo modelo {i['infos veiculo']['modelo']}, fabricado em {i['infos veiculo']['data-fabricação']}"
                  f" foi vendido a um valor de R$ {i['valor de venda']} no dia {i['data da venda']}.")

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
                print(f"Modelo: {item['modelo']} - Portas: {item['portas']} - Potência: {item['potencia']} "
                      f"cavalos - Placa: {item['placa'].upper()} - Valor: R$ {item['valor']}. "
                      f"Data fabricação: {item['data-fabricação']} - Cor {item['cor']} - Chassi: {item['chassi']}.")
            elif tipo == 'moto':
                print(f"Modelo: {item['modelo']} - Rodas: {item['rodas']} - Potência: {item['potencia']} "
                      f"cavalos - Placa: {item['placa'].upper()} - Valor: R$ {item['valor']}. "
                      f"Data fabricação: {item['data-fabricação']} - Cor {item['cor']} - Chassi: {item['chassi']}.")
            elif tipo == 'camionete':
                print(f"Modelo: {item['modelo']} - Portas: {item['portas']} - Potência: {item['potencia']} "
                      f"cavalos - Placa: {item['placa'].upper()} - Valor: R$ {item['valor']}. "
                      f"Data fabricação: {item['data-fabricação']} - Cor {item['cor']} - Chassi: {item['chassi']} - "
                      f"Caçamba: {item['cacamba']} litros.")

    @staticmethod
    def retorna_vendido_maior_valor():
        maior = 0
        item = ' '
        for i in historico_vendas:
            if i['valor de venda'] > maior:
                maior = i['valor de venda']
                item = i
        return print(f"O veículo vendido pelo maior valor foi um(a) {item['tipo']}, modelo "
                     f"{item['infos veiculo']['modelo']}, no valor de R${item['valor de venda']}.")

    @staticmethod
    def retorna_vendido_menor_valor():
        menor = 999999999
        item = ' '
        for i in historico_vendas:
            if i['valor de venda'] < menor:
                menor = i['valor de venda']
                item = i
        return print(f"O veículo vendido pelo menor valor foi um(a) {item['tipo']}, modelo "
                     f"{item['infos veiculo']['modelo']}, no valor de R${item['valor de venda']}")
