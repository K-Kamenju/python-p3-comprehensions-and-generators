#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [i for i in num_list if i % 2 == 0]
    return even_numbers


def make_exclamation(sentence_list):
    add_exclamation = [f"{i}!" for i in sentence_list]
    return add_exclamation

