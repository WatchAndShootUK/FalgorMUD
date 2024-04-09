 
class Stats(object):
    def __init__(self,strength,constitution,agility,coordination,charisma,intelligence):
        self.strength = int(strength)
        self.constitution = int(constitution)
        self.agility = int(agility)
        self.coordination = int(coordination)
        self.charisma = int(charisma)
        self.intelligence = int(intelligence)
        
    def get_avg(self):
        i = self.strength + self.constitution + self.agility + self.coordination + self.charisma + self.intelligence
        return round(i/6)
    