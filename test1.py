data = {
    '27-04-003-01': {
        'Устройство оснований и покрытий из песчано-гравийных или щебеночно-песчаных смесей:': 'однослойных толщиной 12 см',
        'Resources': {
            'Затраты труда рабочих (Средний разряд - 2,8)': '46.18',
            'Автогрейдеры среднего типа, мощность 99 кВт (135 л.с.)': '2.64',
            'Погрузчики одноковшовые универсальные фронтальные пневмоколесные, номинальная вместимость основного ковша 2,6 м3, грузоподъемность 5 т': '5.92',
            'Катки самоходные гладкие вибрационные, масса 8 т': '8.3',
            'Катки самоходные гладкие вибрационные, масса 13 т': '7.66',
            'Катки самоходные пневмоколесные статические, масса 30 т': '0.59',
            'Машины поливомоечные, вместимость цистерны 6 м3': '1.63',
            'Вода': '10.5'
        }
    }
}

# Составление строкового представления данных
result_str = ""
for key, value in data.items():
    result_str += f"Код работы: {key}\n"
    for k, v in value.items():
        if k != "Resources":
            result_str += f"{k}: {v}\n"
        else:
            result_str += "Ресурсы:\n"
            for resource_name, quantity in v.items():
                result_str += f"  {resource_name}: {quantity}\n"

print(result_str)