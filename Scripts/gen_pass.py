#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import string
import itertools

def generate_passwords(password_length):
    """Generate all possible combinations of characters for a given length"""
    all_combinations = itertools.product(string.printable, repeat=password_length)
    return (''.join(combination) for combination in all_combinations)
