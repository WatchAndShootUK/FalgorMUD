from constants.players import players

def who (player, action):
    player.send_message('The Two Towers [Apocolypse Edition]')
    player.send_message('')
    for plyr in players:
            player_length = str(plyr.name.title()) + " the " + plyr.race + '(' + str(plyr.level) + ")"
            spacer_length = int(300-len(player_length))
            who_line = str(str(plyr.name.title()) + " the " + plyr.race + ' ' * spacer_length + '(' + str(plyr.level) + ")")
            player.send_message(who_line)    
    player.send_message('Total users:' + str(len(players)))