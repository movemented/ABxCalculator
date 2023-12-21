# calculator.py

def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    print("Result:", calculate(expression))
