from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='a many-tailed whip',
            long='The fiery whip of a Balrog!',
            aliases=['whip','many tailed whip']
        )    
        self.weapon = Weapon(150,self)