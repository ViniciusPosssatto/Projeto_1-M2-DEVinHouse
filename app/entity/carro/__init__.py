from entity.class_veiculo import Veiculo
from data import carros


class Carro(Veiculo):
    def __init__(self, portas: int, combustivel: str, potencia: int, data_fabr: str, modelo: str, placa: str,
                 valor: int, cor: str):
        super().__init__(data_fabr, modelo, placa, valor, cor)
        self.portas = portas
        self.combustivel = combustivel
        self.potencia = potencia
        self.keys = ['potencia', 'portas', 'combustivel', 'chassi', 'data-fabricação', 'modelo', 'placa', 'valor',
                     'cpf', 'cor']

    def salvar_carro(self):
        valores = [self.potencia, self.portas, self.combustivel, self.chassi, self.data_fabr, self.modelo, self.placa,
                   self.valor, self.cpf, self.cor]
        data = dict(zip(self.keys, valores))
        carros.append(data)
        return True
