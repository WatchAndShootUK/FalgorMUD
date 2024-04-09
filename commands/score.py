import re

def score(player,action):
    if re.match(r'^\w+$',action):
        player.score()
    else:
        player.send_message('Usage: \'score\'')
    