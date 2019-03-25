import Stemmer

class Checker():

    ## @brief         Поиск самого похожего текста в массиве текстов.
    #
    #        Данный метод обрабатывает входные тексты и затем с помощью алгоритма шинглов находит самый похожий текст.
    #
    #
    # @param		_input	Текст для которого мы будем искать максимальное значение схожести.
    # @param		_texts	Массив текстов для поиска.
    #
    # @return
    #            Если найден хотя бы один хоть сколько нибудь похожий текст метод вернет текст, его название, а также
    #            значение схожести при использование алгоритма шинглов и расстояние Левенштейна.
    #

    def analiz(self, _input, _texts):
        name = ''
        ftext = ''
        shingMax = 0
        levensh = 0
        for text in _texts:
            cmp1 = self.genshingle(self.stemmer(_input))
            cmp2 = self.genshingle(self.stemmer(text[1]))
            tmp = self.compaire(cmp1,cmp2)
            if tmp > shingMax:
                shingMax = tmp
                name = text[0]
                ftext = text[1]
                levensh = self.levenshDist(_input.lower(), text[1].lower())
        if not (shingMax is 0):
            return name, ftext, shingMax, levensh
        else:
            return '', 'В БД нет похожих текстов.', 0, 0

    ## @brief         Вычисляет расстояние Левенштейна между входными строками.
    #
    #        Расстояние Левенштейна (редакционное расстояние, дистанция редактирования)
    #        — минимальное количество операций вставки одного символа,
    #        удаления одного символа и замены одного символа на другой,
    #        необходимых для превращения одной строки в другую.
    #        Измеряется для двух строк, широко используется в теории информации и компьютерной лингвистике.
    #
    #
    # @param		a	Первая строка для вычисления расстояния Левенштейна.
    # @param		b	Вторая строка для вычисления расстояния Левенштейна.
    #
    # @return
    #            Целочисленное значение характеризующее расстояние Левенштейна.
    #

    def levenshDist(self, a, b):
        n, m = len(a), len(b)
        if n > m:
            a, b = b, a
            n, m = m, n
        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)
        return current_row[n]

    ## @brief         Делим входное предложение на слова. Убираем знаки препинания. Находим основы для всех слов.
    #
    #        Сте́мминг — это процесс нахождения основы слова для заданного исходного слова.
    #        Основа слова не обязательно совпадает с морфологическим корнем слова.
    #
    #
    # @param		source	Строка для деления на слова и нахождения их основ.
    #
    # @return
    #            Массив основ слов входного предложения.
    #

    def stemmer(self, source):
        stop_symbols = '.,!?:;-\n\r()'
        stm = Stemmer.Stemmer('russian')
        tmp = [x for x in [y.strip(stop_symbols) for y in source.lower().split()]]
        res = []
        for word in tmp:
            res.append(stm.stemWord(word))
        return res

    ## @brief         Делим входной массив слов на шинглы длинной shingleLen.
    #
    # 	Шингл	это фрагмент текста длиной в несколько слов, с которым работает программа проверки уникальности.
    #
    #
    # @param		source	Строка для деления на шинглы.
    #
    # @return
    #            Массив шинглов в crc32.
    #

    def genshingle(self, source):
        import binascii
        shingleLen = 5
        if len(source) < shingleLen:
            shingleLen = len(source)
        out = []
        for i in range(len(source) - (shingleLen - 1)):
            out.append (binascii.crc32(' '.join( [x for x in source[i:i + shingleLen]] ).encode('utf-8')))
        return out

    ## @brief         Вычисляем процентную схожесть двух предложений.
    #
    #        Схожесть двух предложений будет равно 100% если все символы идентичны.
    #
    #
    # @param		source1	Первоя строка для нахождения схожести.
    # @param		source2	Вторая строка для нахождения схожести.
    #
    # @return
    #            Процентная схожесть двух предложений в формате числа с плавующей точкой.
    #

    def compaire (self, source1, source2):
        same = 0
        for i in range(len(source1)):
            if source1[i] in source2:
                same = same + 1

        return same * 2 / float(len(source1) + len(source2)) * 100
