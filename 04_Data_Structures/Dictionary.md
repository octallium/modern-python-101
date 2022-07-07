# Dictionary

They are also known as mapping type, they map keys to the values.

## What data types you can use for keys in Python dictionary?

Any data type which is immutable can be used as a key. To understand this behavior we would
need to understand how dictionary works behind the scene, which is too
advanced for this course.

For now just remember that immutable data types such as **string, int, float, boolean, tuples,** etc, can be used
as keys.

```python
pizza = {
        10: "small",
        8.99: "price",
        ("cheese", "olives"): "toppings",
        True: "available",
    }

print(pizza[10]) # prints => "small"
print(pizza[8.99]) # prints => "price"
print(pizza[("cheese", "olives")]) # prints => "toppings"
print(pizza[True]) # prints => "available"
```

`pizza` is also a perfectly valid dictionary, but does not have practical usability.
