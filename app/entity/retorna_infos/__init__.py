from data.infos import carros, camionetes, motosTriciclos, historico_vendas


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