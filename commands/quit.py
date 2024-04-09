from constants.players import players

def quit(player,direction):
    player.send_message("Goodbye, thanks for playing!")
    for item in player.inv.get_inventory():
        player.inv.drop(item)
    #player.conn.close()
    #del instanceGlobals.clients[player.conn]
    player.parent.items.remove(player)
    player.parent.chat_room(player.name + " left the game.")