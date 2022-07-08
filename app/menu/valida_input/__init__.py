from datetime import date
import re

from entity.class_veiculo import tipos_veiculos


def validar_data():
    atual_year = date.today().year
    atual_month = date.today().month
    atual_day = date.today().day
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    try:
        data = input('Digite a data de fabricação [ dd/mm/aaaa ]: ').strip()
        d = data.split('/')[0]
        m = data.split('/')[1]
        y = data.split('/')[2]
        if 1 <= int(m) <= 12 and 1 <= int(d) <= day_count_for_month[int(m)] and \
                (int(y) <= atual_year or int(m) <= atual_month or int(d) <= atual_day):
            return data
        else:
            raise Exception
    except Exception as error:
        print(f'\033[1;91mData inválida. Data deve ser anterior a atual ou verifique o formato.\033[0;0m')
        return validar_data()


def validar_placa(opcao):
    placa_valida = '[A-Z]{3}[0-9][0-9A-Z][0-9]{2}'
    placa = input('Digite a placa [ AAA11A11 ]: ').strip().upper()
    if re.match(placa_valida, placa):
        for item in tipos_veiculos.get(opcao):
            if placa != item['placa']:
                return placa
            else:
                print('\033[1;93mPlaca já atribuída a um veículo.\033[0;0m')
                return validar_placa(opcao)
    else:
        print('\033[1;91mFormato de placa inválida.\033[0;0m')
        return validar_placa(opcao)


def validar_rodas():
    rodas = ' '
    try:
        while rodas not in [2, 3]:
            rodas = int(input('Digite o número de rodas [2 ou 3]: '))
        return rodas
    except Exception:
        print('\033[1;91mValor deve ser numérico.\033[0;0m')
        return validar_rodas()


def validar_portas():
    portas = ' '
    try:
        while portas not in [2, 3, 4, 5, 6]:
            portas = int(input('Digite o número de portas [2 a 6]: '))
        return portas
    except Exception:
        print('\033[1;91mValor deve ser numérico.\033[0;0m')
        return validar_portas()


def validar_combustivel(opt):
    combustivel = ' '
    tipo = {'carro': ['flex', 'gasolina'], 'camionete': ['diesel', 'gasolina']}
    try:
        while combustivel not in tipo.get(opt):
            combustivel = input(f'Qual o tipo de combustível{tipo.get(opt)}: ').strip()
        return combustivel
    except Exception:
        print(f"\033[1;91mCombustível deve ser '{tipo.get(opt)}'.\033[0;0m")
        return validar_combustivel(opt)


def validar_potencia():
    true = False
    while True:
        potencia = input('Digite a potência do veículo: ').strip()
        if potencia.isnumeric():
            true = True
        else:
            print('\033[1;91mO valor deve ser um número inteiro.\033[0;0m')
        if true:
            break
    return int(potencia)


def validar_valor():
    valor = False
    try:
        while not valor:
            valor = float(input('Digite o valor: R$ '))
        return valor
    except Exception as error:
        print(f'\033[1;91mO valor deve ser numérico.\033[0;0m')
        return validar_valor()


def validar_cacamba():
    valor = 0
    try:
        while not int(valor):
            valor = input('Qual o tamanho da caçamba(litros): ').strip()
            return int(valor)
    except Exception:
        print('\033[1;91mO valor deve ser numérico.\033[0;0m')
        return validar_cacamba()


def validar_options(opt):
    sub_option = ' '
    options = {'a': [1, 2, 3, 4, 5, 0], 'b': [1, 2, 3, 4, 0], 'c': [1, 2, 3, 0], 'd': [1, 2, 0]}
    try:
        while sub_option not in options.get(opt):
            sub_option = int(input('Digite a opção desejada: '))
        return sub_option
    except Exception:
        return validar_options(opt)


def validar_opcao():
    opcao = ' '
    while opcao not in ['moto', 'carro', 'camionete']:
        opcao = input('Informe qual tipo de veículo [moto, carro, camionete]: ').strip()
    return opcao


def validar_chassi(opt):
    chassi = input('Digite a numeração do chassi: ').strip()
    for item in tipos_veiculos.get(opt):
        if chassi == item['chassi']:
            return chassi
    else:
        return validar_chassi(opt)


def validar_cpf():
    cpf = ' '
    try:
        while len(cpf) != 11:
            cpf = input('Digite o CPF do comprador: ').strip()
        return int(cpf)
    except Exception:
        print('\033[1;91mCPF não é válido! Tente novamente.\033[0;0m')
        return validar_cpf()
