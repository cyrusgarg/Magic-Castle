import random
from diamond import Diamond
FIRST_ROOM_ID = 1
LAST_ROOM_ID = 25 
BLOCKED_DOOR = 0

class Room:

    def __init__(self, ID = None, north = None, south = None, east = None, west = None, portal: bool = False, wormhole: bool = False, diamond:Diamond = None):
        '''
    Initialize the class Room
    '''
        self.id = ID
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.portal = portal
        self.wormhole = wormhole
        if diamond == None:
            self.diamond = 0
        else:
            self.diamond = diamond.get_diamonds()
 
    def get_id(self):
        '''
        returns the ID of the room
        '''
        return self.id
    
    def set_id(self,ID:int):
        '''
        sets the ID of the room
        '''
        if not isinstance(ID,int):                  #raises exception if ID is not int type
            raise Exception("ID is not int type")
        
        self.id = ID
    
    def generate_random_room_id(self) -> int:
        '''
        Generate random room ID when there is a wormhole inside the room
        '''
        if not self.wormhole:
            raise Exception("Method is called on a room which does not has wormhole")

        valid = False
        while not valid:
            random_id = random.randint(FIRST_ROOM_ID,LAST_ROOM_ID)
            if random_id != self.get_id():
                valid = True

        return random_id

    def get_portal(self) -> bool:
        '''
        returns the portal status
        '''
        return self.portal
    
    def set_portal(self,portal:bool) -> None:
        '''
        sets the room with portal bool value
        '''
        if self.get_wormhole() or self.get_diamond():
            raise Exception('Room can be only in 1 state.')
        if self.isthere_entrance_exit_door():
            raise Exception("Exit or Entrance room cannot have portal.")
        self.portal = portal
    
    def get_wormhole(self) -> bool:
        '''
        returns the wormhole status
        '''
        return self.wormhole
    
    def set_wormhole(self,wormhole:bool) -> None:
        '''
        sets the room with wormhole bool value
        '''
        if self.get_portal() or self.get_diamond():
            raise Exception('Room can only be in 1 state.')
        if self.isthere_entrance_exit_door():
            raise Exception("Exit or Entrance room cannot have wormhole.")
        self.wormhole = wormhole

    def get_diamond(self) -> bool:
        '''
        returns the number of diamonds in the room
        '''
        return self.diamond
    
    def set_diamond(self,diamond:Diamond) -> None:
        '''
        sets the number of diamonds
        '''
        if self.get_portal() or self.get_wormhole():
            raise Exception('Room can only be in 1 state.')
        
        self.diamond= diamond.get_diamonds()

    def get_door(self,direction:str) -> int:
        '''
        returns the next door ID 
        '''
        input_direction = ["NORTH",'SOUTH','EAST','WEST']
        output_door_ID = [self.north,self.south,self.east,self.west]

        if direction.upper() not in input_direction:
            raise Exception("Input direction is not a valid direction")
        
        next_door_id = output_door_ID[input_direction.index(direction.upper())]
        
        return next_door_id
    
    def set_link(self,direction: str,val) -> None:
        '''
        sets the door link according to the direction
        '''
        input_direction = ["NORTH",'SOUTH','EAST','WEST']
        valid_values = [None,"entrance","exit"]

        if direction.upper() not in input_direction:                    #raise exception if given direction is not a valid
            raise Exception("Input direction is not a valid direction")
        
        if isinstance(val,int):                         #raises Exception if val is not a valid entry
            if val < BLOCKED_DOOR or val > LAST_ROOM_ID:
                raise Exception("Not a valid room ID")
        else:
            if val not in valid_values:
                raise Exception("Not a valid value")
        
        if direction.upper() == "NORTH":
            self.north = val
        elif direction.upper() == "SOUTH":
            self.south = val
        elif direction.upper() == "EAST":
            self.east = val
        elif direction.upper() == "WEST":
            self.west = val

    def isthere_entrance_exit_door(self) -> bool:
        '''
        check whether there is an entrance or exit door in the room
        '''
        exist = False
        output_door_value = [self.north,self.south,self.east,self.west] # in list, each element contains the value as each element is referenced to immutable types like str, float, integer
        
        if 'entrance' in output_door_value:
            exist = True
            return exist
        elif 'exit' in output_door_value:
            exist = True
            return exist
        else:
            return exist
        
if __name__ == "__main__":
    print('Hello')
    room = Room(1,1,0,1,1,True,False,3)
    room.get_id
    room.set_id(2)
    #room.generate_random_room_id()
    room.get_portal()
    room.set_portal(False)
    room.set_diamond(3)
    room.get_diamond()
    room.set_wormhole(True)
    room.get_wormhole()    
    room.generate_random_room_id() 
    room.get_door("east")  
    room.set_link("east",2)
    room.get_door("east")
    room.isthere_entrance_exit_door()    