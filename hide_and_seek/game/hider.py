import random
from game.seeker import Seeker

# TODO: Define the Hider class here

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

        message = "Find me if you can."
        if self.hider_location == self.seeker.location:
            message = "You found me!"
        elif self.hider_location 
    
   


