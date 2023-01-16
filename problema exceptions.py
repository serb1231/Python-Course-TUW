class NegativeException(Exception):
    pass

def simple_function(x):
    if x>0:
        return x
    else:
        raise NegativeException

def cascade_function(x):
    try:
        simple_function(x)
    except NegativeException:
        raise ValueError

assert simple_function(2) == 2

raised = False
try:
    simple_function(-2)
except NegativeException:
    raised = True

def finally_function(x):
    try:
        cascade_function(x)
    except ValueError:
        return True

assert raised

negative_raised = False
value_raised = False
try:
    cascade_function(-2)
except NegativeException:
    negative_raised = True
except ValueError:
    value_raised = True

assert not negative_raised
assert value_raised

assert finally_function(-5)