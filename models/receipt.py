from ext import round_tax


class Receipt:

    def __init__(self, order_items):
        self.order_items = order_items

        if not self.order_items:
            raise ValueError('Please provide a list with at least 1 item!')

    @staticmethod
    def round_total(amount):
        return round(amount, 2)

    # print receipt in desirable format
    def print_receipt(self):

        # initialize values
        total_tax = 0
        total_amount = 0

        for item in self.order_items:
            print("{quantity} {name} : {price}".format(
                quantity=item.quantity,
                name=item.product.name,
                price="{:0.2f}".format(item.product.price * item.quantity + float(
                    round_tax(item.product.calculate_tax() * item.quantity)))
            )
            )

            total_tax += item.total_tax
            total_amount += item.total_amount

        print("Sales Taxes: ", round_tax(total_tax))
        print("Total: ", self.round_total(total_amount))
