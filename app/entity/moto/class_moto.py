from app.entity.class_veiculo import Veiculo


class MotoTriciclo(Veiculo):
    def __init__(self, potencia: int, rodas: int, chassi: str, data_fabr: str, modelo: str, placa: str, valor: int):
        super().__init__(chassi, data_fabr, modelo, placa, valor)
        self.potencia = potencia
        self.rodas = rodas
