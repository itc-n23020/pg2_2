def display_inventory(inventory):
    print ('持ち物リスト：')
    item_total = 0
    for k, v in inventory.items():
        print (str(inventory[k]) + ' ' + k)
        item_total += v
    print ('総アイテム数: ' + str(item_total))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return inventory

inv = {'金貨': 42,'ロープ': 1}
dragon_loot = ['金貨','手裏剣','金貨','金貨','ルビー']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
