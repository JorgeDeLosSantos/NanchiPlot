# -*- coding: utf-8 -*-
import numpy as np

def isempty(iterable):
    if not iterable:
        return True
    else:
        return False

def rgb2hex(r,g,b):
    R = hex(r)[2:]
    if len(R)==1: R = 2*R
    G = hex(g)[2:]
    if len(G)==1: G = 2*G
    B = hex(b)[2:]
    if len(B)==1: B = 2*B
    HEX = "#"+R+G+B
    return HEX
        
if __name__=='__main__':
    pass
    
