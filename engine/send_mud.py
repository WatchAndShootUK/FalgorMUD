from constants.players import players
from constants.debug import debug
from constants.clients import clients

def send_mud(message):
    if debug:
        print(message)
    else:
        for client in clients:
            client.send(message.encode() + b"\n" )