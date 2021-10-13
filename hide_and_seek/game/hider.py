import random


class Hider:
    '''
    This class marks where the hider is and gives clues if the seeker is getting close. 

    arg:
    location of hider is established and the seekers distance is tracked in a list.

    modules:
    
    watch; keeps track of where the seeker is

    get_hint; tells the seeker if they are hot or cold. 
    '''

    def __init__(self):
        '''
        attributes of hider:
        location of hider
        list of distances seeker is from the hider
        '''

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

        if self.distance[-1] == 0:
            message = "You found me!"
        elif self.distance[-1] > self.distance[-2]:
            message = "(^.^) Getting colder."
        elif self.distance[-1] < self.distance[-2]:
            message = "(>.<) Getting warmer."

        return message
    
   


