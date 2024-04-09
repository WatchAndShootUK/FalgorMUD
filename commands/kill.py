import re
from classes import npc,combat
from constants.combats import combats
from utils import locate_obj

def kill (player, action):
    if re.match(r'^\w+$',action):
        player.send_message('Attack what?')
    else:
        target = locate_obj.LocateObject([player.parent],action).locate_item(None,
                                                                             None,
                                                                             locate_obj.ConditionQuery('hp',npc.NPC),
                                                                             locate_obj.Message(player,
                                                                                                'You can\'t attack that.'))
        if target:
            player.in_combat, target[0].in_combat = True, True
            combats.append(combat.Combat(target[0],player))