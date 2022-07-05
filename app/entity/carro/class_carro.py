from app.entity.class_veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, portas: int, combustivel: bool, potencia: int, chassi: str, data_fabr: str, modelo: str,
                 placa: str, valor: int):
        super().__init__(chassi, data_fabr, modelo, placa, valor)
        self.portas = portas
        self.combustivel = 'flex' if combustivel is True else 'gasolina'
        self.potencia = potencia
