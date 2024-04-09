import re
from utils import locate_obj
from engine import send_mud

def comm (player, action):
    if action == '^':
        player.send_message('Usage: ^<message>')
    else:
        send_mud.send_mud('^' + player.name.title() + ": " + action[1:])