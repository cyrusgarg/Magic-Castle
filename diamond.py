class Diamond:
    def __init__(self,Diamonds:int = 1):
        if Diamonds < 0 :
            raise Exception("Number of diamonds cannot be negative")
        
        self.diamonds = Diamonds
    
    def get_diamonds(self):
        '''
        return the number of diamonds
        '''
        return self.diamonds
    def set_diamonds(self,Diamonds:int):
        '''
        sets the number of diamonds
        '''
        self.diamonds = Diamonds
        
    def __str__(self):
        '''
        returns the string representation of the diamonds
        '''
        string = 'Number of Diamonds:'+ str(self.get_diamonds())
        
        return string
    
if __name__ == '__main__':
    diamond = Diamond(1)
    print(diamond)