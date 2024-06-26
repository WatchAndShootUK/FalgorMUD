from classes.map import Map

class GridMap(Map):
    def __init__(self):
        super().__init__(
            map_id='wa',
            map_name='West Arda',
            map_array=[
		'                             ^^^^^^',
		'                           ^^^^^^^^^',
		'                           ^^^^.*..~...................^^^^^^....................................^^                   ~~~~~',
		'                         ::^^^^...~~..................^^^^^.......................................^^           ~~~~~~~^^^^^',
		'                       ::..^^^^^~~~~~................^^^^^.........................................^^         ~.......^^^^^',
		'                     ::....^^^^~~~~~.................^^^^...........................................^^       ~.......^^^^^^^',
		'                    :....^^^^^~~~~~~~~...............^*^.............................................^^      ~.......^^^^^^^',
		'                   :.....^^^^^~~~~^^..~~~~~~~........^^...............................................^     ~.......^^^^^^^^',
		'                  :.......^^^~~^^^^*^........~~.......+...............................................^    ~.......^^^^^^^^^',
		'                 :........^^^^^^^^^^...........~......+...............................................~    ~.......^^^^^^^^^',
		'               ::..........^^^^^^^^^............~.....+...............................................~~~~~.........^^^^^^^^',
		'              :............^^^^..................~....+..............................................~.............^^^^^^^^',
		'              :............^^....................~....+............^^^..............................~.............^^^^^^^^^',
		'             :...................................~.....+.........^^^^^..............................~.............^^*^^^^^^',
		'             :..................................~......+........^^^^^^^............................~...............^^^^^^^^^',
		'            :..................................~*......+.........^^^^^^............................~..............^^^^^^^^^^',
		'            :..................................~........+.........^^^^^^..........................~...............^^^^^^^^^^',
		'           :..................................~.........+.........^^^^^^^.........................~................^^^^^^^^^O',
		'          :...................................~.........+.........^^^^^^^^^.......................~.................^^^^^^^^^',
		'         :....................................~.........+..........^^^^^^^^^.....................~..%%%....%%*%%%%...^^^^^^^^',
		'         :....................................~.....*...+.............^^^^^^^....................~%**%%%%%%%*%%%%%%%%%~~~~~~',
		'         :.......................*~...........~.........+...%%%%\'.......^^^^^^....++++++.........~%%%%%%*%%%%%%%%%%%~~',
		'         :........................~~.....^^^^..~........+...%*%\'\'\'.......^^.....++......++++++++.~%%%%%*%%%%%%%%%%%~  *',
		'         :.........................~~..........~.........+.^*%%\'\'\'\'.......^^..++................+=+%%%%%%%%%%%%%%%%~~~=~~~~~',
		'         ~..........................~..........~.....*...+.^*..\'\'\'.......^^^^+...................~+%%%%%%%%%%%%%%%%~%+%%%^^^^',
		'         :..........................~~~~~~~~~~~~...+++++++***..\'\'\'\'.......^^+...................~%+%%%%%%%%%%%%++++=+%%%%^^^^',
		'        :.....^^^......................*......+=+++.......+.+++.\'\'\'.....++++....................~%+%%%%%%*%%%%+%%~~%%%^^^^^^^',
		'       ::....^^^^^...................+++++++*+*~*%%%..^^^..+.*.+++++++++........................~%%++%%%%%%%%+%~~%%%%%^^^^^^',
		'      *.......^^^^................+++..........*~%%%%%%^^^.+....................................~%%%%++++++++~~%%%%%%^^^^',
		'     :.......^^*^+++...*.......+++*..............~%%%%~*^^.+....................................~%%%%%%%%%%~~%%%%%%%%^^^',
		'  ~::.........^^^^..+++++...+++....^^^^^^^^^*....~%%%~%%^^^.+...................................~%%%%%.%%%~%%%%%%%%%^^^^',
		' :...........^^^^^....+..+++.+...^^*^^^^^^^^......~%~%%%%^^^+^.................................~%%.....%%~%%%%%%%%%^^^^',
		':............^^^^^....+.......+....................~%%%%%%^^+^^^^..............................~%........~...%%%%%^^^^^',
		' ^^.........^^^^^^^..+........+....................~%%%%%%..+..^^^^............................~.........~........^^^^',
		'  ^^^.......^^^^^^^..+.........+...................~%%%%%%.+.....^^^.........^^................~........~........^^^^',
		'  ^^^^^......^^^....+...........+++..............*~%%%%%%%.+......^^^^^^^^^^^^^^...............~........~..........^^^',
		'   ^^^^^...........+...............+++.............~%%%%%%.+........^^^^^^^^^^^^^..............~.......~............^^^^',
		'     ^^^^^^.......+...................+.............~%%%%%.+...................................~......~.............^^^^^',
		'   ^^^^^^........+.....................+............~%%%...+...................................~....~~..............^^^^^^',
		'  ^^^^^.^......++.......................+..........~.......+...................................~...~................^^^^^^',
		' ^^^^^^.....+++..........................+........~........+..................................~..~~................^^^^^^',
		'^^^^^^...+++..............................++++...~.........+..................................~.~.................^^^^^^',
		'^^^^^.+++.....................................+++=++.......+.................................~~~..................^^^^^',
		'^^^*++..........................................~...++.....+.................................~.....................^^^^',
		'^^^^^...........................................~.....++....+................................~....................^^^^^',
		' ^^^^..........................................~........++..+...............................~....................^^^^^^',
		'  ^^^.......................................~~~...........+..+............................~~..................^^^^^^^^',
		' ^^^*......................................~...............+.+..........................~~............^^^^^^^^^*^^^',
		'^^^^^.....................................~.................++.........................~........................^^',
		'^.....................^*.................~....................+.......................~.........................^^^',
		'^^.................^^^^^^^............~~~......................+....................~~.........................^^^^^',
		'^^^...........^^^^^^^^^   ^..........~..........................+..................~............................^^^^^',
		' ^^*.^^^^^^^^^^^^^^^       ^........~............................+...............~~..............................^^^^',
		'  ^^^^^^^^^^^^^^^^          ^....~~~::............................+.............~................................^^^^',
		'   ^^^^^^^^^^^^^             ^^~~    :.............................+............~................................^^^^',
		'                                     :%.............................+..........~................................^^^^O',
		'                                    :%%%.............................+........~...............................^^^^^^',
		'                                    :%%%%............................+.......~~~~~............................^^^^^',
		'                                    :%%%%.............................+.....~~~~~~~~.........................^^^^^',
		'                                    :%%%%::............................+....~~~~~~..~~~~....................^^^^+*',
		'                                    :%%%:  :...........................+...~............~........++++++++..+++++~~',
		'                                     :%%:   ::..........................+.~..............~.....*+~~~~~~~~++~~~~~~^^',
		'                                     :%:      *:.......................*+~................~~~~~~~........~~...^^^^^^',
		'                                      :         :......................~=....................................^^^^^^',
		'                                                :.....................~..+..................................^^^^^^',
		'                                                 ::.................~~....++...............................^^^^^^',
		'                                                   ::..............~........+.............................^^^^^^',
		'                                                     ::..........~~..........+............................^^^^^^',
		'                                                       :::......~.............+............................^^^^^^',
		'                                                          :::::~...............+...........................^^^^^^',
		'                                                                :..*............+........................^^^^^^',
		'                                                               :.................+++...................^^^^^^^',
		'                                                               :....................+++..............^^^^^^^^^',
		'                                                               :.......................++..........^^^^^^^^^^^',
		'                                                               :.........................+.......^^^^^^^^^^^^^',
		'                                                               :..........................+....^^^^^^^^^^^^^^',
		'                                                               :...........................+..^^^^^^^^^^^^^^^^',
		'                                                               :............................+^^^^^^^^^^^^^^^^^',
		'                                                               :...........................^^+^^^^^^^^^^^^^^^',
		'                                                              :...........................^^^^+^^^^^^^^^^^^^',
		'                                                             :............................^^^^^+^^^^^^^^^^^',
		'                                                             :...........................^^^^^^+^^^^^^^^^^^',
		'                                                             :..........................^^^^^^^^++^*^^^^^^^^',
		'                                                             :.........................^^^^^^^^^^^++^^^^^^^^',
		'                                                              :........................^^^^^^^^^^^^^++^^^^^^^',
		'                                                               :.....~~~~~~~~.........^^^^^^^^^^^^^^^^++++++O',
		'                                                               :....~%%%%%%%%~.......^^^~~~~~^^^^^^^^^^~=~~~~',
		'                                                                ::.~%%%%%%%%%%~~....~~~~.....~~~~~~~~~~',
		'                                                                  ~%%%%%%%%%%%%%~~~~%%%%~......*........+.^^^^',
		'                                                                  :%%%%%%%%%%%%%%%%%%%%%%~...........+++..*^^^^^',
		'                                                                 :%%%%%%%%%%%%%%%%%%%%%%%%~~~=+++++++........^^^^',
		'                                                                :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%~~~~*..........^^^',
		'                                                                :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%~~~~~....^^^^',
		'                                                                 :%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^~~~~~^^',
		'                                                                 :%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^',
		'                                                                :%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^',
		'                                                                :%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^',
		'                                                                :%%%%%%%%^^^^^^^^^^^^^^^',
		'                                                               :%%%%%%%%^^^^^^',
		'                                                               :%%%%%%^^^^',
		'                                                               :%%%%%^^^',
		'                                                              :%%%%^^^^',
		'                                                              :%%%^^^',
		'                                                             :%%%^^^',
		'                                                            :%%%^^^',
		'                                                           :%%^^^^',
		'                                                           :%^^^',
		'                                                          :%^^',
		'                                                          :%^',
		'                                                         :%^',
		'                                                         ::^'

])