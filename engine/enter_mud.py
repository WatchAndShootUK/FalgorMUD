import threading
from engine import prompt
from constants.rooms import rooms

def enter_mud(player):
    player.send_message("Wecome to the Two Towers MUD, " + player.name.title() + "!")
    #instanceGlobals.rooms[player.location_str].append(player)
    rooms[player.location_str].append(player)
        
    player_thread = threading.Thread()
    player.thread = player_thread
    player_thread.start()
    
    while True:
        prompt.prompt(player)   