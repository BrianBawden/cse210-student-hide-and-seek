import random
from game.seeker import Seeker


class Hider:

    def __init(self):

        self.location = random.randint(1,1000)
        self.distance = [0, 0]

    
    def watch(self, location):
        '''
        This module keeps track of the seekers location so the program can calculate the distance from the hider. 
        '''
        distance = abs(self.location - location)

        self.distance.append(distance)

    def get_hint(self):
        '''
        This module will return the appropriate message to the user letting them know if they are getting closer or farther from the hider. 
        '''

        message = "Find me if you can."

        if self.location == self.distance[-1]:
            message = "You found me!"
        elif self.distance[-1] > self.distance[-2]:
            message = "(^.^) Getting colder."
        elif self.distance[-1] < self.distance[-2]:
            messsage = "(>.<) Getting warmer."

        return message
    
   


