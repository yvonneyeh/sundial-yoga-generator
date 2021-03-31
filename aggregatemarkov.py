"""Generate all_chains_dict (Markov chains dictionary) from all sequences txt files."""

from random import choice
from crud import get_pose_by_name_eng
import markov
import os

all_chains_dict = {}

Path = "data/sequences/"
filelist = os.listdir(Path)
for file in filelist:
    if file.endswith(".txt"):
        text = markov.open_and_read_file("data/sequences/" + file)
        poses = markov.make_list(text)
        chains_dict = markov.make_chains(poses)
        markov.add_to_all_chains_dict(chains_dict, all_chains_dict)

# all_chains_dict is our aggregated dictionary! <3 Rachel
print("\n\n\nTHIS IS OUR AGGREGATED DICTIONARY:", all_chains_dict, "\n\n\n")