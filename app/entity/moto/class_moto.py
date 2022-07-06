from entity.class_veiculo import Veiculo

from data.infos import motosTriciclos


class MotoTriciclo(Veiculo):
    def __init__(self):
        super().__init__()
        self.potencia = None
        self.rodas = None
        self.keys = ['potencia', 'rodas', 'chassi', 'data_fabricação', 'modelo', 'placa', 'valor', 'cpf', 'cor']

    def cadastrar_mototriciclo(self):
        super().cadastrar_veiculo()
        self.potencia = int(input('Digite a potencia: '))
        self.rodas = int(input('Digite o número de rodas: '))
        self.salvar_mototriciclo()

    def salvar_mototriciclo(self):
        valores = [self.potencia, self.rodas, self.chassi, self.data_fabr, self.modelo, self.placa, self.valor,
                   self.cpf, self.cor]
        data = dict(zip(self.keys, valores))
        motosTriciclos.append(data)
