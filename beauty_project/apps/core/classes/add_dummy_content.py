import random

from django.utils import timezone

from django.contrib.auth.models import Group

from apps.services.models import Services
from apps.account.models import Account

from apps.salon.models.salon import Salon
from apps.salon.models.work_schedule import WorkSchedule
from apps.salon.models.employee import Employee
from apps.salon.models.client_appointment import ClientAppointment


class AddDummyContent:
    # Create Services from array
    def _createSubServices(self, arr, obj):
        for item in arr:
            try:
                Services.objects.get(name=item)
                print(f'Услуга "{item}" уже существует')
            except Exception as e:
                Services.objects.create(name=item, parent=obj)
                print(f'Услуга "{item}" создана!')


    def addServices(self):
        # Ногтевой сервис
        try:
            nails_root = Services.objects.get(name="Ногтевой сервис")
            print(f'Услуга "{nails_root}" уже существует')
        except Exception as e:
            nails_root = Services.objects.create(name="Ногтевой сервис")
            print(f'Услуга "{nails_root}" создана!')

        # Маникюр
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

        self._createSubServices(manicure, manicure_root)

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

        self._createSubServices(pedicure, pedicure_root)

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

        self._createSubServices(sets, sets_root)

        # Парикмахерский зал
        try:
            barber_root = Services.objects.get(name="Парикмахерский зал")
            print(f'Услуга "{barber_root}" уже существует')
        except Exception as e:
            barber_root = Services.objects.create(name="Парикмахерский зал")
            print(f'Услуга "{barber_root}" создана!')

        # Стрижка
        try:
            haircut_root = Services.objects.get(name="Стрижка", parent=barber_root)
            print(f'Услуга "{haircut_root}" уже существует')
        except Exception as e:
            haircut_root = Services.objects.create(name="Стрижка", parent=barber_root)
            print(f'Услуга "{haircut_root}" создана!')

        haircut = [
            'Умная стрижка',
            'Стрижка жгутиками',
            'Подравнивание кончиков',
            'Челка',
            'Мужская стрижка',
        ]

        self._createSubServices(haircut, haircut_root)

        # Окрашивание
        try:
            haircoloring_root = Services.objects.get(name="Окрашивание", parent=barber_root)
            print(f'Услуга "{haircoloring_root}" уже существует')
        except Exception as e:
            haircoloring_root = Services.objects.create(name="Окрашивание", parent=barber_root)
            print(f'Услуга "{haircoloring_root}" создана!')

        haircoloring = [
            'Однотонное',
            'Тонирование',
            'Мелирование',
            'Сложное',
            'Черепаховое',
            'AirTouch',
            'Шатуш',
            'Балаяж',
        ]

        self._createSubServices(haircoloring, haircoloring_root)

        # Укладка
        try:
            hairstyling_root = Services.objects.get(name="Укладка", parent=barber_root)
            print(f'Услуга "{hairstyling_root}" уже существует')
        except Exception as e:
            hairstyling_root = Services.objects.create(name="Укладка", parent=barber_root)
            print(f'Услуга "{hairstyling_root}" создана!')

        hairstyling = [
            'Повседневная укладка',
            'Выпрямление',
            'Голливудские локоны',
            'Локоны на Брашенг',
            'Локоны на Плойку',
            'Вечерняя укладка',
            'Свадебная укладка',
        ]

        self._createSubServices(hairstyling, hairstyling_root)

        # Удаление волос
        try:
            hairremoving_root = Services.objects.get(name="Удаление волос", parent=barber_root)
            print(f'Услуга "{hairremoving_root}" уже существует')
        except Exception as e:
            hairremoving_root = Services.objects.create(name="Удаление волос", parent=barber_root)
            print(f'Услуга "{hairremoving_root}" создана!')

        hairremoving = [
            'Глубокое бикини',
            'Классическое бикини',
            'Подмышки',
            'Ноги до колен',
            'Ноги полностью',
            'Руки до локтя',
            'Руки полностью',
            'Усики',
            'Линия живота',
            'Лицо',
        ]

        self._createSubServices(hairremoving, hairremoving_root)

        # Ресницы и брови
        try:
            eyelashes_eyebrows_root = Services.objects.get(name="Ресницы и брови", parent=barber_root)
            print(f'Услуга "{eyelashes_eyebrows_root}" уже существует')
        except Exception as e:
            eyelashes_eyebrows_root = Services.objects.create(name="Ресницы и брови", parent=barber_root)
            print(f'Услуга "{eyelashes_eyebrows_root}" создана!')

        eyelashes_eyebrows = [
            'Лучики',
            'Цветные ресницы',
            'Снятие ресниц',
            'Ламинирование ресниц',
            'Ламинирование бровей',
            'Коррекция бровей',
            'Окрашивание бровей',
            'Окрашивание ресниц',
            'Окрашивание и коррекция бровей',
        ]

        self._createSubServices(hairremoving, eyelashes_eyebrows_root)

        # Ресницы и брови => Наращивание уголков
        try:
            increase_angles_root = Services.objects.get(name="Наращивание уголков", parent=eyelashes_eyebrows_root)
            print(f'Услуга "{increase_angles_root}" уже существует')
        except Exception as e:
            increase_angles_root = Services.objects.create(name="Наращивание уголков", parent=eyelashes_eyebrows_root)
            print(f'Услуга "{increase_angles_root}" создана!')

        increase_angles = [
            'Неполный объем',
            'Наращивание 1D',
            'Наращивание 2D',
            'Наращивание 3D',
            'Наращивание 4D',
            'Наращивание 5D',
        ]

        self._createSubServices(increase_angles, increase_angles_root)


    def addSalons(self):
        salons_count = Salon.objects.all().count()
        if salons_count == 0:
            i = 1
            for _ in range(10):
                salon = Salon(active=True, \
                                name=f"Salon name {i}", \
                                description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris molestie nisl erat, in auctor purus vehicula vel. Mauris pharetra maximus sapien non bibendum. Pellentesque placerat mauris at dictum lobortis. Nulla consectetur tortor at magna faucibus suscipit. Vivamus aliquam lorem sem, in porta orci commodo sit amet.", \
                                phone="+79990001100", \
                                email="salonmail@gmail.com", \
                                site_url="https://google.com", \
                                # owner=, \
                            )
                salon.save()
                print(f"Салон {salon.name} создан")
                i += 1


    def addSalonsWorkSchedules(self):
        salons = Salon.objects.all()
        for salon in salons:
            i = 0
            if not WorkSchedule.objects.filter(salon=salon).exists():
                for _ in range(7):
                    salon_obj = Salon.objects.get(id=salon.id)
                    ws = WorkSchedule(salon=salon_obj, \
                                        week_day=WorkSchedule.WEEK_DAYS[i][0], \
                                        # working_hours_from="09:00:00", \
                                        working_hours_to="18:00:00", \
                                    )
                    ws.save()
                    print(f'Рабочий график для салона "{ws.salon.name}" на {ws.get_week_day_display()} создан')
                    i += 1
            else:
                print(f'Рабочий график для салона "{salon.name}" уже существует')


    def addSalonsEmployees(self):
        surnames_arr = ['Иванов', 'Петров', 'Сидоров', 'Андреев', 'Лебедев']
        names_arr = ['Иван', 'Кирилл', 'Игорь', 'Артем', 'Павел']
        patronymics_arr = ['Иванович', 'Алексеевич', 'Игоревич', 'Семенович', 'Владимирович']

        salons = Salon.objects.all()
        for salon in salons:
            i = 0
            if not Employee.objects.filter(salon=salon).exists():
                for _ in range(10):
                    salon_obj = Salon.objects.get(id=salon.id)
                    employee = Employee(active=True, \
                                        salon=salon_obj, \
                                        surname=random.choice(surnames_arr), \
                                        name=random.choice(names_arr), \
                                        patronymic=random.choice(patronymics_arr), \
                                    )
                    employee.save()
                    # Set Services by it's id's
                    employee.services.set([1, 2, 3, 4, 5, 6, 7, 8, 9])
                    print(f'Сотрудник {employee.surname} {employee.name} {employee.patronymic} создан')
            else:
                print(f'Сотрудник уже существует')


    def addClientAppointments(self):
        users_client = Account.objects.filter(groups__name='Client')

        for user in users_client:
            user_instance = Account.objects.get(id=user.id)
            employee_instance = Employee.objects.get(id=random.choice([1, 2, 3]))
            salon_instance = Salon.objects.get(id=random.choice([1, 2, 3]))

            if ClientAppointment.objects.all().count() == 0:
                for _ in range(5):
                    client_appointment = ClientAppointment(client=user_instance, \
                                                            employee=employee_instance, \
                                                            # datetime="2020-08-14 16:30:00", \
                                                            datetime=timezone.now(), \
                                                            comment="Some client comment", \
                                                        )
                    client_appointment.save()
                    client_appointment.services.set(["1", "2", "3"])
                    print(f"Запись в салон {client_appointment.id} создана!")
            else:
                print("Записи Клиентов в Салон уже созданы")


    # Init creation
    def createDummyContent(self):
        self.addServices()
        self.addSalons()
        self.addSalonsWorkSchedules()
        self.addSalonsEmployees()
        # self.addClientAppointments()