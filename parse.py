class ParseString(object):

    def __init__(self, input_exp=''):
        self.input_exp = input_exp

    def str_to_arr(self):
        resultStr = ""
        if self.input_exp == '':
            print('------------------------Invalid Input------------------------')
            return None

        
        for str in self.input_exp:
            if str == '(':
                resultStr += str + ' '
            elif str == ')':
                resultStr += ' ' + str
            else:
                resultStr += str

        return resultStr.split()
