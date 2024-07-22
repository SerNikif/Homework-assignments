class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'Purple', 'ORANGE']

    def __init__(self, owner: str, model: str, color: str, e_p: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = e_p
        self._color = color

    def get_owner(self):
        return f'Владелец: {self.owner}'

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\n{self.get_owner()}')

    def set_color(self, new_color: str):
        help_list = []
        for farbe in self.__COLOR_VARIANTS:
            help_list.append(farbe.upper())
        if new_color not in help_list:
            print(f'Нельзя сменить цвет на {new_color}')
        else:
            self._color = new_color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
