def basic_operations(operand1, operand2):

    """
    param1 : operand1 integer or float
    param2 : operand2 integer or float

    For every given arguments it works just fine even if given the wrong arguments it doesn't exit the program handles it greatly!

    If the arguments are OK
        return : dictionary_of_basic_operations
    """

    try:
        addition = operand1 + operand2
        subtraction = operand1 - operand2
        multiplication = operand2 * operand1
        division = operand1 / operand2
        basic = {"addition" : addition , "subtraction" : subtraction, "multiplication" : multiplication, "division" : division}

        return basic
    
    except ZeroDivisionError as e:
        return "Invalid input for operand2: Zero Division"
    
    except TypeError as e:
        return "Invalid Input: Type Error"
    except Exception as e:
        return "Invalid Execution"
    


def power_operation(base, exponent, **kwargs):
    """
    param1 : base integer or float 
    param2 : exponent integer or float
    param3 : optional, anything but with identifier

    if param3 exists:
        return : modules of base the power of exponent of the param3
    return : base the power of exponent



    """
    result = base ** exponent

    for key,val in kwargs.items():
        if key == "modulo":
            result %= val

    return result

def apply_operations(operations):

    """
    the function takes a list of tuples, where each tuple contains a function and its corresponding arguments    
    """
    
    result = map(lambda x : x[0](*x[1]), operations)
    result = list(result)

    return result








