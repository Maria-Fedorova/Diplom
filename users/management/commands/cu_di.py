from django.core.management import BaseCommand

from diary.models import Diary
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email="test23@ex.com")
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save()

        diary1 = Diary.objects.create(author=user, title="Два весёлых гуся", content="Жили у бабуси\n"
                                                                                   " Два весёлых гуся,\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Два весёлых гуся.\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Два весёлых гуся\n"
                                                                                   "Вытянули шеи\n"
                                                                                   "У кого длиннее\n"
                                                                                   "Один серый , другой белый ,-\n"
                                                                                   "Два весёлых гуся!\n"
                                                                                   "Мыли гуси лапки\n"
                                                                                   "В луже у канавки,\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Спрятались в канавке.\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Спрятались в канавке!\n"
                                                                                   "Вот кричит бабуся:\n"
                                                                                   "Ой, пропали гуси!\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Гуси мои, гуси!\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Гуси мои, гуси!\n"
                                                                                   "Выходили гуси,\n"
                                                                                   "Кланялись бабусе,\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Кланялись бабусе.\n"
                                                                                   "Один - серый, другой - белый,\n"
                                                                                   "Кланялись бабусе!\n")
        diary2 = Diary.objects.create(author=user, title="Оливье",
                                      content="Салат «Оливье» был изобретён в XIX веке московским ресторатором "
                                              "и шеф-поваром французского происхождения Люсьеном Оливье. "
                                              "Оригинальный рецепт включал дорогие и редкие для тех времён продукты, "
                                              "такие как рябчики, чёрная икра, лангустины и каперсы. "
                                              "Со временем ингредиенты упростились и удешевились, так появились "
                                              "более привычные компоненты: картофель, морковь, яйца, солёные огурцы"
                                              " и зелёный горошек.")
        diary3 = Diary.objects.create(author=user, title="Почему январь такой теплый", content="Не знаю")
        diary4 = Diary.objects.create(author=user, title="Оливье", content="Тут будет рецепт")
