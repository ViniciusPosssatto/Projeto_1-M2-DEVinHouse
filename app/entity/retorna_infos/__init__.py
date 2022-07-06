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
        for i in motosTriciclos:
            print(f"Moto/triciclo modelo {i['modelo']}, fabricado em {i['data-fabricação']}, com valor base de "
                  f"R$ {i['valor']}.")
        for i in carros:
            print(f"Carro modelo {i['modelo']}, fabricado em {i['data-fabricação']}, com valor base de "
                  f"R$ {i['valor']}.")
        for i in camionetes:
            print(f"Camionete modelo {i['modelo']}, fabricado em {i['data-fabricação']}, com valor base de "
                  f"R$ {i['valor']}.")

    @staticmethod
    def retorna_veiculos_por_tipo(tipo):
        if tipo not in tipos_veiculos:
            print('Opção de veículo inválida.')
        for item in tipos_veiculos.get(tipo):
            if tipo == 'carro':
                print(f"O modelo é {item['modelo']}, possui {item['portas']} portas e {item['potencia']} "
                      f"cavalos de potência. A placa é {item['placa'].upper()} e o valor: R$ {item['valor']}. "
                      f"Foi fabricado em {item['data-fabricação']} na cor {item['cor']}. O número do chassi é "
                      f"{item['chassi']}.")
            elif tipo == 'moto':
                print(f"O modelo é {item['modelo']}, tem {item['potencia']} cavalos de potência. A placa é "
                      f"{item['placa'].upper()} e o valor: R$ {item['valor']}. O número do chassi é "
                      f"{item['chassi']}. Foi fabricado em {item['data-fabricação']} na cor {item['cor']}.")
            elif tipo == 'camionete':
                print(f"O modelo é {item['modelo']}, possui {item['portas']} portas e {item['potencia']} "
                      f"cavalos de potência. A placa é {item['placa'].upper()} e o valor: R$ {item['valor']}. "
                      f"Foi fabricado em {item['data-fabricação']} na cor {item['cor']}. O tamanho da caçamba é de "
                      f"{item['cacamba']} litros e a numeração do chassi é {item['chassi']}.")
    