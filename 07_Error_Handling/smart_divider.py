def smart_divider(x: int, y: int) -> None:
    try:
        num = x / y
        print(num)
    except ZeroDivisionError:
        print("Can't divide by zero! Use some other number")


smart_divider(4, 0)
