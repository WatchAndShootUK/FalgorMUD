from copy import deepcopy
import importlib
import os
import re
from utils import locate_obj
from engine import send_mud

def map (player, action):
    match = re.match(r'^map (\w+)',action)
    if match:
        if match.group(1) == 'small':
            if player.settings.map_radius == 5:
                player.send_message('Your map is already as small as it will go.')
            else:
                player.settings.map_radius = 5
                player.send_message('You fold your map into a smaller size.')
        elif match.group(1) == 'medium':
            if player.settings.map_radius == 15:
                player.send_message('Your map is already its normal size.')
            else:
                player.settings.map_radius = 15
                player.send_message('You return your map to its normal size.')
        elif match.group(1) == 'large':
            if player.settings.map_radius == 20:
                player.send_message('Your map is already completely unfolded.')
            else:
                player.settings.map_radius = 20
                player.send_message('You unfold your map, as large as it will go!')
        else:
            player.send_message('Usage: map <small/medium/large>')
    else:        
        id = player.parent.id
        grid = get_map(id)
        numbers = re.findall(r'\d+', id)    
        if len(numbers) >= 2:
            column, row = int(numbers[0]),int(numbers[1])
        radius = player.settings.map_radius
        width = [column-radius,column+radius]
        height = [row-radius,row+radius]
        
        for line in range(height[0],height[1]):
            if line == row:
                replace_line =  grid[line][:column] + '!' + grid[line][column+1:]               
                player.send_message(replace_line[width[0]:width[1]])
            else:
                player.send_message(grid[line][width[0]:width[1]])
    
def get_map(id):
    match = re.search(r'\d+([a-zA-Z]+)\d+', id)
    if match:
        map_code = match.group(1)
        for root, _, files in os.walk('areas'):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    spec = importlib.util.spec_from_file_location(file, full_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    for name in dir(module):
                        obj = getattr(module, name)
                        if hasattr(obj, '__class__') and obj.__class__.__name__ == 'type' and name in ['GridMap','TownMap']:
                            thisMap = obj()
                            if thisMap.id == map_code:
                                return thisMap.map_array
    else:
        print('cant find map code from ' + id)