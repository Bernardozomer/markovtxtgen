"""Represent Markov chains as an object and store all that are created
at runtime.
"""

chains = []


class Chain:
    def __init__(self, source, states, transitions, transition_matrix):
        # Represents the source file used to create the chain.
        self.source = source
        # Represents the statespace.
        self.states = states
        # Represents all possible sequence of events.
        self.transitions = transitions
        # Represents the probability of each transition.
        self.transition_matrix = transition_matrix

        chains.append(self)
