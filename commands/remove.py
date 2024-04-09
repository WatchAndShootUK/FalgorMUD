import re
from utils import locate_obj
from classes import item as itemclass

def remove(player,action):
    if re.match(r'^\w+$',action):
        player.send_message('Remove what?')
    else:
        remove_item = locate_obj.LocateObject([player],action).locate_item(None,
                                                                             None,
                                                                             locate_obj.ConditionQuery(None,itemclass.Item),
                                                                             locate_obj.Message(player,
                                                                                                'Remove what?'))
        if remove_item:
            remove_item = remove_item[0]
            if remove_item in player.inv.wearing:
                # Armour
                if player.inv.got_hands():
                    player.inv.wearing.remove(remove_item)
                    player.inv.hands.insert(0,remove_item)
                    player.send_message('You hold ' + remove_item.short.lower() + '.')
                else:
                    player.send_message('Your hands are full, where would you put it if your removed it?')
            elif remove_item == player.inv.weapon:
                # Weapon
                remove_item.wielded = False
                player.inv.weapon = None
                player.send_message('You hold ' + remove_item.short.lower() + '.')
            elif remove_item in player.inv.heands:
                player.send_message(remove_item.short.capitalize() + ' is already in your hands.')
            else:               
                player.send_message('You can\'t remove that item.')
                
                    