"""Take a text file and create a Markov chain from that."""

from collections import Counter

from .chain import Chain, chains


def create_chain_from_file(file):
    """Take a text file and return a Markov chain from that."""
    # Check if this file has already been used to create a chain.
    for chain in chains:
        if chain.source == file:
            return chain

    with open(file, encoding='utf8') as fp:
        text = fp.read()

    words = text.split()
    word_position_in_file = 1
    states = []
    transitions = []
    transition_matrix = []

    for word in words:
        # Register the word as a possible state if that hasn't been done.
        if word not in states:
            states.append(word)
            transitions.append([])
            transition_matrix.append([])

        index = states.index(word)

        # Register the next word as a possible transition to this state
        # if it exists. Repeating words are added each time they appear
        # as to later calculate their chance of appearing after this one.
        if word_position_in_file < len(words):
            transitions[index].append(words[word_position_in_file])

        word_position_in_file += 1

    for state in states:
        # Calculate the possibility of each transition.
        index = states.index(state)
        count = Counter(transitions[index])
        total = sum(count.values())

        for value in count.values():
            transition_matrix[index].append(value / total)

        # Update the list of transitions associated with this state
        # as to remove repeating words.
        transitions[index] = list(count)

    new_chain = Chain(file, states, transitions, transition_matrix)
    return new_chain
