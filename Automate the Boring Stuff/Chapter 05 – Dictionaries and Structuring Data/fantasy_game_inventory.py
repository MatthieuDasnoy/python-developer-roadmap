player_inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(some_dict):
    items_total = 0

    print('Inventory:')

    for k, v in some_dict.items():
        print(v, k)
        items_total += v
        
    print('Total number of items: ' + str(items_total))

def addToIventory(some_dict, some_list):
    for i in some_list:
        some_dict.setdefault(i, 0)    
        some_dict[i] += 1             

    return some_dict

player_inventory = addToIventory(player_inventory, dragon_loot)
displayInventory(player_inventory)
