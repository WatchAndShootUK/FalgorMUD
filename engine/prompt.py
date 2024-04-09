
from commands.command_signposter import CommandSignposter
from constants.debug import debug

def prompt(player):
    player.send_message('HP:' + str(round(player.hp)) + ' EP:' + str(round(player.ep)) + ' UID:' + player.parent.id + ' >')
    if debug:
        command = input()
    else:
        command = player.conn.recv(1024).decode().strip()
    CommandSignposter(player,command)