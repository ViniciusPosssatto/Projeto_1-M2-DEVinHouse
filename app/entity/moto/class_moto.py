from entity.class_veiculo import Veiculo
from data.infos import motosTriciclos


class MotoTriciclo(Veiculo):
    def __init__(self, potencia: int, rodas: int, data_fabr: str, modelo: str, placa: str, valor: int, cor: str):
        super().__init__(data_fabr, modelo, placa, valor, cor)
        self.potencia = potencia
        self.rodas = rodas
        self.keys = ['potencia', 'rodas', 'chassi', 'data-fabricação', 'modelo', 'placa', 'valor', 'cpf', 'cor']

    def salvar_mototriciclo(self):
        valores = [self.potencia, self.rodas, self.chassi, self.data_fabr, self.modelo, self.placa, self.valor,
                   self.cpf, self.cor]
        data = dict(zip(self.keys, valores))
        motosTriciclos.append(data)
        return True
