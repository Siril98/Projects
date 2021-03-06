# File:        speedTicket.py
# Author:      Siril Pattammady
# Date:        9/26/2016
# Section:     SECTION NUMBER 6 
# E-mail:      psiril1@umbc.edu
# Description: A program to a help police officer calculate the appropriate fine
#              for driving over the speed limit.
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself.

def main():

    speed_limit = int(input("Please enter the speed limit in MPH:"))
    drive_speed = int(input("Please enter your driving speed in MPH:"))
    speed_dif = (drive_speed-speed_limit)
    print(" You were over the speed limit by",speed_dif, "MPH")
    if speed_dif < 10:
        print("You recieve no ticket...this time.")
    elif speed_dif >= 10 or speed_dif < 25:
        print("You recieve a ticket for $75.")
    elif speed_dif >= 25 or speed_dif < 30:
        print("You recieve a ticket for $150.")
    elif speed_dif >= 30:
        print("You recieve a ticket for a $500 fine, and a mandatory court date.")
    
        
        
main()
