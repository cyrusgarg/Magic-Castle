from game import Game
def main():

    game = Game()
    
    try:
        game.initialize_from_file('castle.txt')     #initialize the game, insert rooms into castle with each door setup, each player at entrance
        turn = 0
    except Exception  as e:
        print(e.args[0])

    while not game.is_finished():                   #check if each player exited the castle
        try:
            game.set_turn(turn%2)                   #sets the turn with player id, loops back if the turn counter goes above 1(player_id) with the help of %(mod)
            game.move()                             #calls the move method defined in game class, generally it moves the player
            turn += 1                               #counter for the turn
        except Exception  as e:
            print(e.args[0])                        #prints the exception error

if __name__ =="__main__":
    main()
    
'''  
    TEST CASES

    
    '''