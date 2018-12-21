#!/usr/bin/env python

from __future__ import print_function
from random import sample

buzz = ('continuous testing', 'continuous integration', 'continous deployment', 'continous improvement', 'devops')
adjectives = ('complete', 'mordern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substaintially', 'significantly', 'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')

def sampling(words, n = 1):
    result = sample(words, n)
    if n == 1:
        return result[0]
    return result


def generate_buzz():
    buzz_terms = sampling(buzz, 2)
    phrase = ' '.join([sampling(adjectives), buzz_terms[0], sampling(adverbs), sampling(verbs), buzz_terms[1]])
    return phrase.title()


if __name__ == '__main__':
    print(generate_buzz())
