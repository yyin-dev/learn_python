# Error: syntax error; Exception: syntactically correct, fail to execute.
# finally clause
# The finally clause is always executed before leaving the 
# try/except/else/finally block. When an exception is thrown but not handled( 
# exception is thrown but there's no except clause, or exception is thrown in an
# except or else clause), that exception is re-raised after the finally clause
# is executed. The finally block is also executed when any other clause of the 
# try statement is left via a break, continue or return.
def divide(x, y):
    try:
        print("Try dividing!")
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    else: 
        print("Result is " + str(result))
    finally:
        print("Executing finally clause!")
    
# The finally clause is executed in any event.
# - No exception: try -> else -> finally
# - Exception catched: try -> except -> finally
# - Exception not catched: try -> finally -> reraise exception
# The finally clause is useful for release resources.
divide(2, 1)
print("-"*20)
divide(2, 0)
print("-"*20)
divide("2", "1")