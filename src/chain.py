"""Represent Markov chains as an object and store all that are created
at runtime.
"""

chains = []


class Chain:
    """Represent Markov chains as an object."""

    def __init__(self, source, states=None):
        # Store the file used to create the chain.
        self.source = source

        # Represent the statespace.
        if not states:
            states = []
        self.states = states

        chains.append(self)

    def find_state(self, word):
        """Create a new state that contains the given word
        if it doesn't already exist.
        """

        for i in self.states:
            if i.content == word:
                return i

        new_state = State(word)
        self.states.append(new_state)
        return new_state


class State:
    """Represent a state in a Markov chain."""

    def __init__(self, content, transitions=None, average_pos=None):
        self.content = content

        # Store all states possible to occur immediately after
        # this one and the probability of that happening.
        # Starts out containing every repeating occurence before
        # the probability of each one is calculated.
        if not transitions:
            transitions = []
        self.transitions = transitions

        # Store how likely it is for the word this state represents
        # to show up at the end of a sentence. Starts out containing
        # one value per occurence before being averaged out.
        if not average_pos:
            average_pos = []
        self.average_pos = average_pos
