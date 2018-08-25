import pytest
from flask import g, session
from medileaks.summariser.extractive_summariser import (
    summarise, build_matrix, similarity
)

def test_summarise():
    """Todo:
           1. Test that the output is a list of strings.
           2. Test that the 1-cosine_distance between each pair of strings is higher than your set threshold.
              This essentially just means that you can't summarise this further.
           3. If you want to know that each string is a sentence, that's a question of using NLTK well, not a question of whether you've implemented everything else well.
    """
    raise NotImplementedError

def test_build_matrix():
    raise NotImplementedError

def test_similarity():
    raise NotImplementedError
