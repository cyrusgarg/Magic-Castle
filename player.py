FIRST_ROOM_ID = 1
LAST_ROOM_ID = 25 
BLOCKED_DOOR = 0
from castle import Castle

class Player:

    def __init__(self,player_id):
        '''
        initialize the player object with below mentioned attributes
        '''
        self.player_id = player_id
        self.path = []
        self.player_diamonds = 0
        self.player_current_position = None
        self.finish = False

    def __str__(self) ->str:
        '''
        str representation of current position of the player and the total number of diamonds the player has gathered so far.
        '''
        line = 'Player ' + str(self.get_player_id()+1) + ". " + "Diamond count: "+ str(self.get_diamonds())
        return line
    
    def get_position(self):
        '''
        returns the current position (room ID) of the player 
        '''
        return self.player_current_position
    
    def set_position(self,id):
        '''
        sets the current position (room ID) of the player
        '''
        if id < BLOCKED_DOOR or id > LAST_ROOM_ID:
            raise Exception('Room ID is out of the range')
        
        self.player_current_position = id

    def get_player_id(self) -> int:
        '''
        returns the ID of the player
        '''
        return self.player_id
    
    def get_diamonds(self) -> int:
        '''
        returns the number of diamonds the player has
        '''

        return self.player_diamonds
    
    def set_diamonds(self,count) ->None:
        ''''
        sets the number of diamonds the player should have
        '''
        self.player_diamonds= count

    def print_path(self) -> None:
        '''
        prints the player path traveled so far
        '''
        symbol = " -> "
        comma_symbol = ", "
        i= 0
        path = ""

        for item in self.path:
            path +=str(item)
            i +=1
            if i%2 == 0 and i != len(self.path):
                path += comma_symbol
            elif i != len(self.path):
                path += symbol

        print(path)

    def add_to_path(self,room_id,door_id) -> None:
        '''
        add the current decision (North... West) and the Room ID corresponding to the player decision
        '''
        self.path.append(room_id)
        self.path.append(door_id.lower())

    def move(self,room_id) -> None:
        '''
        receives one of the room’s IDs and changes the position of the player
        ''' 
        self.player_current_position = room_id

    def get_finished(self):
        '''
        return boolean value if player successfully exited
        '''
        return self.finish
    
    def set_finished(self):
        '''
        sets True boolean value if player successfully exited
        '''
        self.finish = True
        
if __name__ == "__main__":
    print("Hello")              #Test Cases
    player = Player(0)
    print(str(player))
    player.set_position(5)
    print(str(player))
    player.get_player_id()
    player.get_diamonds()
    player.set_diamonds(3)
    print(str(player))
    player.add_to_path(5,"North")
    player.print_path()    
    player.add_to_path(5,"North")
    player.print_path()
    player.move(6)
    print(player.get_position())
    player.print_path()
    player.clear_path()
    player.print_path()    