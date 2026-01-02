def month_to_season(month_number):
    seasons = {
        1: 'Зима',
        2: 'Зима',
        3: 'Весна',
        4: 'Весна',
        5: 'Весна',
        6: 'Лето',
        7: 'Лето',
        8: 'Лето',
        9: 'Осень',
        10: 'Осень',
        11: 'Осень',
        12: 'Зима'
    }

    return seasons.get(month_number, 'Ошибка ввода')

month_input = int(input('Введите номер месяца (1-12): '))
season_name = month_to_season(month_input)

print(f'{month_input}-й месяц соответствует сезону "{season_name}"')