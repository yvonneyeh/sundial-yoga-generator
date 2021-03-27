"""Generate Markov chains from txt files."""

import sys
from random import choice


def open_and_read_file(filepath):
    """Take file path as string; return text as string.
    """

    pose_list = []
    file = open(filepath)
    text = file.read()
    file.close()

    poses = text_string.split(",")

    return pose_list


def make_chains(pose_list):
    """Take input text as string; return dictionary of Markov chains."""
