import re

def inventory (player, action):
    if re.match(r'^\w+$',action):
        player.show_inv()
    else:
        player.send_message('Usage: \'inventory\' or \'i\'')