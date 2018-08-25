# -*- coding: utf-8 -*-
"""TextRank summariser using NLTK.
   NLTK implements the similarity measure for us.
   
   Basic idea:
   1. use similarity measure to build adjacency matrix 
   2. A[i][j] contains the similarity measure between sentences i and j
   3. sentences that are similar to each other can be represented by 1 of the sentences
   4. naive way of doing this is literally just to go through the matrix row by row
   5. everytime you see a row, you pick the sentences that are similar to it (by defining some sensible threshold)
   6. pick this sentence, eject all rows corresponding to this sentnece and the ones it is similar to
   7. repeat until matrix is empty
   
   Todo: 
       1. Test threshold.
       2. Add tests for all functions.
   
"""

from nltk.corpus import brown, stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np


def summarise(content):
    """Generates list of sentences that summarise given content.
       
       Args:
           content (beautifulsoup object): Unsummarised text.
       
       Returns:
           list: summary. List of sentences that summarise content.

    """
    summary = set()
    threshold = 0.8 # to be tested
    matrix, tokenised = build_matrix(content) 
    matrix = np.sort(matrix)
    for row in matrix:
        for i in range(len(row)):
            if row[i] >= threshold:
                np.delete(matrix, i, 0) 
        summary.add(tokenised[i])
    return summary


def build_matrix(content):
    """Creates similarity matrix of raw text content.
       
       Args:
           content (beautifulsoup object): Unsummarised text.
       
       Returns:
           list of lists: rows. Matrix of similarity coefficients.
           list: tokenised. Tokenised content.
    """
    # use some parser to get sentences
    stop_words = set()
    seen = set()
    tokenised = sent_tokenize(content)
    rows = [0]*len(tokenised)
    for sentence in tokenised:
        for word in word_tokenize(sentence):
            if word in stopwords.words('english'):
                stop_words.add(word)
    for i in range(len(tokenised)):
        sentence = tokenised[i]
        seen.add(sentence)
        vector = np.array([similarity(sentence, s, stop_words) for s in tokenised and s not in seen]) 
        rows[i] == vector 
    for row in rows: 
        row = row/sum(row)
    return rows, tokenised


def similarity(s_1, s_2, stop_words=None):
    """Get similarity between the two sentences.

       Args:
           s_1 (string): Sentence.
           s_2 (string): Sentence.
           stop_words (set): Set of stopwords.
       
       Returns:
           float: similarity. Similarity coeffcient between the two sentences.
    """
    if stop_words == None: stop_words = []
    s_1_words = word_tokenize(s_1) 
    s_2_words = word_tokenize(s_2)
    all_words = s_1_words
    for word in s_2_words:
        if word not in all_words:
            all_words.add(word)
    all_words = list(all_words) # count number of occurrences of each word in each sentence
    v_1 = [0]*len(all_words)
    v_2 = [0]*len(all_words)
    for word in s_1_words:
        if word not in stop_words:
            v_1[all_words.index(word)] += 1
    for word in s_2_words:
        if word not in stop_words:
            v_2[all_words.index(word)] += 1 
    similarity = 1-cosine_distance(v_1, v_2) 
    return similarity 
