from datetime import date

from data import historico_vendas


class Historico:

    def __init__(self):
        self.data_atual = date.today().strftime("%d/%m/%Y")

    def save_transation(self, info_veiculo, cpf, valor, tipo):
        historico_vendas.append({'infos veiculo': info_veiculo, 'cpf': cpf, 'valor de venda': valor,
                                 'data da venda': self.data_atual, 'tipo': tipo})
