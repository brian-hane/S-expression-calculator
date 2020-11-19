import sys
from parse import *
from expr import *
from calculator import *

def main():
    if len(sys.argv)<2:
        print('-------------------No input was entered-------------------')
        return

    calc_arr = ParseString(sys.argv[1]).str_to_arr()
    expression = Expression(calc_arr)

    if not expression.check_validation():
        print('---------------------Invalid Input------------------------')
        return
#instantiate calculator object since expression is valid
    calculator = Calculator()
#print out result
    print(calculator.calculate(expression))



if __name__ == '__main__':
    main()
