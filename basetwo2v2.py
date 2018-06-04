#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 22:58:35 2018

@author: armendlulani
"""
#print the base n representation of any integer m
#d=qb + r

m = input("Enter an integer: ")
n = input("Convert to base: ")

remone = (int(m)%int(n))
quoone = (int(m)//int(n))

def div_algo_one():
    if quoone < 1:
        print(remone)

quotwo = (quoone//int(n))
remtwo = (quoone)%int(n)
        
def div_algo_two():
    div_algo_one();
    if quotwo < 1 :
        print(remtwo, remone)
        
remthree = (quotwo%int(n))
quothree = (quotwo)//int(n)

def div_algo_three():
    div_algo_two();
    if quothree < 1:
        print(remthree,remtwo,remone)
        
remfour = (quothree%int(n))
quofour = (quothree)//int(n)


def div_algo_four():
    div_algo_three();
    if quofour < 1:
        print(remfour,remthree,remtwo,remone)
        
def div_algo_n():
    div_algo_four();
div_algo_n();

#how to extend the algorithm using repeating functions?
#how to terminate the program as soon as a quotient is < 1 ?
