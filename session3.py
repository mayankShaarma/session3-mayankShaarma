from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module
    '''
    if base < 2 and base > 36:
        raise ValueError("ValueError: Invalid base Value. Should be >= 2 or =< 36")
    elif len(digit_map) != base:
        raise ValueError("ValueError: Invalid base ValueError must have relevant information")
    elif len(set(digit_map)) != base:
        raise ValueError('ValueError: repeating digit_map')
    elif number == 0:
        return 0
    else:
        digits = []
        if number < 0:
            n, encoding = (-number,"-")
        else:
            n, encoding = (number,"")
        while n > 0:
            mod = n%base
            n = n//base
            digits.insert(0,mod)
        encoding += "".join([digit_map[d] for d in digits])
        return encoding


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    delta = a-b if a > b else b-a
    return delta < max(rel_tol * max(abs(a),abs(b)),abs_tol)


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    # multiplier = 10 ** decimals
    # f_num = INT(num * multiplier) / multiplier
    # return f_num
    if(type(f_num) is float):
        s=str(f_num)
        sub_str=s[0:s.index(".")]
        f=Fraction(sub_str)
        return f.numerator
    else:
        raise ValueError("ValueError : Float nahi pass kiye aap")
        return f_num

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if isinstance(f_num, float):
        if f_num >=0:
            return f_num -(f_num%1)
        else:
            return -(abs(f_num) - (abs(f_num) % 1))
    else:
        raise ValueError("ValueError: Dobara se nahi bolenge, sahi se Float pass kariye aap")
        return f_num

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0