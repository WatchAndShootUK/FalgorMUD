class Map:
    def __init__ (self,map_id,map_array,map_name):
        self.id = map_id
        self.map_name = map_name
        self.map_array = self.bulk_map(map_array)     
        
    def bulk_map(self, map_array):        
        width = 0
        for line in map_array:
            if len(line) > width:
                width = len(line)+200
        padding = ' ' * 100   
        
        for i in range(len(map_array)):
            # Fill all spaces to make rectangular 2d array
            whitespace = width-len(map_array[i])
            map_array[i] += ' '*whitespace
            
            # Apply padding
            map_array[i] = padding + map_array[i] + padding
        
        for i in range(100):
            map_array.insert(0,' ' * width)
            map_array.append(' ' * width)
        
        self.width = width
        self.height = len(map_array)
    
        return map_array