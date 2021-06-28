import math
import pickle

def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)

def tan(x):
    return math.tan(x)

def log(x):
    return math.log(x)

running = True



def load_ops():
    try:
        loaded = pickle.load(open("ops.p","rb"))
        return loaded
    except Exception:
        return []

def save_ops():
    pickle.dump(prev_ops,open("ops.p","wb"))


prev_ops = load_ops()

print("Welcome to my Python Calculator")

symbols = "List of basic operation symbols recognized in the user's input:" + "\n" + "Addition: +" + "\n" + "Subtraction: -" + "\n" + "Division: /" + "\n" + "Multiplication: *" + "\n" + "Exponent: ^"
functions = "This calculator supports cos,sin,tan and log functions, using the function names listed previously, ex cos(2) in the input"
print(symbols)
print(functions)

while running:

    print("Previously calculated operations: ")
    for op in prev_ops:
        print(op)

    operation = input("Operation | type done to leave the program: ")

    if operation == "done":
        running = False


    try:
        cleaned_operation = operation.replace("^","**")

        ans = eval(cleaned_operation)
        operation+=" = " + str(ans)

        prev_ops.append(operation)


        print("The answer is: " + str(ans))

        save_ops()

    except Exception:
        continue

