
# File: hw4_part4.py
# Author: Siril Pattammady
# Date: 10/11/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A program that prompts the user for two strings; it should ask for the
# longer string first. Then will check the longer string for instances of
# the shorter string. If you find one, print out the index the match started at.
# Collaboration:
# I collaborated with harsh3@umbc.edu and Professor Gibson. They helped me uslicing.

def main():

    first = input("First (longer) string:")
    first = first.upper()
    second = input("Second (shorter) string :")
    second_1 = second
    second = second.upper()
    

    for f in range(len(first)):
        if(first[f : f + len(second)])==second:
            print("At index",f, "found a slice of" ,second_1,)
        
        
                         
                         

    
main()
