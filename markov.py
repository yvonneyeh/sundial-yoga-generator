"""Generate Markov chains from txt files."""

from random import choice
import crud


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
    

def make_chains(poses):
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


def make_sequence(chains, session_length="long"):
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

    # Long sessions are 70 - 90 poses
    if session_length == "long" and len(poses) < 90 and len(poses) > 70:
        return poses
    # Short sessions are 35 - 45 poses
    if session_length == "short" and len(poses) < 35 and len(poses) > 45:
        return poses

    # If neither conditions are met, re-run make_sequence
    return make_sequence(chains, session_length)


def generate_sequence(filepath):
    """ Create a sequence list containing strings of pose names. """

    opened_file = open_and_read_file(filepath)
    new_list = make_list(opened_file)
    chains = make_chains(new_list)
    sequence = make_sequence(chains)

    # print(new_sequence)
    return sequence


def generate_seq_list_of_pose_objs(sequence):
    """ Create a sequence list containing pose objects. """
    
    for english_name in sequence:
        pose_obj = crud.get_pose_by_name_eng(english_name)
        seq_list.append(pose_obj)

    seq_list = []

    return seq_list

#---------------------------------------------------------------------#

a = generate_sequence('data/sequence1.txt')
# b = generate_sequence('data/sequence2.txt')

print(generate_seq_list_of_pose_objs(a))
# print(generate_seq_list_of_pose_objs(b))

# filepath = 'data/sequence1.txt'
# opened_file = open_and_read_file(filepath)
# new_list = make_list(opened_file)
# chains = make_chains(new_list)
# new_sequence = make_sequence(chains)
# print(new_sequence)
