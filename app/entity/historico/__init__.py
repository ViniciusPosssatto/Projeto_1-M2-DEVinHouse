from data.infos import historico_vendas


class Historico:

    @staticmethod
    def save_transation(info_veiculo, cpf, valor, data, tipo):
        historico_vendas.append({'infos veiculo': info_veiculo, 'cpf': cpf, 'valor de venda': valor,
                                 'data da venda': data, 'tipo': tipo})