from expr import *

class Calculator(object):

    def __init__(self):
        pass

    def calculate(self, expression):
        return self.calc_expression(expression)

    #determines the operation required by obtaining the operator within the expression object
    def calc_expression(self, expression):
        if not expression:
            print('------------------------Invalid Expression------------------------')
            return

        if expression.get_length() == 1:
            return expression.get_int()
		#get the operator from string and determine the calculation
        operator = expression.get_operator()
        if operator == 'add':
            return self.addition(expression)

        elif operator == 'multiply':
            return self.multiply(expression)


	#calculates addition based on the expression's list of numbers
    def addition(self, expression):
        digit = 0
        for each in expression.get_subexprs(expression.get_exprarr()):
            digit += self.calc_expression(Expression(each))
        return digit

    #calculates multiplication based on the expression's list of numbers
    def multiply(self, expression):
        digit = 1
        for each in expression.get_subexprs(expression.get_exprarr()):
            digit *= self.calc_expression(Expression(each))
        return digit
