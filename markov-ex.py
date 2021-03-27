"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(filepath):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(filepath)
    text = file.read()
    file.close()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'juanita'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]


    dict = {
        (word1, word2): [option1, option2, option3],
        (word2, word3): [option1]
    }
    """

    # Create an empty dictionary
    chains = {}

    # Split the string so each word is an item in a list
    words = text_string.split()

    # To set a stop point, append None to the end of our word list.

    words.append(None)

    # range over the array of words, last word excluded
    for i in range(len(words) - 2):
        # key is a tuple of current word plus the next word
        key = (words[i], words[i + 1])
        # value= a list of the word that is two words after the current word
        value = words[i + 2]

        # if the tuple key isn't already in the dictionary, 
        if key not in chains:
            # create an empty list as the key's value
            chains[key] = []

        # append the value to the key
        chains[key].append(value)

        # or we could replace the last three lines with:
        #    chains.setdefault(key, []).append(value)

    return chains
    # {('Would', 'you'): ['could', 'could', 'could', 'could', 'like', 'like'], ('you', 'could'): ['you', 'you', 'you', 'you'], ('could', 'you'): ['in', 'with', 'in', 'with'], ('you', 'in'): ['a', 'a'], ('in', 'a'): ['house?', 'box?'], ('a', 'house?'): ['Would'], ('house?', 'Would'): ['you'], ('you', 'with'): ['a', 'a'], ('with', 'a'): ['mouse?', 'fox?'], ('a', 'mouse?'): ['Would'], ('mouse?', 'Would'): ['you'], ('a', 'box?'): ['Would'], ('box?', 'Would'): ['you'], ('a', 'fox?'): ['Would'], ('fox?', 'Would'): ['you'], ('you', 'like'): ['green', 'them,'], ('like', 'green'): ['eggs'], ('green', 'eggs'): ['and'], ('eggs', 'and'): ['ham?'], ('and', 'ham?'): ['Would'], ('ham?', 'Would'): ['you'], ('like', 'them,'): ['Sam'], ('them,', 'Sam'): ['I'], ('Sam', 'I'): ['am?'], ('I', 'am?'): [None]}


def make_text(chains):
    """Return text from chains."""

    # key is a random tuple from the dictionary's keys
    key = choice(list(chains.keys())) 
    # ('you', 'in')

    words = [key[0], key[1]]
    # ['you', 'in']

    word = choice(chains[key])
    # 'a'

    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original text)
    # Note that for long texts (like a full book), this might mean
    # it would run for a very long time.

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    # return ' '.join(words)
    # return(key, words, word)
    return words


# Get the filepath from the user through a command line prompt, ex:
# python markov.py green-eggs.txt

input_path = 'data/sequence1.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
# print(random_text)
