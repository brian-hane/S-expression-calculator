# S-expression-calculator
==============================
# Language:
Python 3.7.3


### driver.py
Main file to run all the classes together. 
It can be started in command line, with one valid argument as input

### parse.py
ParseInput is an object to read and parse the string inputted by string manipulation.

 **parse_to_list()** method to parse the input string into an array
['(', 'multiply', '(', 'add', '1', '2', ')', '3', ')']




### calculator.py
Calculator is an Object that can parse the Expression instance and provides the calculated expression

**calculate()** method to calculate, input of this method is an Expression instance, output is a number(integer).
**addition()** method and **multiply()** method to compute addition and multiplication



### expr.py
Expression is an Object that stores the expression list and does basic manipulation on it.

**check_validation()** method checks whether an expression is a valid S-expression. It uses the is_valid(), is_integer(), and check_func(array).

**get_subexprs()** method gets sub expressions for a function expression, and returns a list of expressions(mathematical terms). This method uses the recursive process in both checking expression validation and calculation.
