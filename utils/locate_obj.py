import re
from classes import player, room, npc

class Message(object):
    def __init__(self, _player, _message):
        self.player = _player
        self.message = _message
        
class ConditionQuery(object):
    def __init__(self, _hasattr = None, _isinstance = None):
        self.hasattr = _hasattr
        self.isinstance = _isinstance
    
    def check_conditions(self, item):
        conditions_met = True
        
        if self.hasattr:
            conditions_met = hasattr(item, self.hasattr) and conditions_met

        if self.isinstance:
            conditions_met = isinstance(item, self.isinstance) and conditions_met

        return conditions_met
            
            
        
class LocateObject(object):
    # Searches the room and inv of a player for any matches of search item.
    def __init__(self,search_area,query = None):
        self.search_areas = search_area # Places to look []
        self.target_item_name = None
        self.target_item_index = None
        if query != None:
            match = re.match(r'([a-zA-Z\s]+)\s?(\d+)?',query.replace(query.split()[0] + ' ', '', 1)) # Pattern to look for {}
            self.target_item_name = str(match.group(1).strip()) if match.group(1) else None
            self.target_item_index = int(match.group(2).strip()) if match.group(2) else None
    
    def locate_item(self, target_item_name = None, target_item_index = None, condition_query = None, message = None): # Locate a single item
        if target_item_name:
            self.target_item_name = target_item_name
        if target_item_index:
            self.target_item_index = target_item_index
        
        poss_items = []
        for search_area in self.search_areas:
            if isinstance(search_area,player.Player) or isinstance(search_area,npc.NPC):
                search_list = search_area.inv.get_inventory()
            else:
                search_list = search_area.items                
            for item in search_list:          
                add_item = False               
                if self.target_item_name == 'all' or self.target_item_name in item.aliases:
                    add_item = True                    
                    if condition_query:
                        add_item = condition_query.check_conditions(item)
                
                if add_item:
                    poss_items.append(item)       
                        
        if poss_items:
            if self.target_item_name == 'all':
                return poss_items
            else:
                if self.target_item_index:
                    return [poss_items[self.target_item_index-1]]
                else:
                    return [poss_items[0]]
        else:            
            if message:
                # Send specific failure message
                message.player.send_message(message.message)
            return []