
class Skills(object):
    def __init__(self,attack,aim,defence,dodge,awareness,fire_building):
        self.attack = int(attack)
        self.aim = int(aim)
        self.defence = int(defence)
        self.dodge = int(dodge)
        self.awareness = int(awareness)
        self.fire_building = int(fire_building)        
        
    def get_avg(self):
        i = self.attack + self.aim + self.defence + self.dodge
        return round(i/4)
    