import re
from utils import locate_obj
from classes.npc import NPC

def look (player, action):
    if re.match(r'^\w+$',action):
        player.parent.display_long(player)
    elif re.match(r'^(l|look)\s?([a-z\s]+)?\s?(\d+)?\s?in\s?([a-z\s]+)?\s?(\d+)?',action):
        match = re.match(r'^(l|look)\s?([a-z\s]+)?\s?(\d+)?\s?in\s?([a-z\s]+)?\s?(\d+)?',action)
        item = match.group(2).strip()
        item_index = int(match.group(3)) if match.group(3) else None
        npc = match.group(4).strip()
        npc_index = int(match.group(5)) if match.group(5) else None
        look_in = locate_obj.LocateObject([player.parent],None).locate_item(npc,
                                                                            npc_index,
                                                                            locate_obj.ConditionQuery(None,NPC),
                                                                            locate_obj.Message(player,
                                                                                               'You don\'t see ' + npc + ' here.'))
        if look_in:
            look_item = locate_obj.LocateObject([look_in[0]],None).locate_item(item,
                                                                            item_index,
                                                                            None,
                                                                            locate_obj.Message(player,
                                                                                               'There is no ' + item + ' in ' + look_in[0].short.lower() + '.'))
            if look_item:
                look_item[0].display_long(player)
        
    else:
        target = locate_obj.LocateObject([player,player.parent],action).locate_item(None,
                                                                             None,
                                                                             None,
                                                                             locate_obj.Message(player,
                                                                                                'You don\'t see that here.'))
        if target:
            target[0].display_long(player)