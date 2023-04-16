FIRST_ROOM_ID = 1
LAST_ROOM_ID = 25 
BLOCKED_DOOR = 0
from room import Room

class Castle:
    def __init__(self):
        '''
        initialize the castle class
        '''
        self.castle = {}
        self.entrance_id = None
        self.entrance_door = None
        self.exit_id = None
        self.exit_door = None
            
    
    def add_room(self,room) -> None:
        '''
        add the room with ID in the castle
        '''
        room = int(room)
        if room in self.castle:
            raise Exception("Room ID already exists")
        self.castle[room]=Room()

    def get_room(self,id) -> object:
        '''
        returns the room object against room ID provided
        '''
        if int(id) not in self.castle:
            raise Exception("Room does not exist")
        
        return self.castle[int(id)]
    
    def change_room(self,id,new_room) -> None:
        '''
        change_room from initial "id" to "new_room"
        '''
        if id < BLOCKED_DOOR or id > LAST_ROOM_ID or new_room < BLOCKED_DOOR or new_room > LAST_ROOM_ID:
            raise Exception("ID is out of range")
        
        room = self.castle.pop(id)         #remove room's older id from castle and return the value as it is stored as key:value pair where key is room_ID and value is room object
        room.set_id(new_room)
        self.castle[new_room] = room       #adds back the room with new ID
            
    def get_entrance_id(self) -> list:
        '''
        return the ID of the room with the entrance door
        '''
        return self.entrance_id

    def set_entrance_id_door_number(self,id,door) -> None:
        '''
        sets the entrance id and door number
        '''
        self.entrance_id = int(id)
        self.entrance_door = door

    def get_exit_id(self) -> list:
        '''
        return the ID of the room with the exit door
        '''
        return self.exit_id
    
    def set_exit_id_door_number(self,id,door) -> None:
        '''
        sets the exit id and door number
        '''
        self.exit_id = int(id)
        self.exit_door = door

    def get_next_room(self,room_id,door):
        '''
        receives a Room ID and a door, and outputs another Room ID which 
        is the room behind the door that is selected or a random room ID
        which is generated when entering the room with a wormhole. If the room
        behind the door has a portal inside this function should return the id 
        of the room with the entrance door.  For the cases where the chosen door 
        is “entrance” or “exit”, this function should return “entrance” or “exit”
        '''
        old_room = self.castle[room_id]
        new_room_id = old_room.get_door(door)

        if new_room_id == 'entrance':
            return 'entrance'
        if new_room_id == 'exit':
            return 'exit'
        if new_room_id == BLOCKED_DOOR:                     #execute if room is blocked
            return BLOCKED_DOOR
        
        if self.castle[new_room_id].get_wormhole():         #execute when new_room_id has wormhole
            print("Wormhole Devoured you")
            valid = False
            
            while not valid:
                new_room_id = self.castle[new_room_id].generate_random_room_id()
                if self.castle[new_room_id].get_wormhole() == False: 
                    valid = True
                    
            if self.castle[new_room_id].get_portal():      #execute when new room id generated has portal
                print("Wormhole room returned the portal room which takes to entrance")
                return self.get_entrance_id() 
            
            return new_room_id
        
        if self.castle[new_room_id].get_portal():           #executes when new_room_id has portal
            print("You entered a portal")
            return self.get_entrance_id()
        
        return new_room_id                                  #execute when room behind the door does not has wormhole, portal,is not entrance, and is not exit as well as not blocked 
        
if __name__=="__main__":
    print("hello")                  #TEST CASES
    castle = Castle()
    castle.add_room(1)    
    print(castle.castle)
    castle.change_room(1,5)
    print(castle.castle)
    room =castle.get_room(5)
    room.set_link("north",'entrance')
    room.set_link("south",6)
    castle.add_room(6)
    room_6 = castle.get_room(6)
    room_6.set_wormhole(True)
    castle.get_next_room(5,'north')