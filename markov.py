from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    full_text = open(file_path).read()

    return full_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    # make pairs of words
    for i in range(len(words)-1):
        pair = (words[i], words[i + 1])
        # checking if pairs are in chains dictionary, if not adding them
        if chains.get(pair, 0) == 0:
            chains[pair] = []
        # adding the next word as the value to the pairs keys in chains dictionary
        if words[i + 1] != words[-1]:
            next_word = words[i + 2]
            chains[pair].append(next_word)

    #print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    first_key = choice(chains.keys())

    text = first_key[0] + " " + first_key[1]

    key_list = [first_key[0], first_key[1]]
    while True:   
        # splitting text into a list, and indexing the words in the list
        try:
            new_word = choice(chains[(key_list[0], key_list[1])])
            text = text + " " + new_word
            key_list = [key_list[1], new_word]
            # text_list = text.split()
            # current_pair = (text_list[-2], text_list[-1])

            # try to to fetch a random value for the current_pair in our dictionary and add it to text string
        # try:
        #     text = text + " " + choice(chains[current_pair])
        except IndexError:
            break
            return text
            

    return text

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

# open_and_read_file("green-eggs.txt")
