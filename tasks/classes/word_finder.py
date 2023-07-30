class word_finder():
    '''Класс work_finder. Поиск возможного количества составления слова tinkoff из букв, переданной в строке'''
    
    def __init__(self, search_string: str):
        '''Конструктор'''
        self.__search_string = search_string
    
    @property
    def search_string(self):
        '''Свойство для хранения строки в которой производим поиск'''
        return self.__search_string

    @search_string.setter
    def search_string(self, data):
        '''Сеттер для установки строки в которой производим поиск'''
        self.__search_string = data

    def countWord(self):
        '''Функция поиск возможного количества составления слова tinkoff'''
        
        # Искомое слово
        search_word = "tinkoff"
        
        # Счетчик совпадений
        match_counter = 0

        # Счетчик искомых букв, инициализируем начальным значением 0, каждый счетчик
        letter_counter = {letter.lower(): 0 for letter in search_word}

        # Вспомогательная функция, увеличивающая счетчик искомых букв
        def increse_letter_counter(letter: str):
            for i in letter_counter.keys():
                if letter == i:
                    letter_counter[i] += 1
        
        # Вспомогательная функция, уменьшающая счетчик искомых букв
        def decrese_letter_counter(letter: str):
            for i in letter_counter.keys():
                if letter == i:
                    letter_counter[i] -= 1
        
        # Вспомогательная функция для проверки результата уменьшения счетчика искомых букв, 
        # после вычисления которого принимаем решение увеличивать счетчик количества слов или нет.
        # Изначальный счетчик искомых букв {'t': 2, 'i': 2, 'n': 2, 'k': 2, 'o': 2, 'f': 4}
        # вычитаем слово tinkoff, получаем 
        # {'t': 1, 'i': 1, 'n': 1, 'k': 1, 'o': 1, 'f': 2}
        # все числа >= 0 значит слово tinkoff составлено, и букв на составление 
        # слова tinkoff хватило, возвращаем True.
        # Вычитаем слово tinkoff еще раз, получаем
        # {'t': 0, 'i': 0, 'n': 0, 'k': 0, 'o': 0, 'f': 0}
        # все числа >= 0 значит слово tinkoff составлено, и букв на составление
        # слова tinkoff хватило, возвращаем True.
        # Вычитаем слово tinkoff еще раз, получаем
        # {'t': -1, 'i': -1, 'n': -1, 'k': -1, 'o': -1, 'f': -2}
        # в словаре есть отрицательные значения, это свидетельствует о том, 
        # что букв для составления слова tinkoff не хватило, возвращаем False
        def check_letter_counter():
            # В цикле бежим по значениям счетчика букв, как только встречаем 
            # отрицательное значение, выходим и возвращаем False
            for i in letter_counter.values():
                if i < 0:
                    return False
            
            return True
        
        # Бежим по строке, преобразуем полученные буквы к нижнему регистру, 
        # и передаем полученную и преобразованную букву к нижнему регистру 
        # во вспомогательную функцию, для увеличения счетчика интересующих нас букв
        for char in self.search_string:
            char_in_lower_case = char.lower()
            increse_letter_counter(char_in_lower_case)

        # Начинаем составлять строку для передачи в стандартное устройство вывода
        answer = f'Количество совпадений слова Tinkoff из количественного набора букв {letter_counter}: '
        
        # Считаем количество возможных составлений слова Tinkoff. Считаем, 
        # что слово Tinkoff возможно составить столько раз, 
        # пока счетчик интересующих нас букв >= 0. Как только счетчик 
        # хотя бы одной буквы становится отрицательным числом, 
        # считаем, что слово Tinkoff составить невозможно.
        # Как минимум на начальном этапе, условием для входа в цикл, является то,
        # что все значения счетчиков искомых букв должны быть больше нуля, т.к.
        # если хотя бы одной интересующей нас буквы не будет в счетчике интересующих
        # нас букв, то и входить в цикл никакого смысла нет.
        while all(letter_counter.values()):
            # После входа в цикл, необходимо проверить, хватает ли букв, для составления слова tinkoff,
            # Проводим вычитание букв слова tinkoff из счетчика искомых букв
            for i in list(search_word):
                decrese_letter_counter(i)
            # Вызываем вспомогательную функцию, которая проверит словарь букв на значения >= 0, если все
            # счетчики букв будут >= 0, то вспомогательная функция вернет true, что в свою очередь будет
            # являтся сигналом того, что в текущем наборе букв, хватило букв для составления слова tinkoff.
            # В противном случае ничего не делаем, и переходим к следующей итерации цикла. Как только
            # условие цикла перестанет выполняться, цикл закончит свою работу, и выполнение кода пойдет дальше.
            if check_letter_counter():
                match_counter += 1
        
        # Завершаем составление строки для передачи в стандартное устройство вывода
        answer += f'{match_counter}.'
        
        # Выводим составленную строку
        print(answer)
        
        # Возвращаем результат работы функции
        return match_counter