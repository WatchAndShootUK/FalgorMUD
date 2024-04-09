from constants.corpses import corpses
from constants.combats import combats

def heartbeat():
    for combat in combats:
        combat.combat_heartbeat()

    for corpse in corpses:
        corpse.corpse_heartbeat()