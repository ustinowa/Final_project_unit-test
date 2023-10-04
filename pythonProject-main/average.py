class Average:
    def finedaverage(ls: list):
        if not isinstance(ls, list):
            if len(ls) != 0:
                res = 0
                for i in ls:
                    res += i
                return res / len(ls)
            else:
                return None
        else:
            raise TypeError("Input should be a list")




# print(Average.finedaverage([1, 5, 7]))