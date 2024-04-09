from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='a polished cudgel',
            long='This cudgel is used to beat up criminals in Bree.',
            aliases=['cudgel','polished cudgel']
        )    
        self.weapon = Weapon(75,self)