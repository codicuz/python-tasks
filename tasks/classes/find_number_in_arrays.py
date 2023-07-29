class find_number_in_arrays:
    '''Поиск общего числа в трех списках.'''
    
    def __init__(self, arr1: list = [1, 2, 4, 5], arr2: list = [3, 3, 4], arr3: list = [2, 3, 4, 5, 6]):
        '''Конструктор со значениями по умолчанию'''
        self.__arr1 = arr1
        self.__arr2 = arr2
        self.__arr3 = arr3

    @property
    def arr1(self):
        return self.__arr1

    @property
    def arr2(self):
        return self.__arr2

    @property
    def arr3(self):
        return self.__arr3

    def get_list_of_lists(self, *arg):
        '''Функция для возврата переданных функции аргументов в виде списка'''
        lol = list()
        for i in arg:
            lol.append(i)
        
        return lol

    def get_search_digits(self, l: list):
        '''Функция для возвращения множетсва'''
        result = set()

        for i in l:
            for j in i:
                result.add(j)
        
        return result

    def search_digit_list_and_set(self):
        '''Поиск общего числа используя множества'''
        result = list(set(self.arr1) & set(self.arr2) & set(self.arr3))
        
        print(result)

        return result
    
    def search_digit_for_and_if(self):
        '''Поиск общего числа используя цикл и условие. Если искомое значение из первого масива есть в двух других массивах, то добавляем в лист результатов'''
        result = list()
        for i in self.arr1:
            if i in self.arr2 and i in self.arr3:
                result.append(i)
        
        print(result)

        return result

    def serch_digit_list_digit_and_full_search(self):
        '''Поиск общего числа через формирование списка поиска и общего листа листов'''
        
        # Получим лист листов, тем самым определим все масивы, в ктором будем производить поиск
        lol = self.get_list_of_lists(self.arr1, self.arr2, self.arr3)

        # Получим уникальный список искомых значений
        search_digits = self.get_search_digits(lol)

        # Определим вспомогательную функцию, которая будет использоваться в поиске общего числа во всех листах
        def finder(d: int):
            result = list()

            # Перебираем каждый элемент листа листов
            for i in lol:
                # Определитм переменную-флаг. Установим ее в False перед каждым перебором массива
                res = False
                
                # Перебираем каждый элемент листа
                for j in i:
                    # Если переданная в функцию цифра соответствует полученной цифре из конкретного листа, то установим флаг в Истина
                    if j == d:
                        res = True
                
                # Если в листе i была обнаружена переданная в функцию цифра, то запишем в результирующий лист значение переменной res, иначе запишем False
                if res:
                    result.append(res)
                else:
                    result.append(False)
            
            # Вернем результирующий список
            return result
        
        # Объявим словарь для анализа результатов перебора лиса листов
        result_dict = dict()
        
        # Для каждого искомого числа запустим функцию, которая проверит наличие этого числа во всех интересующих нас массивах. Запишем результат в словарь {число: [лист результатов для числа]}
        for i in search_digits:
            result_dict.update({i: finder(i)})
        
        # Объявим лист результатов
        list_result = list()

        # В полученном словаре результатов, проверим листы результатов для искомого числа. Если все значения в листе результатов Истина, запишем в лист результатов
        for k, v in result_dict.items():
            if all(v):
                list_result.append(k)
                print(k, v)
        
        return list_result