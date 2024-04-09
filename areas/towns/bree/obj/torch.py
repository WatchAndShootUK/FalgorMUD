from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='a torch',
            long='This is a burning piece of wood.',
            aliases=['torch']
        )    
        self.weapon = Weapon(25,self)