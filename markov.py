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
    poses = text_string.split(",")
    poses.append(poses)
    # To set a stop point, append None to the end of ou list.
    poses.append(None)

    return poses
    

def make_dict(pose_list):
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

        # or we could replace the last three lines with:
        # chains.setdefault(key, []).append(value)

    return chains


def make_text(chains):
    """ Create sequence options """
    
    pass
