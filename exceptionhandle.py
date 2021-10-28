# exception examples

try:
    numerator = int(input("Enter a number to divide:  "))
    denomiator = int(input("Enter a number to divide by:  "))

    answer = numerator / denomiator

    print(answer)
except ZeroDivisionError:
    print("stop trying to divide by zero")
except ValueError:
    print("you need to use numbers")
#except Exception:
#    print("nope")