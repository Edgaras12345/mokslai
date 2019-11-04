# def function-name(Parameter list):
#     statements, i.e. the function body

# 1. simple function
print("==== 1. simple function ====")
def add(x, y):
    """ take two params, add them. print result"""
    result = x + y
    print(result)

add(2, 3)


# 2. simple function with a return
print("==== 2. simple function with a return ====")
def add_with_return(x, y):
    result = x + y
    return result

add_with_return(2, 3)

# 3. reusing functions
print("==== 3. reusing functions ====")
print(add_with_return(2, 3))
print(add_with_return(2, 3) + add_with_return(10, 3))
