import re
from constants.combats import combats
from utils import locate_obj

def shape (player,action):
    if " " in action:
        target = locate_obj.LocateObject([player.parent],action).locate_item(None,
                                                                             None,
                                                                             locate_obj.ConditionQuery('hp',None),
                                                                             locate_obj.Message(player,
                                                                                                'Shape what?'))
        if target:
            player.send_message(target[0].shape.get_hp_shape())        
    else:
        void_shape = True
        for combat in combats:
            if player == combat.attacker or player == combat.defender:
                if combat.attacker in player.parent.items and combat.defender in player.parent.items:
                    void_shape = False
                    if combat.attacker is player:
                        player.send_message(combat.defender.shape.get_hp_shape())
                    else:
                        player.send_message(combat.attacker.shape.get_hp_shape())
        if void_shape:
            player.send_message("Usage: shape <target>")
    