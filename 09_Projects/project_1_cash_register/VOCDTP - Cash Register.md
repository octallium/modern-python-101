# Visualize - Outline - Code | Debug - Test - Polish

Let's try to apply VOC-DTP principle and see how we can break this problem into small components and work through it.

## Problem Statement - Make a Simple Cash Register

We want to create a simple cash register, now let's try to imagine what our register would require. Remember whenever you shop, what happens at the checkout counter, you hand over the items to the cashier, the cashier scans the items, generates an invoice, accepts payments and hands over the product.

Now, since we are only interested in Cash Register, let's further try to refine and see what happens when the cashier scans the item -

## Phase 1 -> Visualize - Outline - Code

### Step 1 - Visualize

1. Item is added to the invoice
2. If the customer wants to change the quantity, cashier simply updates the item.
3. If customer changes mind and won't to drop an item, cashier deletes the item from invoice.
4. Item may have other components such as discount or offers.
5. Additional tax may be added to the invoice.

To help you visualize, after implementing our code this is how our `Cash Register` would finally look like -

```python
{
    "customer": {
        "first_name": "Chiko",
        "last_name": "Neutron"
    },
    "invoice_total": 86.88,
    "items": {
        "Apple": {
            "discount": 2,
            "name": "Apple",
            "quantity": 8,
            "sub_total": 43.36
        },
        "Egg": {
            "discount": 12,
            "name": "Egg",
            "quantity": 48,
            "sub_total": 35.52
        },
        "Milk": {
            "discount": 10,
            "name": "Milk",
            "quantity": 4,
            "sub_total": 8.0
        }
    },
    "purchase_date": "June 01, 2022"
}
```

I could visualize this final outcome after implementing `Step 2`, but I am mentioning it here just as a visual aid and to help you imagine.

For a beginner it would be little difficult to imagine how your final outcome would look like, but with practice it would get easier.


### Step 2 - Outline

Now we have a brief idea about the expectations of the cash register, let's try to outline various objects needed to create a cash register.

1. Customer - We require a customer, one who is going to make a purchase.
2. Item - The product that the customer is purchasing.
3. Invoice Entry - Just imagine you bill, whenever you purchase different items may have different discounts or offer. Individual products may also have different taxation. In order to represent this we are going to need a separate object, let's call it `Invoice Item` and only include discount for the sake of simplicity.
4. Cash Register - The place where we record all these purchase transactions, while we are not going to generate an actual invoice, but you get the idea right! To keep things simple we are directly going to create register, in future you may include a invoice objects and expand the code.

Let's try to summarize all the objects we are going to need -

| Sr No | Object/Class |
| ----- | ------------ |
| 1     | Customer     |
| 2     | Item         |
| 3     | InvoiceItem  |
| 4     | CashRegister |

Now since we know which objects we require, we can start coding, let's first refine the previous step and then we can actually implement the code

1. Customer

| Sr No | Instance Variables | Type   | Methods | Description |
| ----- | ------------------ | ------ | ------- | ----------- |
| 1     | First Name         | String | ----    | ------      |
| 2     | Last Name          | String | ----    | ------      |

2. Item

| Sr No | Instance Variables | Type   | Methods | Description                                       |
| ----- | ------------------ | ------ | ------- | ------------------------------------------------- |
| 1     | ID                 | Int    | ----    | Every product needs a unique ID                   |
| 2     | Name               | String | ----    | Every product needs a name                        |
| 3     | Price              | Float  | ----    | Price of the product                              |
| 4     | Measurement Unit   | String | ----    | How do you measure? It can be kg, gms, litre, etc |

3. Invoice Item

| Sr No | Instance Variables | Type  | Methods         | Description                                                      |
| ----- | ------------------ | ----- | --------------- | ---------------------------------------------------------------- |
| 1     | Item               | Item  | ----            | The item that is bring purchased                                 |
| 2     | Discount           | Float | ----            | How much discount is being offered                               |
| 3     | Quantity           | Int   | ----            | Purchase quantity                                                |
| 4     |                    | ----- | get_sub_total() | Returns the sub total of the item after subtracting the discount |

4. Cash Register

| Sr No | Instance Variables | Type       | Methods             | Description                          |
| ----- | ------------------ | ---------- | ------------------- | ------------------------------------ |
| 1     | Customer           | Customer   | ----                | Which customer is doing the purchase |
| 2     | Items              | Dictionary |                     | List of items purchased              |
| 3     | Purchase Date      | DateTime   |                     | ---                                  |
| 4     |                    | ------     | add_item()          | Add's an Item to register            |
| 4     |                    | ------     | update_item()       | Update item details                  |
| 4     |                    | ------     | remove_item()       | Remove item from register            |
| 4     |                    | ------     | get_invoice_total() | Calculates the invoice total         |
| 4     |                    | ------     | display_invoice()   | Displays the invoice                 |

What we have created here is technically known as `Unified Modelling Language Diagram`, to describe it is out of scope for this tutorial. Obviously UML Diagram is in a form of a diagram, I am just simplifying it and representing it here in a table format for your understanding. 

If you are interested then be sure to search and read more about [Unified Modelling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)

In fact `FreeCodeCamp` has a [Full Course](https://www.youtube.com/watch?v=WnMQ8HlmeXc) on UML.

### Step 3 - Code

First two steps are the most time consuming and tedious steps, now comes the easy part! It's time to spin up your code editor and translate our outline to python code.

As mentioned earlier, this is how our final outcome would look like - 

```python
{
    "customer": {
        "first_name": "Chiko",
        "last_name": "Neutron"
    },
    "invoice_total": 86.88,
    "items": {
        "Apple": {
            "discount": 2,
            "name": "Apple",
            "quantity": 8,
            "sub_total": 43.36
        },
        "Egg": {
            "discount": 12,
            "name": "Egg",
            "quantity": 48,
            "sub_total": 35.52
        },
        "Milk": {
            "discount": 10,
            "name": "Milk",
            "quantity": 4,
            "sub_total": 8.0
        }
    },
    "purchase_date": "June 01, 2022"
}
```

What we have created is essentially called as a `Data Structure` which represents a `Cash Register`. Data Structure is a big word, but it doesn't have to be complicated, it's just a way how we want to structure our data!

## Phase 2 -> Debug - Test - Polish

### Debug

Debugging is essentially an art, it's the process of finding out areas in your code which does not work as expected. Most of the time using a simple `print` statement does the trick, I most commonly use it before using any other tools such as `Python Debugger`

What we want to do is, as soon as we code a module/class/object, we want to run it and see if it is working as expected. If not then try and debug the issue and when everything is resolved, then we move to coding the next module.

Use of tools such as `Python Debugger` is out of the scope of this tutorial, if you want to learn more about it, message or tweet me on [@octallium](https://twitter.com/octallium)

### Test

Testing is undoubtedly one of the most important phase, no project can be called complete without proper testing. Testing is essentially trying our code will all possible scenarios and input parameters. Testing is a huge subject and required dedicated series which is out of the scope of this tutorial.

Testing frameworks such as `Unit Testing` or `Pytest` are used for comprehensive testing. Some developers believe in writing test first and then writing the functionality, this is called as `Test Driven Development`

### Polish

Now that your code is complete, tested and working as expected, you can now work on polishing your code. Polishing could mean optimizing for speed, space, resiliency, failure handling, security, etc. Or you could also polish by adding documentation to your project.

We don't want to break our functionality in this phase, just improve on the existing code. Make sure to run your tests after polishing!
