"""Analyse a text file and return a Markov chain from that."""
from collections import Counter

from src import chain


def create_chain_from_file(file):
    """Analyse a text file and return a Markov chain from that."""
    # Check if this file has already been used to create a chain.
    for i in chain.chains:
        if i.source == file:
            return i

    with open(file, encoding='utf8') as fp:
        words = fp.read().split()

    # Store the position of every word in the document that ends a sentence.
    # These will be used as reference to calculate how close to
    # the end of sentences each word tends to appear.
    # TODO: Breaks if last word doesn't classify as the end of a sentence.
    last_words_pos = [words.index(y, x) for x, y
                      in enumerate(words) if y.endswith(('.', '!', '?'))]

    new_chain = chain.Chain(file)
    word_pos_in_file = 0
    # Store the position of the first word of the current sentence.
    sentence_start_pos = 0

    for word in words:
        state = new_chain.find_state(word)

        # Register the next word as a possible transition to this state
        # (if it exists). Repeating words are added each time they appear
        # as to later calculate their probabilities of occuring.
        if word_pos_in_file + 1 < len(words):
            transition = new_chain.find_state(words[word_pos_in_file + 1])
            state.transitions.append(transition)

        # Delete the first element of this list if the current word
        # has passed it, Setting the next one as reference.
        if word_pos_in_file > last_words_pos[0]:
            sentence_start_pos = word_pos_in_file
            del last_words_pos[0]

        # Calculate the average position of this word in a sentence.
        # This will be done on every occurence and the resulting values
        # will be later averaged out.
        try:
            state.average_pos.append((word_pos_in_file - sentence_start_pos)
                                     / (last_words_pos[0] - sentence_start_pos)
                                     )

        except ZeroDivisionError:
            # Use 1 as the average position of this occurrence if it's
            # the only element in the sentence.
            state.average_pos.append(1)

        word_pos_in_file += 1

    for state in new_chain.states:
        # Calculate the probability of each transition happening,
        # removing repeating states in the process.
        count = Counter(state.transitions)
        temporary_transitions = {}

        for key, value in dict(count).items():
            temporary_transitions[key] = value / sum(count.values())

        state.transitions = temporary_transitions

        # Calculate the average position of this state in a sentence.
        state.average_pos = sum(state.average_pos) / len(state.average_pos)

    return new_chain
