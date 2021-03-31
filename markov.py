"""Generate Markov chains from txt files."""

from random import choice
from crud import get_pose_by_name_eng


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
    poses = text.split("\n")
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

def add_to_all_chains_dict(chains_dict, all_chains_dict):
    """Takes in a chains dictionary and adds items to all_chains_dict."""

    for key, value_list in chains_dict.items():
        if key not in all_chains_dict.keys():
            all_chains_dict[key] = value_list
        if key in all_chains_dict.keys():
            for value in value_list:
                if value not in all_chains_dict[key]:
                    all_chains_dict[key].append(value)



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


def make_default_sequence(filepath):
    """ Create a sequence list for default sequences. """

    opened_file = open_and_read_file(filepath)
    sequence = make_list(opened_file)

    # print(new_sequence)
    return sequence


def generate_random_sequence(filepath):
    """ Create a sequence list containing strings of pose names. """

    opened_file = open_and_read_file(filepath)
    new_list = make_list(opened_file)
    chains = make_chains(new_list)
    sequence = make_sequence(chains)

    # print(new_sequence)
    return sequence


def generate_list_of_pose_objs(sequence):
    """ Create a sequence list containing pose objects. """

    seq_list = []
    for english_name in sequence:
        pose_obj = get_pose_by_name_eng(english_name)
        seq_list.append(pose_obj)

    return seq_list

dict_1 = {("Child's Pose", 'Downward-Facing Dog'): ['Ragdoll', 'Forward Fold', 'Table Top'], ('Downward-Facing Dog', 'Ragdoll'): ['Standing at Attention'], ('Ragdoll', 'Standing at Attention'): ['Mountain Pose', None], ('Standing at Attention', 'Mountain Pose'): ['Forward Fold'], ('Mountain Pose', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift', 'Halfway Lift'], ('Forward Fold', 'Halfway Lift'): ['High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank'], ('Halfway Lift', 'High-to-Low Plank'): ['Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog'], ('High-to-Low Plank', 'Upward-Facing Dog'): ['Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog'], ('Upward-Facing Dog', 'Downward-Facing Dog'): ['Mountain Pose', 'Mountain Pose', 'Chair', 'Warrior 2', 'Chair', 'Warrior 2', 'Chair', 'Warrior 2', 'Crescent Lunge'], ('Downward-Facing Dog', 'Mountain Pose'): ['Forward Fold', 'Forward Fold'], ('Downward-Facing Dog', 'Chair'): ['Forward Fold', 'Forward Fold', 'Forward Fold'], ('Chair', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift', 'Halfway Lift'], ('Downward-Facing Dog', 'Warrior 2'): ['Extended Side Angle', 'Extended Side Angle',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'Extended Side Angle'], ('Warrior 2', 'Extended Side Angle'): ['Reverse Warrior', 'Reverse Warrior', 'Reverse Warrior'], ('Extended Side Angle', 'Reverse Warrior'): ['High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank'], ('Reverse Warrior', 'High-to-Low Plank'): ['Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog'], ('Downward-Facing Dog', 'Crescent Lunge'): ['Revolved Crescent'], ('Crescent Lunge', 'Revolved Crescent'): ["Runner's Lunge"], ('Revolved Crescent', "Runner's Lunge"): ['Side Plank'], ("Runner's Lunge", 'Side Plank'): ['Prayer Twist'], ('Side Plank', 'Prayer Twist'): ['Gorilla'], ('Prayer Twist', 'Gorilla'): ['Crow'], ('Gorilla', 'Crow'): ['Eagle'], ('Crow', 'Eagle'): ['Dancer'], ('Eagle', 'Dancer'): ['Tree'], ('Dancer', 'Tree'): ['Warrior 1'], ('Tree', 'Warrior 1'): ['Warrior 2'], ('Warrior 1', 'Warrior 2'): ['Triangle'], ('Warrior 2', 'Triangle'): ['Wide Leg Forward Fold'], ('Triangle', 'Wide Leg Forward Fold'): ['Half Pigeon'], ('Wide Leg Forward Fold', 'Half Pigeon'): ['Cobra'], ('Half Pigeon', 'Cobra'): ['Bow', 'Savasana'], ('Cobra', 'Bow'): ['Camel'], ('Bow', 'Camel'): ['Bridge'], ('Camel', 'Bridge'): ['Reclined Bound Angle'], ('Bridge', 'Reclined Bound Angle'): ['Seated Forward Fold'], ('Reclined Bound Angle', 'Seated Forward Fold'): ['Happy Baby'], ('Seated Forward Fold', 'Happy Baby'): ['Supine Twist'], ('Happy Baby', 'Supine Twist'): ['Savasana'], ('Supine Twist', 'Savasana'): [None]}
{("Child's Pose", 'Downward-Facing Dog'): ['Ragdoll'], ('Downward-Facing Dog', 'Ragdoll'): ['Standing at Attention'], ('Ragdoll', 'Standing at Attention'): ['Mountain Pose', None], ('Standing at Attention', 'Mountain Pose'): ['Forward Fold'], ('Mountain Pose', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift', 'Halfway Lift'], ('Forward Fold', 'Halfway Lift'): ['High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank'], ('Halfway Lift', 'High-to-Low Plank'): ['Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog'], ('High-to-Low Plank', 'Upward-Facing Dog'): ['Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog'], ('Upward-Facing Dog', 'Downward-Facing Dog'): ['Mountain Pose', 'Mountain Pose', 'Chair', 'Warrior 2', 'Chair', 'Warrior 2', 'Chair', 'Warrior 2', 'Crescent Lunge'], ('Downward-Facing Dog', 'Mountain Pose'): ['Forward Fold', 'Forward Fold'], ('Downward-Facing Dog', 'Chair'): ['Forward Fold', 'Forward Fold', 'Forward Fold'], ('Chair', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift', 'Halfway Lift'], ('Downward-Facing Dog', 'Warrior 2'): ['Extended Side Angle', 'Extended Side Angle', 'Extended Side Angle'], ('Warrior 2', 'Extended Side Angle'): ['Reverse Warrior', 'Reverse Warrior',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'Reverse Warrior'], ('Extended Side Angle', 'Reverse Warrior'): ['High-to-Low Plank', 'High-to-Low Plank'], ('Reverse Warrior', 'High-to-Low Plank'): ['Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog'], ('Downward-Facing Dog', 'Crescent Lunge'): ['Revolved Crescent'], ('Crescent Lunge', 'Revolved Crescent'): ["Runner's Lunge"], ('Revolved Crescent', "Runner's Lunge"): ['Side Plank'], ("Runner's Lunge", 'Side Plank'): ['Prayer Twist'], ('Side Plank', 'Prayer Twist'): ['Gorilla'], ('Prayer Twist', 'Gorilla'): ['Crow'], ('Gorilla', 'Crow'): ['Eagle'], ('Crow', 'Eagle'): ['Dancer'], ('Eagle', 'Dancer'): ['Tree'], ('Dancer', 'Tree'): ['Warrior 1'], ('Tree', 'Warrior 1'): ['Warrior 2'], ('Warrior 1', 'Warrior 2'): ['Triangle'], ('Warrior 2', 'Triangle'): ['Wide Leg Forward Fold'], ('Triangle', 'Wide Leg Forward Fold'): ['Half Pigeon'], ('Wide Leg Forward Fold', 'Half Pigeon'): ['Cobra'], ('Half Pigeon', 'Cobra'): ['Bow'], ('Cobra', 'Bow'): ['Camel'], ('Bow', 'Camel'): ['Bridge'], ('Camel', 'Bridge'): ['Reclined Bound Angle'], ('Bridge', 'Reclined Bound Angle'): ['Seated Forward Fold'], ('Reclined Bound Angle', 'Seated Forward Fold'): ['Happy Baby', 'Savasana', 'Savasana''Savasana'], ('Seated Forward Fold', 'Happy Baby'): ['Supine Twist', 'Savasana', 'Savasana', 'Savasana'], ('Happy Baby', 'Supine Twist'): ['Savasana', 'Savasana', 'Savasana', 'Savasana', 'Savasana'], ('Happy Baby', 'Savasana'): [None], ('Seated Forward Fold', 'Savasana'): [None], ('Bridge', 'Savasana'): [None]}


dict_2 = {("Child's Pose", 'Table Top'): ['Cow'], ('Downward-Facing Dog', 'Table Top'): ['Cat'], ('Table Top', 'Cow'): ['Cat'], ('Cow', 'Cat'): ['Cow', 'Thread the Needle'], ('Cat', 'Cow'): ['Cat'], ('Cat', 'Thread the Needle'): ['Downward-Facing Dog'], ('Thread the Needle', 'Downward-Facing Dog'): ['Standing at Attention'], ('Downward-Facing Dog', 'Standing at Attention'): ['Mountain Pose', None], ('Standing at Attention', 'Mountain Pose'): ['Side Body Stretch'], ('Mountain Pose', 'Side Body Stretch'): ['Baby Back Bend', 'Baby Back Bend'], ('Side Body Stretch', 'Baby Back Bend'): ['Mountain Pose', 'Mountain Pose'], ('Baby Back Bend', 'Mountain Pose'): ['Forward Fold', 'Forward Fold'], ('Mountain Pose', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift'], ('Forward Fold', 'Halfway Lift'): ['High-to-Low Plank', 'High-to-Low Plank'], ('Halfway Lift', 'High-to-Low Plank'): ['Upward-Facing Dog', 'Upward-Facing Dog'], ('High-to-Low Plank', 'Upward-Facing Dog'): ['Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog'], ('Upward-Facing Dog', 'Downward-Facing Dog'): ['Mountain Pose', 'Chair', 'Low Lunge', 'Chair Pose', 'Star'], ('Downward-Facing Dog', 'Mountain Pose'): ['Side Body Stretch'], ('Downward-Facing Dog', 'Chair'): ['Airplane Arms'], ('Chair', 'Airplane Arms'): ['Crescent Lunge'], ('Airplane Arms', 'Crescent Lunge'): ['Open Twist', 'Open Twist', 'Open Twist'], ('Crescent Lunge', 'Open Twist'): ['Crescent Lunge'], ('Open Twist', 'Crescent Lunge'): ['Warrior 2'],
          ('Crescent Lunge', 'Warrior 2'): ['Extended Side Angle', 'Extended Side Angle', 'Extended Side Angle'], ('Warrior 2', 'Extended Side Angle'): ['Reverse Warrior', 'Reverse Warrior', 'Reverse Warrior'], ('Extended Side Angle', 'Reverse Warrior'): ['Chair', 'Chair', 'High-to-Low Plank'], ('Reverse Warrior', 'Chair'): ['Airplane Arms', 'Airplane Arms'], ('Reverse Warrior', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Low Lunge'): ['Warrior 1'], ('Low Lunge', 'Warrior 1'): ['Humble Warrior'], ('Warrior 1', 'Humble Warrior'): ['Pyramid'], ('Humble Warrior', 'Pyramid'): ['Revolved Triangle'], ('Pyramid', 'Revolved Triangle'): ['High-to-Low Plank'], ('Revolved Triangle', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Chair Pose'): ['Prayer Twist'], ('Chair Pose', 'Prayer Twist'): ['High-to-Low Plank'], ('Prayer Twist', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Star'): ['Horse'], ('Star', 'Horse'): ['Star'], ('Horse', 'Star'): ['Wide Leg Forward Fold'], ('Star', 'Wide Leg Forward Fold'): ['Low Lunge'], ('Wide Leg Forward Fold', 'Low Lunge'): ['Fallen Triangle'], ('Low Lunge', 'Fallen Triangle'): ['Half Pigeon'], ('Fallen Triangle', 'Half Pigeon'): ['Cobra'], ('Half Pigeon', 'Cobra'): ['Seated Forward Fold'], ('Cobra', 'Seated Forward Fold'): ['Happy Baby'], ('Seated Forward Fold', 'Happy Baby'): ['Supine Figure 4'], ('Happy Baby', 'Supine Figure 4'): ['Savasana'], ('Supine Figure 4', 'Savasana'): [None]}
{("Child's Pose", 'Table Top'): ['Cow'], ('Table Top', 'Cow'): ['Cat'], ('Cow', 'Cat'): ['Cow', 'Thread the Needle'], ('Cat', 'Cow'): ['Cat'], ('Cat', 'Thread the Needle'): ['Downward-Facing Dog'], ('Thread the Needle', 'Downward-Facing Dog'): ['Standing at Attention'], ('Downward-Facing Dog', 'Standing at Attention'): ['Mountain Pose', None], ('Standing at Attention', 'Mountain Pose'): ['Side Body Stretch'], ('Mountain Pose', 'Side Body Stretch'): ['Baby Back Bend', 'Baby Back Bend'], ('Side Body Stretch', 'Baby Back Bend'): ['Mountain Pose', 'Mountain Pose'], ('Baby Back Bend', 'Mountain Pose'): ['Forward Fold', 'Forward Fold'], ('Mountain Pose', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift'], ('Forward Fold', 'Halfway Lift'): ['High-to-Low Plank', 'High-to-Low Plank'], ('Halfway Lift', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('High-to-Low Plank', 'Upward-Facing Dog'): ['Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog'], ('Upward-Facing Dog', 'Downward-Facing Dog'): ['Mountain Pose', 'Chair', 'Low Lunge', 'Chair Pose', 'Star'], ('Downward-Facing Dog', 'Mountain Pose'): ['Side Body Stretch'], ('Downward-Facing Dog', 'Chair'): ['Airplane Arms'], ('Chair', 'Airplane Arms'): ['Crescent Lunge'], ('Airplane Arms', 'Crescent Lunge'): ['Open Twist'], ('Crescent Lunge', 'Open Twist'): ['Crescent Lunge'], ('Open Twist', 'Crescent Lunge'): [
    'Warrior 2'], ('Crescent Lunge', 'Warrior 2'): ['Extended Side Angle'], ('Warrior 2', 'Extended Side Angle'): ['Reverse Warrior'], ('Extended Side Angle', 'Reverse Warrior'): ['Chair', 'Chair', 'High-to-Low Plank'], ('Reverse Warrior', 'Chair'): ['Airplane Arms', 'Airplane Arms'], ('Reverse Warrior', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Low Lunge'): ['Warrior 1'], ('Low Lunge', 'Warrior 1'): ['Humble Warrior'], ('Warrior 1', 'Humble Warrior'): ['Pyramid'], ('Humble Warrior', 'Pyramid'): ['Revolved Triangle'], ('Pyramid', 'Revolved Triangle'): ['High-to-Low Plank'], ('Revolved Triangle', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Chair Pose'): ['Prayer Twist'], ('Chair Pose', 'Prayer Twist'): ['High-to-Low Plank'], ('Prayer Twist', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Star'): ['Horse'], ('Star', 'Horse'): ['Star'], ('Horse', 'Star'): ['Wide Leg Forward Fold'], ('Star', 'Wide Leg Forward Fold'): ['Low Lunge'], ('Wide Leg Forward Fold', 'Low Lunge'): ['Fallen Triangle'], ('Low Lunge', 'Fallen Triangle'): ['Half Pigeon'], ('Fallen Triangle', 'Half Pigeon'): ['Cobra'], ('Half Pigeon', 'Cobra'): ['Seated Forward Fold'], ('Cobra', 'Seated Forward Fold'): ['Happy Baby'], ('Seated Forward Fold', 'Happy Baby'): ['Supine Figure 4', None], ('Happy Baby', 'Supine Figure 4'): ['Savasana'], ('Supine Figure 4', 'Savasana'): [None]}

final_dict = dict_1

for key, value_list in dict_2.items():
    if key not in final_dict.keys():
        final_dict[key] = value_list
    if key in final_dict.keys():
        for value in value_list:
            if value not in final_dict[key]:
                final_dict[key].append(value)


final_dict_hard_coded_in = {("Child's Pose", 'Downward-Facing Dog'): ['Ragdoll', 'Forward Fold', 'Table Top'], ('Downward-Facing Dog', 'Ragdoll'): ['Standing at Attention'], ('Ragdoll', 'Standing at Attention'): ['Mountain Pose', None], ('Standing at Attention', 'Mountain Pose'): ['Forward Fold', 'Side Body Stretch'], ('Mountain Pose', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift', 'Halfway Lift'], ('Forward Fold', 'Halfway Lift'): ['High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank'], ('Halfway Lift', 'High-to-Low Plank'): ['Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog'], ('High-to-Low Plank', 'Upward-Facing Dog'): ['Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog', 'Downward-Facing Dog'], ('Upward-Facing Dog', 'Downward-Facing Dog'): ['Mountain Pose', 'Mountain Pose', 'Chair', 'Warrior 2', 'Chair', 'Warrior 2', 'Chair', 'Warrior 2', 'Crescent Lunge', 'Low Lunge', 'Chair Pose', 'Star'], ('Downward-Facing Dog', 'Mountain Pose'): ['Forward Fold', 'Forward Fold', 'Side Body Stretch'], ('Downward-Facing Dog', 'Chair'): ['Forward Fold', 'Forward Fold', 'Forward Fold', 'Airplane Arms'], ('Chair', 'Forward Fold'): ['Halfway Lift', 'Halfway Lift', 'Halfway Lift'], ('Downward-Facing Dog', 'Warrior 2'): ['Extended Side Angle', 'Extended Side Angle', 'Extended Side Angle'], ('Warrior 2', 'Extended Side Angle'): ['Reverse Warrior', 'Reverse Warrior', 'Reverse Warrior'], ('Extended Side Angle', 'Reverse Warrior'): ['High-to-Low Plank', 'High-to-Low Plank', 'High-to-Low Plank', 'Chair'], ('Reverse Warrior', 'High-to-Low Plank'): ['Upward-Facing Dog', 'Upward-Facing Dog', 'Upward-Facing Dog'], ('Downward-Facing Dog', 'Crescent Lunge'): ['Revolved Crescent'], ('Crescent Lunge', 'Revolved Crescent'): ["Runner's Lunge"], ('Revolved Crescent', "Runner's Lunge"): ['Side Plank'], ("Runner's Lunge", 'Side Plank'): ['Prayer Twist'], ('Side Plank', 'Prayer Twist'): ['Gorilla'], ('Prayer Twist', 'Gorilla'): ['Crow'], ('Gorilla', 'Crow'): ['Eagle'], ('Crow', 'Eagle'): ['Dancer'], ('Eagle', 'Dancer'): ['Tree'], ('Dancer', 'Tree'): ['Warrior 1'], ('Tree', 'Warrior 1'): ['Warrior 2'], ('Warrior 1', 'Warrior 2'): ['Triangle'], ('Warrior 2', 'Triangle'): ['Wide Leg Forward Fold'], ('Triangle', 'Wide Leg Forward Fold'): ['Half Pigeon'], ('Wide Leg Forward Fold', 'Half Pigeon'): [
    'Cobra'], ('Half Pigeon', 'Cobra'): ['Bow', 'Seated Forward Fold', 'Savasana'], ('Cobra', 'Bow'): ['Camel'], ('Bow', 'Camel'): ['Bridge'], ('Camel', 'Bridge'): ['Reclined Bound Angle'], ('Bridge', 'Reclined Bound Angle'): ['Seated Forward Fold'], ('Reclined Bound Angle', 'Seated Forward Fold'): ['Happy Baby'], ('Seated Forward Fold', 'Happy Baby'): ['Supine Twist', 'Supine Figure 4', None], ('Happy Baby', 'Supine Twist'): ['Savasana'], ('Supine Twist', 'Savasana'): [None], ("Child's Pose", 'Table Top'): ['Cow'], ('Table Top', 'Cow'): ['Cat'], ('Cow', 'Cat'): ['Cow', 'Thread the Needle'], ('Cat', 'Cow'): ['Cat'], ('Cat', 'Thread the Needle'): ['Downward-Facing Dog'], ('Thread the Needle', 'Downward-Facing Dog'): ['Standing at Attention'], ('Downward-Facing Dog', 'Standing at Attention'): ['Mountain Pose', None], ('Mountain Pose', 'Side Body Stretch'): ['Baby Back Bend', 'Baby Back Bend'], ('Side Body Stretch', 'Baby Back Bend'): ['Mountain Pose', 'Mountain Pose'], ('Baby Back Bend', 'Mountain Pose'): ['Forward Fold', 'Forward Fold'], ('Chair', 'Airplane Arms'): ['Crescent Lunge'], ('Airplane Arms', 'Crescent Lunge'): ['Open Twist', 'Open Twist', 'Open Twist'], ('Crescent Lunge', 'Open Twist'): ['Crescent Lunge'], ('Open Twist', 'Crescent Lunge'): ['Warrior 2'], ('Crescent Lunge', 'Warrior 2'): ['Extended Side Angle', 'Extended Side Angle', 'Extended Side Angle'], ('Reverse Warrior', 'Chair'): ['Airplane Arms', 'Airplane Arms'], ('Downward-Facing Dog', 'Low Lunge'): ['Warrior 1'], ('Low Lunge', 'Warrior 1'): ['Humble Warrior'], ('Warrior 1', 'Humble Warrior'): ['Pyramid'], ('Humble Warrior', 'Pyramid'): ['Revolved Triangle'], ('Pyramid', 'Revolved Triangle'): ['High-to-Low Plank'], ('Revolved Triangle', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Chair Pose'): ['Prayer Twist'], ('Chair Pose', 'Prayer Twist'): ['High-to-Low Plank'], ('Prayer Twist', 'High-to-Low Plank'): ['Upward-Facing Dog'], ('Downward-Facing Dog', 'Star'): ['Horse'], ('Star', 'Horse'): ['Star'], ('Horse', 'Star'): ['Wide Leg Forward Fold'], ('Star', 'Wide Leg Forward Fold'): ['Low Lunge'], ('Wide Leg Forward Fold', 'Low Lunge'): ['Fallen Triangle'], ('Low Lunge', 'Fallen Triangle'): ['Half Pigeon'], ('Fallen Triangle', 'Half Pigeon'): ['Cobra'], ('Cobra', 'Seated Forward Fold'): ['Happy Baby'], ('Happy Baby', 'Supine Figure 4'): ['Savasana'], ('Supine Figure 4', 'Savasana'): [None], ('Cobra', 'Savasana'): [None], ('Downward-Facing Dog', 'Forward Fold'): ['Halfway Lift'], ('Happy Baby', 'Savasana'): [None], ('Downward-Facing Dog', 'Table Top'): ['Cow']}


def final_sequences(session_length="long"):
    """Function wrapper that uses the hard coded in data.
    Short or long session length.
    """

    return make_sequence(final_dict_hard_coded_in, session_length)


# loop through each key in dict 1, loop through each key in dict 2
# append key value into final dict
# if key already exists final_dict, append values to current list of values
# if key doesn't exist, create key value pair

# mini test case
# ("Child's Pose", 'Downward-Facing Dog'): ['Ragdoll']
# add to final_dict
# ('Downward-Facing Dog', 'Ragdoll'): ['Standing at Attention']
# add to final_dict


#---------------------------------------------------------------------#

# a = make_default_sequence('data/sequences/sequence1.txt')
# b = generate_sequence('data/sequences/sequence2.txt')

# print(generate_list_of_pose_objs(a))
# print(generate_seq_list_of_pose_objs(b))


filepath = 'data/sequences/sequence2.txt'
opened_file = open_and_read_file(filepath)
new_list = make_list(opened_file)
chains = make_chains(new_list)
# new_sequence = make_sequence(chains)
# print(new_sequence)

# print(chains)


def create_long_sequence():
    """ Generates a random, long yoga sequence  """

    return final_sequences('long')


# This doesn't work because there is not enough endings.
def create_short_sequence():
    """ Generates a random, short yoga sequence """

    return final_sequences('short')
