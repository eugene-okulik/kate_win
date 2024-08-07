# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры (объекты) цветов разных видов. Собрать букет
# (букет - еще один класс) с определением его стоимости. В букете цветы пусть хранятся
# в списке. Это будет список объектов.
#
# Для букета создать метод, который определяет время его увядания по среднему времени
# жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
#
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по
# среднему времени жизни) (и это тоже метод).
class Flower:
    stem = True
    bud = True

    def __init__(self, stem_length, color, pick_days, flower_price):
        self.stem_length = stem_length
        self.color = color
        self.pick_days = pick_days
        self.flower_price = flower_price
        self.freshness = 0


class Rose(Flower):
    life_span = 8
    name = 'rose'

    def __init__(self, stem_length, color, pick_days, flower_price):
        super().__init__(stem_length, color, pick_days, flower_price)
        self.freshness = (self.life_span - self.pick_days) / self.life_span


class Tulip(Flower):
    life_span = 5
    name = 'tulip'

    def __init__(self, stem_length, color, pick_days, flower_price):
        super().__init__(stem_length, color, pick_days, flower_price)
        self.freshness = (self.life_span - self.pick_days) / self.life_span


class Peony(Flower):
    life_span = 6
    name = 'peony'

    def __init__(self, stem_length, color, pick_days, flower_price):
        super().__init__(stem_length, color, pick_days, flower_price)
        self.freshness = (self.life_span - self.pick_days) / self.life_span


class Carnation(Flower):
    name = 'carnation'
    life_span = 10

    def __init__(self, stem_length, color, pick_days, flower_price):
        super().__init__(stem_length, color, pick_days, flower_price)
        self.freshness = (self.life_span - self.pick_days) / self.life_span


rose_1 = Rose(50, 'red', 1, 15)
carnation_1 = Carnation(40, 'white', 3, 10)
peony_1 = Peony(35, 'pink', 0, 12)
tulip_1 = Tulip(30, 'yellow', 4, 5)

rose_2 = Rose(50, 'pink', 4, 15)
carnation_2 = Carnation(40, 'violet', 5, 10)
peony_2 = Peony(35, 'white', 1, 12)
tulip_2 = Tulip(30, 'violet', 3, 5)

rose_3 = Rose(50, 'white', 5, 15)
carnation_3 = Carnation(40, 'red', 2, 10)
peony_3 = Peony(35, 'pink', 3, 12)
tulip_3 = Tulip(30, 'red', 2, 5)


class Bouquet:
    def __init__(self):
        self.flower_list = []

    def add_flower(self, flowers):
        if isinstance(flowers, list):
            self.flower_list.extend(flowers)
        else:
            self.flower_list.append(flowers)

    def bouquet_cost(self):
        print(f'Bouquet cost: {sum(flower.flower_price for flower in self.flower_list)}')

    def wilting_time(self):
        wilting_time = int(
            sum(flower.life_span - flower.pick_days for flower in self.flower_list) / len(self.flower_list)
        )
        print(f'Wilting time: {wilting_time}')

    def sort_flowers(self, by='freshness'):
        self.flower_list.sort(key=lambda flower: getattr(flower, by), reverse=(by == 'freshness'))
        sorted_flowers = ', '.join(f'{flower.name} - {getattr(flower, by)}' for flower in self.flower_list)
        print(f'Flowers sorted by {by}: {sorted_flowers}')

    def search_flowers(self, by, value):
        found_flowers = [flower for flower in self.flower_list if getattr(flower, by) == value]
        found_flowers_str = ', '.join(f'{flower.name} - {getattr(flower, by)}' for flower in found_flowers)
        print(f'Flowers with {by} = {value}: {found_flowers_str}')


bouquet_1 = Bouquet()

bouquet_1.add_flower(rose_1)
bouquet_1.add_flower(carnation_1)
bouquet_1.add_flower(peony_1)

bouquet_1.bouquet_cost()
bouquet_1.wilting_time()

bouquet_1.sort_flowers(by='color')
bouquet_1.search_flowers(by='life_span', value=8)

bouquet_2 = Bouquet()
flowers_for_bouquet_2 = [rose_1, rose_2, rose_3, carnation_1, carnation_3]
bouquet_2.add_flower(flowers_for_bouquet_2)

bouquet_2.search_flowers('color', 'pink')
bouquet_2.search_flowers('stem_length', 50)

bouquet_2.sort_flowers('color')
bouquet_2.sort_flowers('freshness')
bouquet_2.sort_flowers('flower_price')
bouquet_2.sort_flowers('stem_length')
