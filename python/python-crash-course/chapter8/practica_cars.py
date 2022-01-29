from matplotlib import markers


def make_car(color, year,**car_info):
    car_info['color'] = color
    car_info['year'] = year

    return car_info

car = make_car('green','1960', motor = 6, tipo = 'Hibrido')

print(car)
