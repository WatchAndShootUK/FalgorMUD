import json
from classes import player, stats, skills
from constants.players import players
from constants.debug import debug
from engine import enter_mud

def login(conn = None,addr = None):
    
    with open(r'json/ascii.json', 'r') as f:   
        if debug:     
            print(json.load(f)["title"])
        else:
            conn.send(json.load(f)["title"].encode())
    
    name = input() if debug else conn.recv(1024).decode().strip()
    
    name_avaliable = True
    for plyr in players:
        if plyr.name.lower() == name.lower():
            name_avaliable = False
  
    if name_avaliable:
        thisPlayer = player.Player(name = name,level = 19,gender = 'male', race = 'dunedain', location_str='158wa125',stats=stats.Stats(100,100,100,100,100,100),skills=skills.Skills(100,100,100,100,100,100))
        if debug == False:
            thisPlayer.conn = conn
            thisPlayer.addr = addr
        players.append(thisPlayer)
        enter_mud.enter_mud(thisPlayer)
    