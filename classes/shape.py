class Shape(object):
    def __init__(self,parent):
        self.parent = parent
    
    def get_hp_shape(self):
        max_hp = self.parent.max_hp
        current_hp = self.parent.hp
        
        current_shape = round((current_hp/max_hp)*100)
        
        if current_shape == 100:
            return (self.parent.name.title() + ' is in perfect shape.' + str(current_hp))
        elif current_shape > 75:
            return (self.parent.name.title() + ' is in good shape.' + str(current_hp))
        elif current_shape > 50:
            return (self.parent.name.title() + ' is in average shape.' + str(current_hp))
        elif current_shape > 25:
            return (self.parent.name.title() + ' doesn\'t look so great.' + str(current_hp))
        elif current_shape > 0:
            return (self.parent.name.title() + ' is near death.' + str(current_hp))
        elif current_shape <= 0:
            return (self.parent.name.title() + ' is in critical condition, very close to death.' + str(current_hp))