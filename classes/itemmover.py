import re
from utils import locate_obj     
from classes import player as playerclass,item as itemclass
        
class ItemMover(object):
    def __init__ (self, player, syntax):
        self.player = player
        self.room = player.parent     
        self.command = None
        self.target_item = None
        self.target_item_index = None
        self.first_verb = None
        self.destination_item = None
        self.destination_item_index = None
        self.second_verb =None
        self.final_destination_item =  None
        self.final_destination_item_index =  None    
        
        patterns = [r'(get|drop|put|wear|wield|draw)\s+([a-z\s]+)\s?(\d+)?()?()?()?()?()?()?',
                    r'(get|drop|put|wear|wield|draw)\s+([a-z\s]+)\s?(\d+)?\s?(into|from)\s?([a-z\s]+)?\s?(\d+)?()?()?()?',
                    r'(get|drop)\s+([a-z\s]+)\s?(\d+)?\s?(from)\s?([a-z\s]+)?\s?(\d+)?\s?(into)\s?([a-z\s]+)?(\d+)?']
        for pattern in patterns:
            matches = re.match(pattern, syntax)
            if matches:
                self.command = matches.group(1).strip()
                self.target_item = matches.group(2).strip()
                self.target_item_index = int(matches.group(3)) if matches.group(3) else None
                self.first_verb = matches.group(4).strip() if matches.group(4) else None
                self.destination_item = matches.group(5).strip() if matches.group(5) else None
                self.destination_item_index = int(matches.group(6)) if matches.group(6) else None
                self.second_verb = matches.group(7).strip() if matches.group(7) else None
                self.final_destination_item = matches.group(8).strip() if matches.group(8) else None
                self.final_destination_item_index = int(matches.group(9)) if matches.group(9) else None              
        
        if self.command == 'get':
            if self.first_verb == None:
                self.basic_get()
            elif self.second_verb == None:
                self.get_into() if self.first_verb == 'into' else self.get_from()
            else:
                self.get_from_into()
                
        elif self.command == 'drop':
            if self.first_verb == None:
                self.basic_drop()
            elif self.second_verb == None:
                self.drop_from() if self.first_verb == 'from' else self.drop_from()
            else:
                self.drop_from_into()
                
        elif self.command == 'put':
            if self.second_verb == None:
                self.basic_put()
                
        elif self.command == 'wear':
            if self.first_verb == None:
                self.basic_wear()
            elif self.second_verb == None:
                self.wear_from_ground() if self.destination_item == 'ground' else self.wear_from()
            
        elif self.command == 'wield':
            if self.first_verb == None:
                self.basic_wield()
            elif self.second_verb == None:
                self.wield_from()
 
 
 # GET 
 
    def basic_get(self):
        gets = locate_obj.LocateObject([self.room],None).locate_item(self.target_item,
                                                                    self.target_item_index,
                                                                    locate_obj.ConditionQuery(None,itemclass.Item),
                                                                    locate_obj.Message(self.player,
                                                                                        'There is nothing here to get.' if self.target_item == 'all' else 'You don\'t see a ' + self.target_item + ' here.'))
        if gets:
            for item in gets:            
                if self.player.inv.append(item,'hands'):
                    self.room.items.remove(item)
                    self.room.chat_room(self.player.name.title() + ' gets ' + item.short.lower() + '.', [self.player])
      
    def get_into(self):
        into_item = locate_obj.LocateObject([self.player, self.room],None).locate_item(self.destination_item,
                                                                                     self.destination_item_index,
                                                                                     locate_obj.ConditionQuery('container',itemclass.Item),
                                                                                     locate_obj.Message(self.player,
                                                                                                        'There is no ' + self.destination_item + ' here.'))
        if into_item:
            into_item = into_item[0]
            gets = locate_obj.LocateObject([self.room],None).locate_item(self.target_item,
                                                                        self.target_item_index,
                                                                        locate_obj.ConditionQuery(None,itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           'There is nothing here to get.' if self.target_item == 'all' else 'You don\'t see that here.'))

            if gets:
                for item in gets:
                    if item is not into_item:
                            self.move_item(item,self.room,into_item)
                            self.room.chat_room(self.player.name.title() + ' gets ' + item.short.lower() + ' into ' + into_item.short.lower() + '.', [self.player])
                            self.ok_message(item)
                    else:
                        self.player.send_message('Nothing works that way.')
         
    def get_from(self):
        from_item = locate_obj.LocateObject([self.player,self.room],None).locate_item(self.destination_item,
                                                                                        self.destination_item_index,
                                                                                        locate_obj.ConditionQuery('container',itemclass.Item),
                                                                                        locate_obj.Message(self.player,
                                                                                                           'There is no ' + self.destination_item + ' here.'
                                                                                                           ))
        if from_item:
            from_item = from_item[0]
            gets = locate_obj.LocateObject([from_item],None).locate_item(self.target_item,
                                                                           self.target_item_index,
                                                                           locate_obj.ConditionQuery(None,itemclass.Item),
                                                                           locate_obj.Message(self.player,
                                                                                              'There is nothing in ' + from_item.short.lower() + '.' if self.target_item == 'all' else 'There is no ' + self.target_item + ' in ' + from_item.short.lower() + '.'))
            if gets:
                for item in gets:
                    if self.player.inv.append(item,'hands'):
                        # Remove it from source            
                        from_item.items.remove(item)
                        # Chat the move
                        self.room.chat_room(self.player.name.title() + ' gets ' + item.short.lower() + ' from ' + from_item.short.lower() + '.', [self.player])
    
    def get_from_into(self):
        into_item = locate_obj.LocateObject([self.player,self.room],None).locate_item(self.final_destination_item,
                                                                            self.final_destination_item_index,
                                                                            locate_obj.ConditionQuery('container',itemclass.Item),
                                                                            locate_obj.Message(self.player,
                                                                                               'There is no ' + self.final_destination_item + ' here.'))
        if into_item:
            into_item = into_item[0]
            from_item = locate_obj.LocateObject([self.player,self.room],None).locate_item(self.destination_item,
                                                                            self.destination_item_index,
                                                                            locate_obj.ConditionQuery('container',itemclass.Item),
                                                                            locate_obj.Message(self.player,
                                                                                               'There is no ' + self.final_destination_item + ' here.'))
            if from_item:
                from_item = from_item[0]                
                gets = locate_obj.LocateObject([from_item],None).locate_item(self.target_item,
                                                                            self.target_item_index,
                                                                            locate_obj.ConditionQuery(None,itemclass.Item),
                                                                            locate_obj.Message(self.player,
                                                                                               'There is nothing in ' + from_item.short.lower() + '.' if self.target_item_index == 'all' else 'You don\'t see ' + self.target_item + ' in ' + from_item.short.lower() + '.'))
                if gets:
                    # Move my items
                    for item in gets:
                        if item is not into_item:
                            self.move_item(item,from_item,into_item)
                            self.ok_message(item)
                            self.room.chat_room(self.player.name.title() + ' gets ' + item.short.lower() + ' from ' + from_item.short.lower() + ' into ' + into_item.short.lower() + '.')
         
# DROP
         
    def basic_drop(self):
        drops = locate_obj.LocateObject([self.player],None).locate_item(self.target_item,
                                                                        self.target_item_index,
                                                                        locate_obj.ConditionQuery(None,itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           'Drop what?'))   
        if drops:
            for item in drops:
                self.player.inv.remove(item)
                self.room.items.insert(0,item)
                self.room.chat_room(self.player.name.title() + ' drops ' + item.short.lower() + '.', [self.player])
                self.ok_message(item)
   
    def drop_from(self):
        from_item = locate_obj.LocateObject([self.player, self.room],None).locate_item(self.destination_item,
                                                                        self.destination_item_index,
                                                                        locate_obj.ConditionQuery('container',itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           self.destination_item + ' isn\'t a container.')) 
        if from_item:
            from_item = from_item[0]
            drops = locate_obj.LocateObject([from_item],None).locate_item(self.target_item,
                                                                        self.target_item_index,
                                                                        locate_obj.ConditionQuery(None,itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           'There is nothing in ' + from_item.short.lower() + '.' if self.target_item == 'all' else 'You don\'t see ' + self.target_item + ' in ' + from_item.short.lower()))
            if drops:
                for item in drops:
                    self.move_item(item,from_item,self.room)                    
                    self.ok_message(item)
                    self.room.chat_room(self.player.name.title() + ' drops ' + item.short.lower() + ' from ' + from_item.short.lower() + '.', [self.player])
     
    def drop_into(self):
        into_item = locate_obj.LocateObject([self.player, self.room],None).locate_item(self.destination_item,
                                                                        self.destination_item_index,
                                                                        locate_obj.ConditionQuery('container',itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           self.destination_item + ' isn\'t a container.')) 
        if into_item:
            into_item = into_item[0]
            drops = locate_obj.LocateObject([into_item],None).locate_item(self.target_item,
                                                                        self.target_item_index,
                                                                        locate_obj.ConditionQuery(None,itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           'There is nothing in ' + into_item.short.lower() + '.' if self.target_item == 'all' else 'You don\'t see ' + self.target_item + ' in ' + into_item.short.lower()))
            if drops:
                for item in drops:                    
                    self.player.inv.remove(item)  
                    into_item.items.insert(0,item)                  
                    self.ok_message(item)
                    self.room.chat_room(self.player.name.title() + ' drops ' + item.short.lower() + ' into ' + into_item.short.lower() + '.', [self.player])
          
    def drop_from_into(self):  
        into_item = locate_obj.LocateObject([self.room],None).locate_item(self.final_destination_item,
                                                                        self.final_destination_item_index,
                                                                        locate_obj.ConditionQuery('container',itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           self.destination_item + ' isn\'t a container.')) 
        if into_item:
            into_item = into_item[0]
            from_item = locate_obj.LocateObject([self.player],None).locate_item(self.destination_item,
                                                                        self.destination_item_index,
                                                                        locate_obj.ConditionQuery('container',itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           'You dont\'t have a ' + self.destination_item + '.')) 
            if from_item:
                from_item = from_item[0]
                drops = locate_obj.LocateObject([from_item],None).locate_item(self.target_item,
                                                                        self.target_item_index,
                                                                        locate_obj.ConditionQuery('container',itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                           'There is nothing in ' + from_item.short.lower() + '.' if self.target_item == 'all' else 'You don\'t see ' + self.target_item + ' in ' + from_item.short.lower() + '.'))       
                if drops:
                    for item in drops:
                        print(into_item.short)
                        self.move_item(item,from_item,into_item)
                        self.ok_message(item)
                        self.room.chat_room(self.player.name.title() + ' drops ' + item.short.lower() + ' from ' + from_item.short.lower() + ' into ' + into_item.short.lower() + '.', [self.player])                                  


# WEAR

    def basic_wear(self):
        wears = locate_obj.LocateObject([self.player] if self.target_item == 'all' else [self.player,self.room],None).locate_item(
                                                                                                                                self.target_item,
                                                                                                                                self.target_item_index,
                                                                                                                                locate_obj.ConditionQuery('armour',itemclass.Item),
                                                                                                                                locate_obj.Message(self.player,
                                                                                                                                                    'You have no armour to wear!' if self.target_item == 'all' else 'No ' + self.target_item + ' here!'))        
        if wears:
            for item in wears:    
                if self.player.inv.append(item,'wearing'):                            
                    if item in self.room.items:
                        self.room.items.remove(item)
                    self.room.chat_room(self.player.name.title() + ' wears ' + item.short.lower() + '.', [self.player])        
    
    def wear_from(self):            
        from_item = locate_obj.LocateObject([self.player,self.room],None).locate_item(
                                                                                    self.destination_item,
                                                                                    self.destination_item_index,
                                                                                    locate_obj.ConditionQuery('container',itemclass.Item),
                                                                                    locate_obj.Message(self.player,
                                                                                                    'There is no ' + self.destination_item + ' near you'))
        if from_item:
            from_item = from_item[0]
            wears = locate_obj.LocateObject([from_item],None).locate_item(
                                                                        self.target_item,
                                                                        self.target_item_index,
                                                                        locate_obj.ConditionQuery('armour',itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                        'There is no ' + self.destination_item + ' in ' + from_item.short.lower() + '.'))
            if wears:
                for item in wears:
                    if self.player.inv.append(item,'wearing'):
                        from_item.items.remove(item)
                        self.room.chat_room(self.player.name.title() + ' wears ' + item.short.lower() + '.', [self.player]) 
       
    def wear_from_ground(self):            
        wears = locate_obj.LocateObject([self.room],None).locate_item(
                                                                        self.target_item,
                                                                        self.target_item_index,
                                                                        locate_obj.ConditionQuery('armour',itemclass.Item),
                                                                        locate_obj.Message(self.player,
                                                                                        'There is no armour on the ground' if self.target_item == 'all' else 'There is no ' + self.target_item + 'here!'))
        if wears:
            for item in wears:
                if self.player.inv.append(item,'wearing'):
                    self.room.items.remove(item)
                    self.room.chat_room(self.player.name.title() + ' wears ' + item.short.lower() + '.', [self.player]) 
                    
# PUT
    
    def basic_put(self):
        into_item = locate_obj.LocateObject([self.player, self.room],None).locate_item(self.destination_item,
                                                                            self.destination_item_index,
                                                                            locate_obj.ConditionQuery('container',itemclass.Item),
                                                                            locate_obj.Message(self.player,
                                                                                               'There is no ' + self.destination_item + ' here.'))
        if into_item:
            into_item = into_item[0]
            puts = locate_obj.LocateObject([self.player],None).locate_item(self.target_item,
                                                                            self.target_item_index,
                                                                            locate_obj.ConditionQuery(None,itemclass.Item),
                                                                            locate_obj.Message(self.player,
                                                                                               'Put what into what?'))
            if puts:
                for item in puts:
                    if item is not into_item:                        
                        self.player.inv.remove(item)
                        into_item.items.insert(0,item)
                        self.ok_message(item)                        
                        self.room.chat_room(self.player.name.title() + ' puts ' + item.short.lower() + ' into ' + into_item.short.lower() + '.', [self.player])
           
# WIELD

    def basic_wield(self):
        weapons = locate_obj.LocateObject([self.player,self.room],None).locate_item('not_today_sir' if self.target_item == 'all' else self.target_item,
                                                                                    self.target_item_index,
                                                                                    locate_obj.ConditionQuery('weapon',itemclass.Item),
                                                                                    locate_obj.Message(self.player,
                                                                                                       'Wield what?'))
        if weapons:
            self.player.inv.append(weapons[0],'weapon')
                         
# FUNCS
          
    def move_item(self,item,move_from,move_to):
        move_from.items.remove(item)
        move_to.items.insert(0,item)
        item.parent = move_to
        
        if hasattr(move_from,'armour') and ' containing ' in move_from.short:
            move_from.short = move_from.short.split('containing')[0]
    
    def ok_message(self,item):        
        if self.target_item == 'all':
            self.player.send_message(item.short.lower() + ' : Ok.')
        else:
            self.player.send_message('Ok.')