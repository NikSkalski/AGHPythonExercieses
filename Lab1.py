#!/usr/bin/env python3
print "Hello World"
name, surename ,date = raw_input("Enter Your Name,Surname and date of birth").split()

code=raw_input("Enter Your Code: ")
while(1):
    attempt = raw_input("Enter password: ")
    if(attempt==code):
        print("Great!")
        exit(0)
    print("wrong")

