from db import Dbdrive
from antiplagiat import Checker

class Controller():

    #        Метод который получает данные из БД. Обрабатывает ошибки в случае их возникновения.
    #        А затем вызывает метод анализа входных данных от пользователя.
    #
    #
    # @param		input	Текст который ввел пользователь и требует анализа.
    #
    # @return
    #            Возвращает результат анализа введенного текста.
    #

    def comp(self, input):
        try:
            dbcon = Dbdrive()
            res = dbcon.getAll()
        except Exception as exp:
            return exp
        chk = Checker()
        return chk.analiz(input, res)

    ## @brief         Метод добавляет 1 запись, которую ввел пользователь, в БД.
    #
    #
    # @param		input	Текст который ввел пользователь и требует добавления в БД.
    #
    # @return
    #            Возвращает результат добавления в БД введенного текста.
    #

    def add(self, input):
        try:
            dbcon = Dbdrive()
            dbcon.add(input)
        except Exception as exp:
            return exp
        return 'Данный текст добавлен в БД'

