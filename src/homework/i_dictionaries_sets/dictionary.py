def main():
     inventory = {'Widget1' : 10}
     widget = str(input('Enter your widget: '))
     quantity = int((input('Enter your quantity: ')))

     add_inventory(inventory, widget, quantity)

     print(inventory)
     

def add_inventory(inventory, widget, quantity):

    if widget not in inventory:
        inventory[widget] = quantity
    else:
        inventory[widget] += quantity

    return inventory
 

def remove_inventory(inventory, widget):

    if widget in inventory:
            del inventory[widget]
    else: 
         print('Item not Found.')


    return inventory 

#if &value& not in inventory: print('Item not Found.')