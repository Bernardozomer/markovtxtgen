"""Generate a new sentence using a chain."""

import random

import numpy as np


def create_sentence(chain, length, sensitivity=0, starting_word=None):
    """Generate a new sentence using a chain."""
    if not starting_word:
        # Randomly choose the starting word among every one
        # whose state has an average position close enough
        # to the start of a sentence.
        possible_starts = [i for i in sorted(chain.states,
                                             key=lambda x: x.average_pos)
                           if i.average_pos <= 1 - sensitivity]

        if not possible_starts:
            possible_starts = chain.states

        current_state = random.choice(possible_starts)
    else:
        current_state = chain.find_state(starting_word)

    # Store the sequence of words taken.
    states = [current_state]
    # The count starts at 0, but the starting word
    # has already been chosen.
    current_pos = 1

    while current_pos <= length - 1:
        # End sentence early if the current word
        # never precedes another one in the source file.
        if not current_state.transitions:
            break

        relative_pos = current_pos / (length - 1)

        # Get every state whose average position is enough within range
        # of the current relative position.
        transitions = {key: val for key, val
                       in current_state.transitions.items()
                       if relative_pos - sensitivity <= key.average_pos
                       <= relative_pos + sensitivity}

        if not transitions:
            transitions = current_state.transitions

        # Get next word.
        transitions = {k: v / total for total in (sum(transitions.values()),)
                       for k, v in transitions.items()}
        transition = np.random.choice(list(transitions.keys()), replace=True,
                                      p=list(transitions.values()))

        current_state = transition
        states.append(current_state)
        current_pos += 1

    return ' '.join(i.content for i in states)
