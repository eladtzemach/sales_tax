# Sales Tax

The program was built using:
Language: Python 3.4
IDE: PyCharm
OS: Windows 8

## Design:

The program includes the following entities:

### Receipt
- **OrderItem(s)**

### OrderItem
- **Product**
- Quantity
- Total Price
- Total Tax
- Total Amount (Price + Tax)

### Product
- Name
- **ProductCategory**
- **ProductOrigin**
- Price

### ProductOrigin
- Name (local/imported)
- **TaxRate**

### ProductCategory
- Name (books/food/medical/other)
- **TaxRate**

### TaxRate
- Name (exempt/sales_tax/import_duty)
- Rate (0.0/0.10/0.05)


## Assumptions and Design Choices:

1. Although it was not explicitly mentioned in the requirements, the `OrderItem` entity was added to allow
for more than 1 product of the same type and price (hence the variable `Quantity`).

2. I have used constant variables (all upper case) in the relevant entities in the case of future scaling of the program
(avoiding DRY).

3. When calculating tax, the `calculate_tax()` functions of the `Product` class calls the `calculate_tax()` functions of both
`ProductOrigin` and `ProductCategory` classes since we can have tax of only one of them or both, depends on the product's
category and origin (local vs. imported).
This type of logic helps if in the future we decide to make non-taxable items taxable or vice versa.

4. Since we only know of tax exceptions for the following categories: Books, Food and Medical - all of the products that
do not fall under those categories are classified as Other. However, it is very simple to create new categories. 

5. I have decided to hardcode the input into the program. For example:
`1 book at 12.49` was translated to `Product("book", books, local, 12.49)`.
I could have done string (input) parsing but i assumed that would be an "overkill". 

6. The `ext.py` (external functions) file includes functions that do not belong to any single class but rather being used by more
than just one class.

## Testing:

Aside from manual testing, i have included 22 unit tests for the different classes.
For running the tests, run `python run_tests.py` from the command prompt / terminal.
Excpected output:
```
......................
----------------------------------------------------------------------
Ran 22 tests in 0.006s

OK
```

## Running the Program:

The file `main.py` takes care of initializing all of the tax rates, product categories and origins and orders.
It then prints the receipt as requested.

Running `python main.py` from the command prompt / terminal should display the following output:

```
OUTPUT 1
1 book : 12.49
1 music CD : 16.49
1 chocolate bar : 0.85
Sales Taxes:  1.50
Total:  29.83


OUTPUT 2
1 imported box of chocolates : 10.50
1 imported bottle of perfume : 54.65
Sales Taxes:  7.65
Total:  65.15


OUTPUT 3
1 imported bottle of perfume : 32.19
1 bottle of perfume : 20.89
1 packet of headache pills : 9.75
1 imported box of chocolates : 11.85
Sales Taxes:  6.70
Total:  74.68
```
