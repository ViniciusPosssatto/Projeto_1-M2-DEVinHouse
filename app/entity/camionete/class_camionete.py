from entity.class_veiculo import Veiculo
from data.infos import camionetes


class Camionete(Veiculo):
    def __init__(self, portas: int, cacamba: int, potencia: int, combustivel: str, data_fabr: str, modelo: str,
                 placa: str, valor: int, cor: str):
        super().__init__(data_fabr, modelo, placa, valor, cor)
        self.portas = portas
        self.tamanho_cacamba = cacamba
        self.potencia = potencia
        self.combustivel = combustivel
        self.__cor = 'roxa'
        self.keys = ['potencia', 'portas', 'cacamba', 'combustivel', 'chassi', 'data-fabricação', 'modelo', 'placa',
                     'valor', 'cpf', 'cor']

    def salvar_camionete(self):
        valores = [self.potencia, self.portas, self.tamanho_cacamba, self.combustivel, self.chassi, self.data_fabr,
                   self.modelo, self.placa, self.valor, self.cpf, self.__cor]
        data = dict(zip(self.keys, valores))
        camionetes.append(data)
        return True
