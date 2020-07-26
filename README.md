## Define README.md with description of keyworkds and method used 
### Session 3 - Numeric Types
- Integers, Constructors, Bases, Rational Numbers, Floats, rounding, Coercing to Integers and equality

>  *** In python we have 5 main type of numbers ***

1. Boolean: Represented by bool class True , False which is a subset of the integer class as True = 1 and False = 0
2. Integer number: Represented by int class
3. Rational number: Rational number are number which can be represented in fractions. All the number within a programming language are Rational numbers
4. Real number: the float and decimal class represent these
5. Complex numbers: python have a class for representing complex numbers too. ex = 2

### Keywords:
#### 1. 'int': 
> we dont have to use built-in function to convert string or float to string. so i used Fraction for this.

#### 2. 'digit_map':
- test_innacurate_digit_map_length() : checking encoded_from_base10() with digit_map length as test case.
- test_repeating_digits_in_digit_map() : checking encoded_from_base10 with repeating character in encoded return from digit_map

#### 3. 'ValueError':
- If Conditions not match we explictly raising ValueError from code with proper readable statement.
    
#### 4. 'relative' and 'tolerance':
- In python used to rounding to make precision and tolerance with large values which relative to dynamic and  

#### 5. 'test conversions':
'bin('
'hex('
- Python as inbuit function to conversions of hexa, decimal, octa, bin. all are very handy to change values.

#### 6. 'math' : Its Library of Python which provide, many utility functions.
#### 7. 'isclose': this is function which equates values closer. 

#### 8. 'absolute': abs() in-buit libraryr function, which return absolute value. 

#### 9. 'round': round() inbuilt library function, which round of decimal values as integer.
 
### Details Description of function written in Code file:

#### 1. 'encoded_from_base10':
we need to write function which return encoded from number pass,
This function returns a string encoding in the "base" for the the "number" using the "digit_map"
#### 1. Conditions that this function must satisfy:
- 2 <= base <= 36 else raise ValueError
- invalid base ValueError must have relevant information
- digit_map must have sufficient length to represent the base
- must return proper encoding for all base ranges between 2 to 36 (including)
- must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
- the digit_map must not have any repeated character, else ValueError
- the repeating character ValueError message must be relevant
- you cannot use any in-built functions in the MATH module

#### 2. float_equality_testing: 
test_float_equality_testing()
This function emulates the isclose method from the math module, but you can't use this function
- 'math': 
- 'isclose' :

#### 3. manual_truncation_function: 
test_manual_truncation_function() : This functon returning truncation of value with manual checking without help of built-in function.
'''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
'''
'truncation',

#### 4. 'manual_rounding_function' :
test_manual_rounding_function() - rounding of value to Integer and clip of decimal values.
'''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
'''

#### 5. 'test_fraction_used_or_not' :
- checking Fraction used or not in logic. 
- Rational number can be represent as Fraction class or module in python.
- we can get rational number to Divide into numerator and denomiator.

#### 6. 'rounding_away_from_zero':
    'error',
    'equality',
    'zero',
    'away'
- writing this function to pass the test of readme to include words like error and away.
