from datetime import date
import re

from entity.class_veiculo import tipos_veiculos


def validar_data():
    atual_year = date.today().year
    atual_month = date.today().month
    atual_day = date.today().day
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    try:
        data = input('Digite a data de fabricação [ dd/mm/aa ]: ')
        d = data.split('/')[0]
        m = data.split('/')[1]
        y = data.split('/')[2]
        if 1 <= int(m) <= 12 and 1 <= int(d) <= day_count_for_month[int(m)] and \
                (int(y) <= atual_year or int(m) <= atual_month or int(d) <= atual_day):
            return data
        else:
            raise Exception
    except Exception as error:
        print(f'Formatação inválida.')
        validar_data()


def validar_placa(opcao):
    placa_valida = '[A-Z]{3}[0-9][0-9A-Z][0-9]{2}'
    placa = input('Digite a placa [ AAA11A11 ]: ').upper()
    if re.match(placa_valida, placa):
        for item in tipos_veiculos.get(opcao):
            if placa != item['placa']:
                return placa
            else:
                print('Placa já atribuída a um veículo.')
                return validar_placa(opcao)
    else:
        print('Formato de placa inválida.')
        return validar_placa(opcao)


def validar_rodas():
    rodas = ' '
    try:
        while rodas not in [2, 3]:
            rodas = int(input('Digite o número de rodas [2 ou 3]: '))
        return rodas
    except Exception:
        print('Valor deve ser numérico.')
        return validar_rodas()


def validar_portas():
    portas = ' '
    try:
        while portas not in [2, 3]:
            portas = int(input('Digite o número de portas [2 ou 3]: '))
        return portas
    except Exception:
        print('Valor deve ser numérico.')
        return validar_portas()


def validar_combustivel(opt):
    combustivel = ' '
    tipo = {'carro': ['flex', 'gasolina'], 'camionete': ['diesel', 'gasolina']}
    try:
        while combustivel not in tipo.get(opt):
            combustivel = input(f'Qual o tipo de combustível{tipo.get(opt)}: ')
        return combustivel
    except Exception:
        print(f"Combustível deve ser '{tipo.get(opt)}'.")
        return validar_combustivel(opt)


def validar_potencia():
    true = False
    while True:
        potencia = input('Digite a potência do veículo: ')
        if potencia.isnumeric():
            true = True
        else:
            print('O valor deve ser um número inteiro.')
        if true:
            break
    return int(potencia)


def validar_valor():
    valor = ' '
    try:
        while not valor.isnumeric():
            valor = float(input('Digite o valor: R$ '))
            return int(valor)
    except Exception:
        print('O valor deve ser numérico.')
        return validar_valor()


def validar_cacamba():
    valor = 0
    try:
        while not int(valor):
            valor = input('Qual o tamanho da caçamba(litros): ')
            return int(valor)
    except Exception:
        print('O valor deve ser numérico.')
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

