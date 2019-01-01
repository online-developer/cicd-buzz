#!/usr/bin/env python

import unittest
from buzz import generator


def test_sampling_single_word():
    words = ('foo', 'bar', 'foobar')
    word = generator.sampling(words, 1) 
    assert word in words 


def test_sampling_multiple_word():
    words = ('foo', 'bar', 'foobar')
    word = generator.sampling(words, 2) 
    assert len(word) == 2
    assert word[0] in words 
    assert word[1] in words 
    assert word[0] is not word[1] 


def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 15

