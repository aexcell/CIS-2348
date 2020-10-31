# Alexandra Excell  PSID: 1595971


# First Part

class ItemToPurchase:
	def __init__(self, item_name='none', item_price=0, item_quantity=0):
		self.item_name = item_name
		self.item_price = item_price
		self.item_quantity = item_quantity

	def print_item_cost(self):
		item_cost = (self.item_quantity * self.item_price)
		print(self.item_name, self.item_quantity, '@ ${}'.format(self.item_price), '=', '${}'.format(item_cost))
		return (item_cost)


# Second Part

if __name__ == "__main__":
	print('Item 1')
	input1_name = input("Enter the item name:\n")
	input1_price = int(input("Enter the item price:\n"))
	input1_quant = int(input("Enter the item quantity:\n"))

	print('\nItem 2')
	input2_name = input("Enter the item name:\n")
	input2_price = int(input("Enter the item price:\n"))
	input2_quant = int(input("Enter the item quantity:\n"))

	print('\nTOTAL COST')
	item1 = ItemToPurchase(input1_name, input1_price, input1_quant)
	cost1 = item1.print_item_cost()
	item2 = ItemToPurchase(input2_name, input2_price, input2_quant)
	cost2 = item2.print_item_cost()
	print('')
	print('Total: ${}'.format(str(cost1 + cost2)))






