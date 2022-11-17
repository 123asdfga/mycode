#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:01:41 2022

@author: ubuntu
"""
#
class Node:
    
    def __init__(self,value):
        self._value = value
        self._children = []
        
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    
    def add_child(self,node):
        self._children.append(node)
        
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
#Example
def jumping_range(N):
    index = 0 
    while index < N:
        print('star!!')
        print('index is:',index)
        jump = yield index
        print("jump is:",jump)
        print("index yield is:",index)
        print('end@@')
        if jump is None:
            jump = 1
        index += jump  
class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
    for rr in reversed(Countdown(30)):
        print(rr)
    for rr in Countdown(30):
        print(rr)
    
 