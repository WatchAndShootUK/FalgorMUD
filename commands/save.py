import re

def save (player, action):
    if re.match(r'^\w+$',action):
        player.send_message('There is nothing to save, but thanks for trying.')
    else:
        player.send_message('Usage: \'save\'')