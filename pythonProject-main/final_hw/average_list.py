"""Класс для сравнения средних значений двух списков"""


class AverageList:
    @staticmethod
    def findaverage(ls: list):
        if isinstance(ls, list):
            if len(ls) != 0:
                res = 0
                for i in ls:
                    res += i
                return res / len(ls)
            else:
                return None
        else:
            raise TypeError("Input should be a list")

    @staticmethod
    def list_comparison(ls1: list, ls2: list):
        average_1 = AverageList.findaverage(ls1)
        average_2 = AverageList.findaverage(ls2)
        if average_1 and average_2:
            if average_1 > average_2:
                return "Первый список имеет большее среднее значение"
            elif average_1 < average_2:
                return "Второй список имеет большее среднее значение"
            else:
                return "Средние значения равны"
        else:
            return None


