
def fib(n):
    '''
        Implementation of the Nth Fibonacci number using recursion
        By definition:
            F(0) = 0
            F(1) = 1

            and Fib(N) = Fib(N-1) + Fib(N-2)
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)






if __name__ == '__main__':
    '''
        Asks user to insert the parameter N to calculate Fib(N). 
            + Checks if N is a number
                - If it is not a number, then raise an ValueError Exception
                - If it is a number 
                    * Checks if the number is positive
                    * Else asks for a positive integer 
                    
        Warning:    The given implementation is not optimal. 
                    The complexity of the algorithm is exponential O(φ^n). 
                    Therefore do not insert large input (e.g. >20) 
                    Except you have plenty of time...
    
    '''

    try:
        number = int(input("This script calculates the Fib(N) number. \n"
                        "Insert N here: "))
        if number < 0:
            print("Please insert a positive integer...")
        else:
            print("Result: %d" % fib(number))
    except ValueError:
        print("Please insert a positive integer...")




