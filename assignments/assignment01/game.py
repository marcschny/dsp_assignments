#!/usr/bin/env python3


from random import choice

class Draw():
    '''One possible draw for one player.
    '''
    
    choice_set = ('rock', 'paper', 'scissors',)
    
    def __init__(self, draw='random'):
        ''' '''        
        if draw == 'random':
            self.draw = choice(self.choice_set)
        else:
            if not draw in self.choice_set:
                raise ValueError('You have to pick among {}'.format(self.choice_set))
            self.draw = draw
            
    def __repr__(self):
        return 'Draw("{}")'.format(self.draw)
    
    def __str__(self):
        return self.draw
    
    def __lt__(self, d):
        if not type(d) == Draw:
            raise ValueError('You can only compare to objects of type "Draw".')
        if self.draw == d.draw:
            return False
        if self.draw == 'rock' and d.draw == 'paper':
            return True
        if self.draw == 'rock' and d.draw == 'scissors':
            return False
        if self.draw == 'paper' and d.draw == 'scissors':
            return True
        if self.draw == 'paper' and d.draw == 'rock':
            return False
        if self.draw == 'scissors' and d.draw == 'rock':
            return True
        if self.draw == 'scissors' and d.draw == 'paper':
            return False
            
    def __gt__(self, d):
        if not type(d) == Draw:
            raise ValueError('You can only compare to objects of type "Draw".')
        if self.draw == d.draw:
            return False
        else:
            return not self.__lt__(d)       



class Points:

    def __init__(self, h, c):
        self.human = h
        self.computer = c
        
    def max(self):
        return max((self.human, self.computer))


class Game():
    
    def __init__(self, player, max_points=3):
        ''' '''
        self.player = player
        self.max_points = max_points
        self.points = Points(0,0)
        print("\nLet's go {}!\n".format(self.player))
        
    def __repr__(self):
        ''' '''
        return 'Game({} {} : {} Computer)'.format(self.player, self.points.human, self.points.computer)
    
    def play(self):
        while self.points.max() < self.max_points:
            h = Game.draw()
            c = Draw()
            if h < c:
                self.points.computer +=1
            elif h > c:
                self.points.human += 1
            
            print('{} : {} - SCORE {}:{}'.format(h, c, self.points.human, self.points.computer))

        if self.points.human > self.points.computer:
            winner = self.player
        else:
            winner = 'Computer'
        print('\nThe winner is {}!'.format(winner))
                     
    @staticmethod
    def draw():
        ''' '''
        draw = input('Pick among "paper" (p), "scissors" (s), "rock" (r) :  ')
        draw = Game._validate_draw(draw)
        if draw is None:
            Game.draw()
        else:
            return Draw(draw)
    
    @staticmethod
    def _validate_draw(draw):
        ''' '''
        if draw in Draw.choice_set:
            return draw
        elif draw == 'p':
            return 'paper'
        elif draw == 's':
            return 'scissors'
        elif draw == 'r':
            return 'rock'
        else:
            print('\nYour pick is not valid ..')
            return None
        
        
if __name__ == '__main__':
    Game('Michael').play()
