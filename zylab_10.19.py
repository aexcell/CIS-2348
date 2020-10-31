# Alexandra Excell  PSID: 1595971
# First Part

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        item_cost =(self.item_quantity * self.item_price)
        print(self.item_name, self.item_quantity, '@ ${}'.format(self.item_price), '=', '${}'.format(item_cost))
        return(item_cost)

    def print_item_description(self, ItemToPurchase):
        print(self.item_name, ':', self.item_description)


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
        print('')
        print('Customer name: {}'.format(self.customer_name))
        print("Today's date: {}\n".format(self.current_date))

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, ItemToRemove):
        if ItemToRemove in self.cart_items:
            self.cart_items.remove(ItemToRemove)
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase, new_quantity):
        if ItemToPurchase in self.cart_items:
            ItemToPurchase.quantity = new_quantity
        else:
            print('Item not found in cart. Nothing removed.')

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(len(self.cart_items,0))

    def print_descriptions(self):
        for item in self.cart_items:
            print(item.item_description)

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return(total_cost)

    def output_items(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
        print('Item Descriptions')
        for item in self.cart_items:
            print('{} @ ${} = ${}'.format(item.item_name, item.item_price,
                                          (item.item_price*item.item_quantity)))

    def output_shoppingCart(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
        print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
        if self.get_num_items_in_cart() == 0:
            print('SHOPPING CART IS EMPTY')
        print('\nTotal: ${}\n'.format(self.get_cost_of_cart()))


###################################
def print_menu(ShoppingCart):
    menu = {'a': 'Add item to cart', 'r':'Remove item from cart',
            'c': 'Change item quantity', 'i': "Output items' descriptions",
            'o': 'Output shopping cart', 'q': 'Quit'}
    print('MENU')
    for option in menu:
        print('{} - {}'.format(option, menu[option]))
    print('')
    user_input = ''
    while user_input != 'q':
        user_input = input('Choose an option:\n')
        # if user_input == 'q':
        #     break
        if user_input == 'a':
            print('\nADD ITEM TO CART')
            itemToPurchase = input('Enter the item name\n')
            item_description = input('Enter the item description:\n')
            item_price = input('Enter the item price:\n')
            item_quantity = input('Enter the item quantity:\n')
            ShoppingCart.add_item(itemToPurchase,item_description,
                                  item_price,item_quantity)
        elif user_input == 'r':
            print('\nREMOVE ITEM FROM CART')
            itemToRemove = input('Enter name of item to remove:\n')
            ShoppingCart.remove_item(itemToRemove)
        elif user_input == 'c':
            print('\nCHANGE ITEM QUANTITY')
            itemToPurchase = input('Enter the item name\n')
            new_quantity = input('Enter the new quantity:\n')
            ShoppingCart.modify_item(itemToPurchase,new_quantity)
        elif user_input == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            ShoppingCart.output_items()
        elif user_input == 'o':
            print('\nOUTPUT SHOPPING CART')
            ShoppingCart.output_shoppingCart()

############################
if __name__ == "__main__":
    input_name = input("Enter customer's name:\n")
    input_date = input("Enter today's date:\n")

    customer1 = ShoppingCart(input_name,input_date)
    print_menu(customer1)

    # input_name2 = input()
    # input_date2 = input()
    #
    # customer2 = ShoppingCart(input_name2,input_date2)
    # print_menu(customer2)



# Second Part


#     print('Item 1')
#     input1_name = input("Enter the item name:\n")
#     input1_price = int(input("Enter the item price:\n"))
#     input1_quant = int(input("Enter the item quantity:\n"))
#
#     print('\nItem 2')
#     input2_name = input("Enter the item name:\n")
#     input2_price = int(input("Enter the item price:\n"))
#     input2_quant = int(input("Enter the item quantity:\n"))
#
#     print('\nTOTAL COST')
#     item1 = ItemToPurchase(input1_name,input1_price,input1_quant)
#     cost1 = item1.print_item_cost()
#     item2 = ItemToPurchase(input2_name,input2_price,input2_quant)
#     cost2 = item2.print_item_cost()
#     print('')
#     print('Total: ${}'.format(str(cost1+cost2)))


