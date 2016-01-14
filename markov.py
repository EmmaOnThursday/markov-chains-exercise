from random import choice
import sys


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


    # # make pairs of words
    # for i in range(len(words)-1):
    #     ngram = (words[i], words[i + 1])
    #     # checking if pairs are in chains dictionary, if not adding them
    #     if chains.get(ngram, 0) == 0:
    #         chains[ngram] = []
    #     # adding the next word as the value to the pairs keys in chains dictionary
    #     if words[i + 1] != words[-1]:
    #         next_word = words[i + 2]
    #         chains[ngram].append(next_word)

    for i in range(len(words)-n):
        ngram_list = words[i:i+n]
        ngram = tuple(item for item in ngram_list)
        if chains.get(ngram, 0) == 0:
                chains[ngram] = []
        if words[i + n] != words[-1]:
                next_word = words[i + n]
                chains[ngram].append(next_word)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    # ,makes a list of keys from dictionary(tuple) that starts with a capital letter
    capital_keys = [key for key in chains.keys() if key[0].isupper()]

    # grabs a random key from the list of capital_keys
    # adds two initial tuple words to text string
    # creates list containing two initial words from tuple; limits to 127 characters for twitter
    first_key = choice(capital_keys)

    text = " ".join(first_key)

    key_list = [item for item in first_key]
    while True:   
      
        # tries to grab a new word from the values associated with initial tuple/key
        # adds new word to text string
        # rebuilds key_list with new word in second position
        try:
            new_word = choice(chains[tuple(item for item in key_list)])
            text = text + " " + new_word
            key_list.append(new_word)
            key_list = key_list[1:]
            # print key_list
            
        # when choice selects "I am?", receives IndexError and quits loop
        except IndexError:
            print "IndexError"
            break
        except KeyError:
            print "KeyError"
            break

    return text

input_path = sys.argv[1]
n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

# open_and_read_file("green-eggs.txt")
