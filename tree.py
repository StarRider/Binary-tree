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
    #******************verticalOrder Supplimentory funcitons*******************
    # to find the maximum and minimum distac from the root
    def findMinMAx(self,minimum,maximum,hd):
        if self.data is None:
            return
        else:
            if hd > maximum[0]:
                maximum[0] = hd
            elif hd < minimum[0]:
                minimum[0] = hd
            if self.right:
                self.right.findMinMAx(minimum,maximum,hd+1)
            if self.left:
                self.left.findMinMAx(minimum,maximum,hd-1)

    # prints the nodes present in that line
    def printVerticalLine(self,line_no,hd):
        if self.data is not None:
            if line_no == hd:
                print(self.data,end=" ")
            if self.right:
                self.right.printVerticalLine(line_no,hd+1)
            if self.left:
                self.left.printVerticalLine(line_no,hd-1)
    #******************verticalOrder Supplimentory funcitons*******************
    
    def verticalOrder(self):
        maximum = [0]
        minimum = [0]
        
        # find the maximum and minimum
        self.findMinMAx(minimum,maximum,0)
    
        for line_no in range(minimum[0],maximum[0]+1):
            self.printVerticalLine(line_no,0)
            print()
            
    
            
x = Node(5)
x.bst_insert(3)
x.bst_insert(1)
x.bst_insert(4)
x.bst_insert(6)



    
    
        
    
        