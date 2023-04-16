from castle import Castle
from player import Player
from diamond import Diamond
from room import Room
FIRST_PLAYER_ID = 0
SECOND_PLAYER_ID = 1
INITIAL_TURN = 0

class Game:

    def __init__(self):
        self.castle = Castle()                                              #creates castle object
        self.players = [Player(FIRST_PLAYER_ID),Player(SECOND_PLAYER_ID)]   #creates players list
        self.finished = []                                                  #creates finished list
        self.turn = INITIAL_TURN                                            #turn parameter

    def initialize_from_file(self,filename) -> None:
        '''
        read a file containing the information about the Castle,
        create the Castle based on the information provided,
        set the initial position of the players to the room with the entrance.
        read the file, build the castle, set initial position of the players
        '''
        castle_info = self.read_room_file(filename)                             #returns text file in list[list]
        entrance = self.get_entrance_info(castle_info)                            #returns entrance info
        exit = self.get_exit_info(castle_info)                                  #returns exit info
        self.set_player_initial_position(entrance)                               #sets initial position of the player
        self.set_exit(exit)                                                     #sets exit door info
        self.set_entrance(entrance)                                               #sets entrance door info
        rooms_info = self.extract_rooms_info(castle_info)                       #returns door info of each room
        self.build_castle(rooms_info)                                           #build castle
        

    def read_room_file(self,filename) ->list:
        '''
        reads the file contains room information and return it in nested list format
        '''
        with open(filename,'r') as file:                                       #opens file
            text=file.readlines()                                           
        
        for line_index in range(len(text)):
            text[line_index] = text[line_index].strip()                       #strips /n character from each line
            
        #print(text)
        return text
        

    def get_entrance_info(self,castle_info) -> str:
        '''
        returns entrance info of the castle
        '''
        for line in castle_info:                
            if line[0] == "E":                                              # looks for the line that has first letter "E" which means that line contains room ID, door direction of entrance
                line = line.split(":")
                line= line[1].strip()
                #print(line)        
                return line                                                 #return line format is "5,S"
    
    def get_exit_info(self,castle_info) -> str:
        '''
        returns exit info of the castle
        '''
        for line in castle_info:
            if line[0] == "X":                                          #looks for the line that has first letter "X" which means that line contains room ID, door direction of exit
                line = line.split(":")
                line= line[1].strip()
                #print(line)
                return line                                             #return line format is "24,S"

    def set_player_initial_position(self,entrance) ->None:
        '''
        sets the initial position of each player
        '''
        entrance_room_id = int(entrance[0])
        for player in self.players:
            player.set_position(entrance_room_id)
        
    def set_exit(self,exit) -> None:
        '''
        sets the exit info in the castle object
        '''
        input_direction = ["NORTH",'SOUTH','EAST','WEST']
        direction = ['N','S','E','W']

        exit = exit.split(",")
        id = int(exit[0])
        door = exit[1].strip()
        door = input_direction[direction.index(door)]
        #print('exit info',id,door)
        self.castle.set_exit_id_door_number(id,door)
    
    def set_entrance(self,entrance) ->None:
        '''
        sets the entrance info in the castle object
        '''
        input_direction = ["NORTH",'SOUTH','EAST','WEST']
        direction = ['N','S','E','W']

        entrance = entrance.split(",")
        id = int(entrance[0])
        door = entrance[1].strip()
        door = input_direction[direction.index(door)]
        self.castle.set_entrance_id_door_number(id,door)

    def extract_rooms_info(self,castle_info) ->list[list]:
        '''
        return the list which contains room information
        '''
        rooms_info = []
        for line in castle_info:
            if line[0] != "E" and line[0] != 'X': 
                line = line.split(":")                           #['25', ' 18, 0, 0, 20,']
                line[1]= line[1].split(",")                      #['25', [' 18', ' 0', ' 0', ' 20', '']]
                rooms_info.append(line)
        #print(rooms_info)
        return rooms_info

    def build_castle(self,rooms_info) ->None:
        '''
        builds the castle room based on the info provided
        '''
        input_direction = ["NORTH",'SOUTH','EAST','WEST']

        for room in rooms_info:
            room_id = int(room[0])                  # first element of the list - int type
            room_info = room[1]                     # second element of the list- list type
            self.castle.add_room(room_id)           # creates room object associated with room id
            room = self.castle.get_room(room_id)    # return the room object associated with room_id
            room.set_id(room_id)
            for i in range(len(room_info)):
                if i <4:
                    try:
                        room.set_link(input_direction[i],int(room_info[i].strip()))             #sets link for each room
                    except:
                        if (room_info[i].strip()) == "E":                                       #if door has 'E"(entrance), it will set 'entrance' string
                            room.set_link(input_direction[i],'entrance')
                        elif (room_info[i].strip()) == "X":                                     #if door has "X"(exit), it will set 'exit' string
                            room.set_link(input_direction[i],'exit')
                if i ==4:
                    if len(room_info[i]) != 0:                                                  #checks whether 5 element is empty means room does not contain anything
                        self.add_room_content(room_id,room_info[i])                             #helpher function to add room content
    
    def add_room_content(self,room_id : int,room_content: str) -> None:
        '''
        adds room content in the given room_id
        '''
        room_content = room_content.strip()         #removes the white space present in front of the string when it passes to the current function
        diamond = Diamond(0)                        #initial value
        portal = False                              #initial value
        wormhole = False                            #initial value
        #print(room_content)
        if room_content == "W":                     #means it has wormhole
            wormhole =  True
        if room_content == "P":                     #means it has portal
            portal = True
        if room_content[0] =="D":                   #means it has diamonds
            number_of_diamonds = len(room_content)  #count the number of diamonds the room should have
            diamond.set_diamonds(number_of_diamonds)
        
        self.build_room(room_id,diamond,portal,wormhole)

    def build_room(self, room_id, diamond, portal, wormhole) -> None:
        '''
        Adds the features to the room
        '''
        room = self.castle.get_room(room_id)
        
        if portal:
            room.set_portal(portal)
        if wormhole:
            room.set_wormhole(wormhole)
        if diamond.get_diamonds() != 0:
            room.set_diamond(diamond)
    
    def get_turn(self) -> int:
        '''
        return the index of the player who's the turn to play
        '''
        return self.turn
    
    def set_turn(self, turn) -> None:
        '''
        sets the index of the player who's the turn to play
        '''
        self.turn = turn
    
    def get_player(self,player_id) -> object:
        '''
        receives a player ID and returns the Player object corresponds
        to that given player_ID.
        '''
        for player in self.players:
            if player.get_player_id() == player_id:
                return player                           #returns player object
    
    def move(self) -> None:
        '''
        asks the user to enter a decision(North, South, East, West)
        and move the player whose turn it is
        '''
        valid_direction = ["NORTH",'SOUTH','EAST','WEST']
        player_id = self.get_turn()
        player = self.get_player(player_id)                             #gets player object related to player id
        current_player_room = player.get_position()
        valid = False
        if player.get_finished() == False:
            print("It's player %s turn" %((player.get_player_id())+1))

            while not valid:
                decision = input("Please input a direction (North, South, East, West): ")
                if decision.upper() in valid_direction:
                    valid = True
                else:
                    print('Please enter a valid input')
            print('Player %d , previous room %d' %((player.get_player_id())+1,current_player_room))  #increments the player id because 0 should print as 1
            next_room_id = self.castle.get_next_room(int(current_player_room),str(decision))
            if next_room_id == 0:
                print("It's a blocked door. Player %s can't move further" %((player.get_player_id())+1))
            elif next_room_id == "entrance":
                print("It's the entrance. Player %s can't move further" %((player.get_player_id())+1))
            elif next_room_id == 'exit':
                print('Player %d exited the castle! %s'%((player.get_player_id())+1,decision))
                player.set_finished()                                                           #sets that player exited the castle
            else:
                print('Player %d , %s , New room  %s'%((player.get_player_id())+1,decision,next_room_id))
                player.add_to_path(current_player_room,decision)
                player.move(next_room_id)
                self.update_diamonds()
            

    def is_finished(self) -> bool:
        ''''
        checks whether the game is finished or not
        Game will be finished when both of the players exit from the castle
        If it is finished, print the path both players traveled so far
        '''
        self.finished = []
        for player in self.players:
            self.finished.append(player.get_finished())                                    #adds the state of each player, either player finished(True) or not finished(False)

        if sum(self.finished) == 2:                                                        #Executes when both players exited the castle. If exited, list would be [True, True]
            for player in self.players:
                #player.add_to_path(player.get_position(),self.castle.exit_door)            #can be added to print player's last position
                player.print_path() 
            #for player in self.players:
            print('Final Score is '+ str(self.players[0]) + ", " + str(self.players[1]) + "! Good game!")
            return True

        return False      
    
    def update_diamonds(self) -> None:
        '''
        updates the number of diamonds the player has based on the current position of the player
        set the number of diamonds to zero after visiting the room containing diamonds
        '''
        player_id = self.get_turn()
        player = self.get_player(player_id)
        current_room_id = player.get_position()                                             #self attaches with caller player
        room= self.castle.get_room(current_room_id)
        room_diamonds = room.get_diamond()
        if room_diamonds != 0:
            current_player_diamonds = player.get_diamonds()       
            total_player_diamonds = current_player_diamonds + room_diamonds
            player.set_diamonds(total_player_diamonds)
            print("Number of Diamonds: %s, Total: %s" %(room_diamonds, player.get_diamonds()))
            diamond = Diamond(0)
            room.set_diamond(diamond)

    if __name__ == "__main__":
        print('Hello')                  #TEST CASES