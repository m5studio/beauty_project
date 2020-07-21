from apps.services.models import Services

"""
Ногтевой сервис
    Маникюр
        'Классический',
        'Европейский',
        'Обрезной',
        'Комбинированный',
        'Аппаратный',
        'Кл. маник+гель лак',
        'Мужской маникюр',
        'Укрепление акрилом',
        'Ремонт ногтя',
        'Выравнивание ногт. Пластины',
        'Наращивание ногтей',
        'Наращивание гелем ногтя',
        'Снятие геля',
        'Снятие гель-лака',
        'Снятие лака',
        'Градиент(1/все)',
        'Френч классический',
        'Френч цветной',
        'Френч обратный',
        'Лунки',
        'Кошачий глаз',
        'Втирка(1/все)',
        'Стразы',
        'Рисунки',
        'Наклейки',
        'Матовое покрытие',
        'Парафинотерапия',
    Педикюр
        'Классический',
        'Европейский',
        'Аппаратный',
        'Покрытие гель-лак',
        'Покрытие лак',
        'Кл.пед+гель лак',
        'Удаление натоптышей',
        'Ремонт ногтя',
        'Наращивание гелем',
        'Снятие гель-лака',
        'Мужской педикюр',
    Сеты
        'Классический маникюр + классический педикюр + гель лак',
        'Классический маникюр + гель лак',
        'Классический педикюр + гель лак',
=============================
Парикмахерский зал
    Стрижка
        Умная стрижка
        Стрижка жгутиками
        Подравнивание кончиков
        Челка
        Мужская стрижка
    Окрашивание
        Однотонное
        Тонирование
        Мелирование
        Сложное
        Черепаховое
        AirTouch
        Шатуш
        Балаяж
    Укладка
        Повседневная укладка
        Выпрямление
        Голливудские локоны
        Локоны на Брашенг
        Локоны на Плойку
        Вечерняя укладка
        Свадебная укладка
    Удаление волос
        Глубокое бикини
        Классическое бикини
        Подмышки
        Ноги до колен
        Ноги полностью
        Руки до локтя
        Руки полностью
        Усики
        Линия живота
        Лицо
    Ресницы и брови
        Наращивание уголков
            Неполный объем
            Наращивание 1D
            Наращивание 2D
            Наращивание 3D
            Наращивание 4D
            Наращивание 5D
        Лучики
        Цветные ресницы
        Снятие ресниц
        Ламинирование ресниц
        Ламинирование бровей
        Коррекция бровей
        Окрашивание бровей
        Окрашивание ресниц
        Окрашивание и коррекция бровей
"""
class AddDefaultContent:
    def _addRootService(self, root_service_name: str, parent_name=None: str):
        try:
            root_service = Services.objects.get(name=root_service_name)
            print(f'Услуга "{root_service}" уже существует')
        except Exception as e:
            root_service = Services.objects.create(name=root_service_name)
            print(f'Услуга "{root_service}" создана!')

    # TODO:
    def _addChildService(self):
        pass

    def addServices(self):
        # nails_root = Services.objects.create(name="Ногтевой сервис")
        # manicure_root = Services.objects.create(name="Маникюр", parent=nails_root)
        # root = Services.objects.create(name="")
        # Services.objects.create(name="test", parent=root)

        self._addRootService("Ногтевой сервис")

        # try:
        #     nails_root = Services.objects.get(name="Ногтевой сервис")
        #     print(f'Услуга "{nails_root}" уже существует')
        # except Exception as e:
        #     nails_root = Services.objects.create(name="Ногтевой сервис")
        #     print(f'Услуга "{nails_root}" создана!')

        try:
            manicure_root = Services.objects.get(name="Маникюр", parent=nails_root)
            print(f'Услуга "{manicure_root}" уже существует')
        except Exception as e:
            manicure_root = Services.objects.create(name="Маникюр", parent=nails_root)
            print(f'Услуга "{manicure_root}" создана!')

        manicure = [
            'Классический',
            'Европейский',
            'Обрезной',
            'Комбинированный',
            'Аппаратный',
            'Кл. маник+гель лак',
            'Мужской маникюр',
            'Укрепление акрилом',
            'Ремонт ногтя',
            'Выравнивание ногт. Пластины',
            'Наращивание ногтей',
            'Наращивание гелем ногтя',
            'Снятие геля',
            'Снятие гель-лака',
            'Снятие лака',
            'Градиент(1/все)',
            'Френч классический',
            'Френч цветной',
            'Френч обратный',
            'Лунки',
            'Кошачий глаз',
            'Втирка(1/все)',
            'Стразы',
            'Рисунки',
            'Наклейки',
            'Матовое покрытие',
            'Парафинотерапия',
        ]
        for m in manicure:
            try:
                Services.objects.get(name=m)
                print(f'Услуга "{m}" уже существует')
            except Exception as e:
                # print(e)
                Services.objects.create(name=m, parent=manicure_root)
                print(f'Услуга "{m}" создана!')

        # Педикюр
        try:
            pedicure_root = Services.objects.get(name="Педикюр", parent=nails_root)
            print(f'Услуга "{pedicure_root}" уже существует')
        except Exception as e:
            pedicure_root = Services.objects.create(name="Педикюр", parent=nails_root)
            print(f'Услуга "{pedicure_root}" создана!')

        pedicure = [
            'Классический',
            'Европейский',
            'Аппаратный',
            'Покрытие гель-лак',
            'Покрытие лак',
            'Кл.пед+гель лак',
            'Удаление натоптышей',
            'Ремонт ногтя',
            'Наращивание гелем',
            'Снятие гель-лака',
            'Мужской педикюр',
        ]

        for p in pedicure:
            try:
                Services.objects.get(name=p)
                print(f'Услуга "{p}" уже существует')
            except Exception as e:
                # print(e)
                Services.objects.create(name=p, parent=pedicure_root)
                print(f'Услуга "{p}" создана!')

        # Сеты
        try:
            sets_root = Services.objects.get(name="Сеты", parent=nails_root)
            print(f'Услуга "{sets_root}" уже существует')
        except Exception as e:
            sets_root = Services.objects.create(name="Сеты", parent=nails_root)
            print(f'Услуга "{sets_root}" создана!')

        sets = [
            'Классический маникюр + классический педикюр + гель лак',
            'Классический маникюр + гель лак',
            'Классический педикюр + гель лак',
        ]

        for s in sets:
            try:
                Services.objects.get(name=s)
                print(f'Услуга "{s}" уже существует')
            except Exception as e:
                # print(e)
                Services.objects.create(name=s, parent=sets_root)
                print(f'Услуга "{s}" создана!')


    def addContent(self):
        self.addServices()