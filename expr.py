class Expression(object):

    def __init__(self, calc_arr=None):
        self.__expression = calc_arr

    def is_integer(self, calc_arr):
        return calc_arr[0].isdigit()


    def get_length(self):
        return len(self.__expression)


    def get_int(self):
        if len(self.__expression) == 1:
            return int(self.__expression[0])


    def get_operator(self):
        if len(self.__expression) > 1 :
            return self.__expression[1]


    def get_exprarr(self):
        return self.__expression

    def get_subexprs(self, calc_arr):
        answer = []
        i = 2
        while i < len(calc_arr)-1:
            l = self.get_sub_len(calc_arr, i)
            answer.append(calc_arr[i:i+l])
            i += l
        return answer


    def get_sub_len(self, calc_arr, i):
        x = i+1
        if calc_arr[i] == '(':
            current = 1
            while current!= 0 and x<len(calc_arr):
                if calc_arr[x] == ')':
                    current -= 1
                if calc_arr[x] == '(':
                    current += 1
                x += 1
        return x-i


    def check_validation(self):
        return self.is_valid(self.__expression)


    def is_valid(self, calc_arr):
        if not calc_arr:
            return False
        if len(calc_arr)==1:
            return self.is_integer(calc_arr)
        return self.check_func(calc_arr)


    def check_func(self, calc_arr):
        funcs = ['add', 'multiply']
        if len(calc_arr) < 4:
            return False
        if calc_arr[-1] != ')' or calc_arr[0] != '(':
            return False
        if calc_arr[1] not in funcs:
            return False

        current = 0
        for char in calc_arr:
            if char == '(':
                current += 1
            if char == ')':
                current -=1
                if current <0:
                    return False
        if current != 0 :
            return False 

        for subexpr in self.get_subexprs(calc_arr):
            if not self.is_valid(subexpr):
                return False
        return True



