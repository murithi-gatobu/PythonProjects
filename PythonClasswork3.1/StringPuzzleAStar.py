from queue import PriorityQueue


class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        delf.dist = 0


        if parent:
            self.start = parent.start
            self.goal = parent.goal
            self.path = parent.path[:]
            self.path.append(value)

        else:
            self.path = [value]
            self.start = start
            self.goal = goal
        
    def get_distance(self):
        pass

    def create_children(self):
        pass

class StateString(state):
    def __init__(self, value, parent, start=0, goal=0):
        super(StateString,self).__init__(value, parent,start, goal)
        self.dist = self.get_distance()

    def get_distance(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.geoal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
            

        