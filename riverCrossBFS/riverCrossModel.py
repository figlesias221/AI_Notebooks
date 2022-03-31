from riverCrossEnv import RiverCrossEnv
from riverCrossUtils import win

class RiverCrossModel(RiverCrossEnv):

    def actions(self):
        for d in range(2):
            for p in range(4):
                yield {'direction': d, 'passenger': p}
        
    def set_state(self, state):
        self.state = state
        
    def next_state(self, action):
        state = self.state.copy()
        next_state, _, _, _ = self.step(action)
        self.state = state
        return next_state

    def BFS(self):
        state = self.reset()
        root = frozenset(state.items())
        to_visit = [root]
        reached = set()
        prev_node = dict()
        while to_visit != []:
            node = to_visit.pop(0)
            reached.add(node)
            state = dict(node)
            if win(state):
                return node, prev_node
            self.set_state(state)
            for a in self.actions():
                next_state = self.next_state(a)
                child = frozenset(next_state.items())
                if not (child in to_visit or child in reached):
                    to_visit.append(child) 
                    prev_node[child] = (node, frozenset(a))


















