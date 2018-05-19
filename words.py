#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 12:39:39 2018

@author: Ankit
"""

"""
This module is used to fetch data from provided URL.

Usage: python words.py 'http://sixty-north.com/c/t.txt'
"""
import sys
from urllib2 import urlopen


def fetchFromUrl(url):
    """
    Fetch the data from the provided URL
    input: URL
    output: list of data fetched from URL
    """
    #'http://sixty-north.com/c/t.txt'
    story = urlopen(url)
    story_words = []
    for line in story:
        for words in line.split():
            story_words.append(words)
    
    return story_words

def printItems(items): 
    """
    Print the items
    
    input: list of items
    
    output: prints each item in list
    """
    for item in items:
        print item 
        
def main(url):
    
    Item = fetchFromUrl(url)
    printItems(Item)
    
    
if __name__== "__main__":
    url = sys.argv[1] # first argument will be file name
    main(url)