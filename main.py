from models.order_item import OrderItem
from models.product import Product
from models.product_category import ProductCategory
from models.product_origin import ProductOrigin
from models.receipt import Receipt

from models.tax_rate import TaxRate

# create tax types
# TaxRate(name, rate)
tax_exempt = TaxRate("TAX_EXEMPT", TaxRate.TAX_EXEMPT)
sales_tax = TaxRate("SALEX_TAX", TaxRate.SALES_TAX)
import_duty = TaxRate("IMPORT_DUTY", TaxRate.IMPORT_DUTY)

# create item categories
# ProductCategory(name, TaxRate)
books = ProductCategory(ProductCategory.BOOKS, tax_exempt)
food = ProductCategory(ProductCategory.FOOD, tax_exempt)
medical = ProductCategory(ProductCategory.MEDICAL, tax_exempt)
other = ProductCategory(ProductCategory.OTHER, sales_tax)

# create the additional local/imported tax types
# ProductOrigin(name, TaxRate)
local = ProductOrigin(ProductOrigin.LOCAL, tax_exempt)
imported = ProductOrigin(ProductOrigin.IMPORTED, import_duty)

# INPUT 1 - Products
# Product(name, ProductCategory, ProductOrigin, price)
i1_product1 = Product("book", books, local, 12.49)
i1_product2 = Product("music CD", other, local, 14.99)
i1_product3 = Product("chocolate bar", food, local, 0.85)

# INPUT 1 - Quantity
# OrderItem(Product, quantity)
i1_order_item1 = OrderItem(i1_product1, 1)
i1_order_item2 = OrderItem(i1_product2, 1)
i1_order_item3 = OrderItem(i1_product3, 1)

print("OUTPUT 1")
output1_receipt = Receipt([i1_order_item1, i1_order_item2, i1_order_item3])
output1_receipt.print_receipt()
print("\n")

# INPUT 2 - Products
i2_product1 = Product("imported box of chocolates", food, imported, 10.00)
i2_product2 = Product("imported bottle of perfume", other, imported, 47.50)

# INPUT 2 - Quantity
i2_order_item1 = OrderItem(i2_product1, 1)
i2_order_item2 = OrderItem(i2_product2, 1)

print("OUTPUT 2")
output2_receipt = Receipt([i2_order_item1, i2_order_item2])
output2_receipt.print_receipt()
print("\n")

# INPUT 3 - Products
i3_product1 = Product("imported bottle of perfume", other, imported, 27.99)
i3_product2 = Product("bottle of perfume", other, local, 18.99)
i3_product3 = Product("packet of headache pills", medical, local, 9.75)
i3_product4 = Product("imported box of chocolates", food, imported, 11.25)

# INPUT 3 - Quantity
i3_order_item1 = OrderItem(i3_product1, 1)
i3_order_item2 = OrderItem(i3_product2, 1)
i3_order_item3 = OrderItem(i3_product3, 1)
i3_order_item4 = OrderItem(i3_product4, 1)

print("OUTPUT 3")
output3_receipt = Receipt([i3_order_item1, i3_order_item2, i3_order_item3, i3_order_item4])
output3_receipt.print_receipt()
print("\n")
