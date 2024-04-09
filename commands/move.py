from constants.rooms import rooms
from utils.get_direction import GetDirection

def move(player, direction):
    if direction in GetDirection.full_dirs:
        direction = GetDirection(direction)
    
    if direction in player.parent.exits:
        player.parent.chat_room(player.name.title() + " leaves " + GetDirection(direction)() + ".",[player])   
        rooms[player.parent.exits[direction]].append(player)    
    else:
        player.send_message("You can't go that way!")