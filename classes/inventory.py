from utils.proper import proper

class Inventory(object):
    def __init__(self, parent):
        self.parent = parent
        self.hands = []
        self.wearing = []
        self.unhanded = []
        self.weapon = None
    
    def get_armour_power(self):
        total_power = 0
        for item in self.wearing:
            total_power += item.armour.power
        total_power = total_power/len(self.wearing)
        # Maximum armour power is 200
        return total_power if total_power < 200 else 200
   
    def got_hands(self):
        if len(self.hands) < 2:
            return True
        else:
            return False
    
    def drop(self,item):
        self.remove(item)
        self.parent.parent.items.insert(0,item)
        
    def remove(self,item):
        for itm in self.unhanded:
            if itm == item:
                self.unhanded.remove(item)
        for itm in self.wearing:
            if itm == item:
                self.wearing.remove(item)
                item.armour.worn = False
                self.parent.send_message('You remove ' + item.short.lower() + '.')                    
        for itm in self.hands:     
            if itm == item:
                self.hands.remove(item)
                if hasattr(item, 'weapon'):
                    item.weapon.wielded = False
                if itm == self.weapon:                
                    self.weapon = None
                    self.parent.send_message('You remove ' + item.short.lower() + '.')
                
    def get_body_parts(self):
        body_parts = []
        for item in self.wearing:
            for bp in item.armour.body_parts:
                body_parts.append(bp)
        return body_parts
    
    def append(self,item,destination):
        # ------------- A R M O U R -----------------
        if destination == 'wearing':
            if hasattr(item,'armour'):
                # Check if body slot is avaliable
                body_slot_avaliable = True
                body_part = ''
                for bp in item.armour.body_parts:
                    if bp in self.get_body_parts():
                        body_slot_avaliable = False
                        body_part = bp
                if body_slot_avaliable:
                    if item in self.hands:
                        self.hands.remove(item)                     
                    self.wearing.insert(0,item)
                    item.armour.worn = True
                    self.parent.send_message(item.short.lower() + ' : Ok.\nYou wear ' + item.short + '.')
                    return True
                else:
                    if item in self.wearing:
                        self.parent.send_message('You already wear it!')
                    else:
                        self.parent.send_message(item.short.lower() + ' : Failed.\nYou are already wearing something on your ' + body_part + '.')
                    return False
            else:
                self.parent.send_message('You cannot wear ' + item.short.lower() + '.')
                return False
            
        # ------------- H A N D S -----------------  
        elif destination == 'hands':            
            if len(self.hands) < 2:
                self.parent.send_message(item.short + ' : Ok.')
                self.hands.insert(0,item)
                if self.weapon == None and hasattr(item,'weapon'): # Auto-wield
                    self.append(item,'weapon')
                return True
            else:
                self.parent.send_message(item.short + ' : Your hands are full!\nFailed.')  
                return False
                        
                
        # ------------- W E A P O N -----------------    
        elif destination == 'weapon':
            if item in self.hands:
                # It's in your hands
                if hasattr(item,'weapon'):
                    if item.weapon.wielded:
                        self.parent.send_message(item.short.lower() + ' : You already wield it!')
                    else:
                        if self.weapon:
                            self.weapon.wielded = False
                            self.parent.send_message('You remove ' + proper(self.weapon.short) + '.')
                        self.weapon = item
                        item.weapon.wielded = True
                        self.parent.send_message('You wield ' + proper(item.short) + '.')                        
                        return True
                else:
                    self.parent.send_message('You can\'t wield ' + proper(item.short) + '.')                        
                    return False
            else:
                # It's on the floor
                if len(self.hands) < 2:
                    self.hands.insert(0,item)
                    self.parent.parent.items.remove(item)
                    self.append(item,'weapon')
                    return True
                else:
                    self.parent.send_message('Your hands are full')
                    return False
        elif destination == 'unhanded':
            self.unhanded.insert(0,item)
            return True
            
    def get_inventory(self):
        return self.hands + self.wearing + self.unhanded
    
    def show_inventory(self, player):
        for item in self.get_inventory():
            if item in self.hands:
                if item == self.weapon:
                    player.send_message(proper(item.short) + ' (wielded).') 
                else:
                    player.send_message(proper(item.short) + ' (in hands).') 
            elif item in self.wearing:
                player.send_message(proper(item.short) + ' (worn).')
            elif item in self.unhanded:
                player.send_message(proper(item.short) + '.')
            
            
