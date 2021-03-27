"""Generate Markov chains from txt files."""

from random import choice


def open_and_read_file(filepath):
    """Take file path as string; return text as string.
    """

    file = open(filepath)
    text = file.read()
    file.close()

    return text


def make_list(text):
    """ Take the string of text, return a list of poses.
    
    First split the text to create a list of poses. 
    
    [cat, cow, downward dog, tree, etc ]
    
    """
    poses = text.split(",\n")
    # poses.append(poses)
    # To set a stop point, append None to the end of ou list.
    poses.append(None)

    return poses
    

def make_dict(poses):
    """Take in list of poses, return dictionary of pose tuples and options of poses that follow them.
    
    Each key will be a tuple of two consecutive poses. 
    
    The value of a each will be a list containing every pose that follows the second tuple item.  
    
    pose_dict = {
        (pose1, pose2): [option1, option2, option3],
        (pose2, pose3): [option1]
    }
    """
    chains = {}

    # range over the array of poses, last pose excluded
    for i in range(len(poses) - 2):
        # key is a tuple of current pose plus the next pose
        key = (poses[i], poses[i + 1])
        # value = a list of the pose that is two poses after the current pose
        value = poses[i + 2]

        # if the tuple key isn't already in the dictionary, 
        if key not in chains:
            # create an empty list as the key's value
            chains[key] = []

        # append the value to the key
        chains[key].append(value)

    return chains


def make_sequence(chains):
    """Return randomly generated sequence from chains."""

    # key is a random tuple from the dictionary's keys
    key = choice(list(chains.keys())) 

    poses = [key[0], key[1]]

    pose = choice(chains[key])

    # Keep looping until we reach a value of None
    # (which would mean it was the end of our original sequence)
    # Note that for long sequences, this might mean
    # it would run for a very long time.

    while pose is not None:
        key = (key[1], pose)
        poses.append(pose)
        pose = choice(chains[key])

    return poses


#---------------------------------------------------------------------#

# opened_file = open_and_read_file(s1)
# new_list = make_list(opened_file)
# chains = make_dict(new_list)
# print(make_sequence(chains))

# print(make_dict(make_list(open_and_read_file(s1))))


# Get the filepath from the user through a command line prompt, ex:
s1 = 'data/sequence1.txt'

# Open the file and turn it into one long string
input_text1 = open_and_read_file(input_path)

# Get a Markov chain
chains1 = make_chains(input_text1)

# Produce random text
random_sequence = make_text(chains1)

print(random_sequence)