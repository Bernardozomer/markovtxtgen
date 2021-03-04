"""Generate a new sentence using a chain."""

import numpy as np
import random


def create_sentence(chain, length, starting_word=None):
    """Generate a new sentence using a chain."""
    if not starting_word:
        # If not specified, the starting word is randomly chosen from
        # the entire pool, which isn't optimal because
        # some words are more likely to start sentences than others.
        current_word = random.choice(chain.states)
    else:
        current_word = starting_word

    # Store the sequence of words taken.
    word_list = [current_word]
    prob = 1
    i = 1

    while i <= length:
        state_index = chain.states.index(current_word)

        # End sentence early if the current word never precedes another one
        # in the text file.
        if not chain.transitions[state_index]:
            break

        # Get the next word.
        transition = np.random.choice(chain.transitions[state_index],
                                      replace=True,
                                      p=chain.transition_matrix[state_index])
        transition_index = chain.transitions[state_index].index(transition)
        current_word = transition
        word_list.append(current_word)

        prob = prob * chain.transition_matrix[state_index][transition_index]
        i += 1

    print('Sentence generated:\n' + ' '.join(i for i in word_list), sep=' ')
    print('\nProbability of this possible sequence of states: ' + str(prob)
          + '\n')
