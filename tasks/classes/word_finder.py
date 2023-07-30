class word_finder():
    
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
        # Искомое слово
        search_word = "tinkoff"
        
        # Счетчик совпадений
        match_counter = 0

        # Счетчик искомых букв
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
        # На входе {'t': 2, 'i': 2, 'n': 2, 'k': 2, 'o': 2, 'f': 4}
        # вычитаем слово tinkoff, получаем 
        # {'t': 1, 'i': 1, 'n': 1, 'k': 1, 'o': 1, 'f': 2}
        # все числа >= 0 значит слово tinkoff составлено, и букв на составление 
        # слова tinkoff хватило, увеличиваем счетчик слова
        # вычитаем слово tinkoff еще раз, получаем
        # {'t': 0, 'i': 0, 'n': 0, 'k': 0, 'o': 0, 'f': 0}
        # все числа >= 0 значит слово tinkoff составлено, и букв на составление 
        # слова tinkoff хватило, увеличиваем счетчик слова
        # вычитаем слово tinkoff еще раз, получаем
        # {'t': -1, 'i': -1, 'n': -1, 'k': -1, 'o': -1, 'f': -2}
        # в словаре есть отрицательные значения, это свидетельствует о том, 
        # что букв для составления слова tinkoff не хватило,
        # счетчик слова не увеличиваем
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
        while all(letter_counter.values()):
            if all(letter_counter.values()):
                # Проводим вычитание букв слова tinkoff из словаря букв
                for i in list(search_word):
                    decrese_letter_counter(i)
                # Вызываем вспомогательную функцию, которая проверит словарь букв на значения >= 0
                if check_letter_counter():
                    match_counter += 1
        
        # Завершаем составление строки для передачи в стандартное устройство вывода
        answer += f'{match_counter}.'
        
        # Выводим составленную строку
        print(answer)
        
        # Возвращаем результат работы функции
        return match_counter