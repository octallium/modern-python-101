"""
Variable Scope:
---------------

Scopes can be `Global` or `Local`
"""

num = 10


def print_global_num():
    # Global declaration not required as there is no operation
    # on the variable
    print(f"Global num is: {num}")


def print_num():
    num = 20  # function or local scope
    print(f"Local num is: {num}")


def inc_num():
    # Explicit Global Declaration
    global num
    num += 2
    print(f"Global num is now: {num}")


def inc_local_num():
    new_num = num + 10
    print(f"New num: {new_num}")


print_global_num()
print_num()
inc_num()
inc_local_num()
