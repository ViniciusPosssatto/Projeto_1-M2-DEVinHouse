from datetime import date


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
