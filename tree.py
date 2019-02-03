#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:10:49 2019

@author: sharon
"""

class Node:
    def __init__(self,num = None):
        self.data = num
        self.left = None
        self.right = None
        
    def bst_insert(self,data):
        if self.data is not None:
            print('Root data is ',self.data)
            if data < self.data:
                print('%d is smaller than root data %d'%(data,self.data))
                if self.left is None:
                    print('The left is None so self.left = Node(%d)'%data)
                    self.left = Node(data)
                else:
                    print('The left side is not None. Going to the left Node')
                    self.left.bst_insert(data)
            else:
                print('%d is greater than root data %d'%(data,self.data))
                if self.right is None:
                    print('The right is None so self.right = Node(%d)'%data)
                    self.right = Node(data)
                else:
                    print('The right side is not None. Going to the right Node')
                    self.right.bst_insert(data)
        else:
            print('Data is None but it is a Node which is visited!')
            self.data = data
    
    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            print('Which side left/right?[l/r]:', end = " ")
            ch = input()
            
            if ch == "l":
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif ch == "r":
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                print('Invaid option!')

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
            



    
    
        
    
        