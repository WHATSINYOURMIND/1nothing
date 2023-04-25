def division(x, y):
    try:
        div = x / y
        print(f"{x}/{y} = {div}")
    except ZeroDivisionError as e:
        print("Exception occurred!:", e)
    except ValueError as e:
        print("Exception occurred!:", e)
    except Exception as e:
        print("Exception occurred!:", e)
    finally:
        print("Working on division function") #clan-up action
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

division(a, b)
