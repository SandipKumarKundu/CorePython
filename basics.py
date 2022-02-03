def calc(ops,arg1,arg2):

    if(ops=="Add"):
        print(arg1+arg2)
    elif (ops == "Sub"):
        print(arg1 - arg2)
    elif (ops == "Mul"):
        print(arg1 * arg2)
    else :
        print("operation not mentioned")

calc("Mul",2,3)