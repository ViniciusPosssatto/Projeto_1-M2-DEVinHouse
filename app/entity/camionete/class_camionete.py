from entity.class_veiculo import Veiculo


class Camionete(Veiculo):
    def __init__(self, portas: int, cacamba: int, potencia: int, combustivel: str, chassi: str, data_fabr: str,
                 modelo: str, placa: str, valor: int, cor='roxa'):
        super().__init__(chassi, data_fabr, modelo, placa, valor)
        self.portas = portas
        self.tamanho_cacamba = cacamba
        self.potencia = potencia
        self.combustivel = "diesel" if combustivel is True else 'gasolina'
        self.cor = cor
