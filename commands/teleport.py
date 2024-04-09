import re
from constants.rooms import rooms

def teleport (player, action):
    match = re.match(r'^teleport (\w+)',action)
    if match:
        target_room_uid = match.group(1) if match.group(1) else None
        if target_room_uid:
            if target_room_uid in rooms:
                player.send_message('You teleport and find yourself elsewhere...')                
                rooms[match.group(1)].append(player)
            else:
                player.send_message('You try to summon your inner power to teleport but can\'t seem to visualise where you want to go!')