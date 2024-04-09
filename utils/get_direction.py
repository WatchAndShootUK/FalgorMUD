class GetDirection:   
    full_dirs = {
    'north':'n',
    'northwest':'nw',
    'south':'s',
    'northeast':'ne',
    'west':'w',
    'southwest':'sw',
    'east':'e',
    'northeast':'ne',
    'up':'u',
    'down':'d'}   
         
    brief_dirs = {
    'n':'north',
    's':'south',
    'w':'west',
    'e':'east',
    'u':'up',
    'd':'down',
    'ne':'northeast',
    'se':'southeast',
    'nw':'northwest',
    'sw':'southwest'}
    
    def __init__ (self,input_dir):        
        self.input_dir = input_dir    
    
    def __call__(self):
        if self.input_dir in self.full_dirs:
            return self.full_dirs[self.input_dir]
        else:
            return self.brief_dirs[self.input_dir]