#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:53:29 2018

@author: Ankit


Example to demonstarte the use of generators in python

debugging this example will explain how generators work 
and the significance of yield keyword.
"""

def gen123():
    yield 1
    yield 2
    yield 3
    return

g=gen123()

print g.next()
print g.next()
print g.next()

print "*"*10


def run_take(count,iterable):
    counter=0
    for item in iterable:
        if counter==count:
            return
        counter+=1
        yield item
def run_take_distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_pipeline(count,iterable):
    for item in run_take(4,run_take_distinct(iterable)):
        print item

def main():
    items = [1,2,3,4,5]
    for item in run_take(4,items):
        print(item)
        
    print "*"*10
    
    items =[1,2,2,3,4,4,4,4,5,6,6,6,6,7,7,7,7,7]
    
    for item in run_take_distinct(items):
        print(item)
        
    print "*"*10
    
    run_pipeline(4,items)
        
if __name__=="__main__":
    main()


# next call to new_g.next() will throw a StopIteration exception