#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 rzavalet <rzavalet@noemail.com>
#
# Distributed under terms of the MIT license.

"""
An implementation of a Hash using mod.
Please implement the requiered methods.
"""

from HashScheme import HashScheme
import hashlib

from consistent_hash.Store import Node

class ModHash(HashScheme):

    def __init__(self):
        """
        You have to decide what members to add to the class
        """
        self.__scheme_name = 'Modular_Hash'
        self.nodes = {}
        self.count = 0

    def get_name(self):
        return self.__scheme_name

    def __get_hash(self, value):
        """
        Calculates an initial hash using md5.
        """
        return int(hashlib.md5(value.encode()).hexdigest(),16) % 1000

    def dump(self):
        """
        Auxiliary method to print out information about the hash
        """
        for k in self.nodes.keys():
            print ("Node: {0} hash: {1}".format(self.nodes[k], k))

    def add_node(self, new_node):
        """
        Possibly just increment a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        self.nodes[self.count] = new_node
        self.count = self.count + 1
        return 0
        

    def remove_node(self, node):
        """
        Possibly just decrement a counter of number of nodes. You may also
        need to update Store to react in certain way depending on the
        scheme_name.
        """
        if self.nodes != 0:
            del self.nodes[self.count]
            self.count = self.count - 1
            return 0
        return 1
        

    def hash(self, value):
        """
        Convert value to a number representation and then obtain mod(number_of_nodes)
        """

        hash_value = self.__get_hash(value)

        return self.nodes[hash_value%self.count]

