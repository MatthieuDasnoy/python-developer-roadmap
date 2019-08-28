player_inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(some_dictionary):
    item_total = 0
    print('Inventory:')

    for k, v in some_dictionary.items():
        print(v, k)
        item_total += v
        
    print('Total number of items: ' + str(item_total))

def addToIventory(some_dictionary, some_list):
    for i in some_list:
        some_dictionary.setdefault(i, 0)    
        some_dictionary[i] += 1             

    return some_dictionary

player_inventory = addToIventory(player_inventory, dragon_loot)
displayInventory(player_inventory)

