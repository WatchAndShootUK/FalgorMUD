from classes.map import Map

class TownMap(Map):
    def __init__(self):
        super().__init__(
            map_id='br',
            map_name='bree',
            map_array=[
'a +-o-o',
'| |',
's-+-o        i',
'  |         /',
'o |    o   b-o',
'| |    |   |',
'+-+----+-+-o',
'  |\   | | |',
'  | s  o o o',
'  |      |',
'  |      o',
'o-+-o',
'  |',
'  +-x',
'  |',
'  o'
])
        