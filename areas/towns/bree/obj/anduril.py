from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='anduril, the Flame of the West',
            long='Aragorns sword LOL',
            aliases=['sword','flame','anduril','flame of the west','narsil']
        )    
        self.weapon = Weapon(5000,self)