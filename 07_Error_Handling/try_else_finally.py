def divider(x: int, y: int) -> None:
    try:
        num = x / y
    except ZeroDivisionError:
        print("Can't divide by zero! Use some other number")
    except TypeError:
        print("Both x & y needs to be numbers.")
    except Exception as e:
        print(f"Oops, something went wrong: {e}")
    else:
        print("Else: Is executed only when try succeeds")
        print("Printing num....")
        print(num)
    finally:
        print("Finally: Always executes irrespective of success or exception.")


divider(3, 0)
divider(3, 4)
